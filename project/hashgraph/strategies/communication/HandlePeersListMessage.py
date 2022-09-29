import os
import traceback
from typing import Dict

from dotenv import load_dotenv

from project.Logger.Logger import LogLevels, Logger
from project.hashgraph.controllers.TinyDB.PeerController import PeerController
from project.hashgraph.interfaces.Strategies.ServerMessageHandlerStrategy import ServerMessageHandlerStrategy
from project.hashgraph.models.GossipProtocol import GossipProtocol
from project.hashgraph.models.Hashgraph import Hashgraph
from project.hashgraph.models.Peer import Peer
from project.hashgraph.models.communication.CommunicationMessagePeersList import CommunicationMessagePeersList

load_dotenv()

class HandlePeersListMessage(ServerMessageHandlerStrategy):

    def __init__(self):
        self.hashgraph: Hashgraph = Hashgraph.instance
        self.gossipProtocol: GossipProtocol = None
        self.myPeerDeviceId: str = None

    def handleMessage(self, message: CommunicationMessagePeersList) -> None:
        # Update local peer list
        PeerController.storeAll(message.peers)

        hashgraphPeersList: Dict[str, Peer] = {}
        myPeer: Peer = None
        myPeerDeviceId: str = os.getenv('DEVICE_ID')


        for peer in message.peers:
            hashgraphPeersList[peer.deviceId] = peer

            if peer.deviceId == myPeerDeviceId:
                myPeer = peer

        self.hashgraph = Hashgraph.instance

        if self.hashgraph is None:
            Logger.createLog(LogLevels.DEBUG, __file__, 'Init local hashgraph..')
            self.hashgraph = Hashgraph.getInstance(hashgraphPeersList, myPeer)

            # Create myPeer first event
            self.hashgraph.addUndeterminedEvents(myPeer.createFirstEvent())

            self.gossipProtocol = GossipProtocol(self.hashgraph, myPeerDeviceId)
            try:
                self.gossipProtocol.start()
            except:
                traceback.print_exc()
        else:
            self.gossipProtocol = GossipProtocol.instance

            if self.gossipProtocol is not None:
                self.hashgraph.peers = hashgraphPeersList
                self.gossipProtocol.updatePeerKeys()
            else:
                Logger.createLog(LogLevels.ERROR, __file__, 'Gossip protocol not initialized')
                raise Exception('At this point Gossip protocol cannot be None')



