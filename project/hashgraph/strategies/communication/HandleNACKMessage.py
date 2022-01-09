from threading import Lock
from typing import Type

from project.Logger.Logger import Logger, LogLevels
from project.hashgraph.interfaces.Strategies.ServerMessageHandlerStrategy import ServerMessageHandlerStrategy
from project.hashgraph.models.GossipProtocol import GossipProtocol
from project.hashgraph.models.Hashgraph import Hashgraph
from project.hashgraph.models.communication.CommunicationMessage import CommunicationMessage
from project.hashgraph.models.communication.CommunicationMessageACK import CommunicationMessageACK


class HandleACKMessage(ServerMessageHandlerStrategy):

    lock = Lock()

    def __init__(self):
        self.hashgraph: Hashgraph | None = None

    def handleMessage(self, message: CommunicationMessageACK) -> None:
        Logger.createLog(LogLevels.DEBUG, __file__, 'Received ACK')
        self.hashgraph = Hashgraph.instance

        # Check if hashgraph is not initialized yet
        if self.hashgraph is None:
            Logger.createLog(LogLevels.DEBUG, __file__, 'Peer list not initialized, hashgraph null')
            print('Peer list not initialized, hashgraph null')
            return

        # Check if gossip is waiting an ACK to unlock receive semaphore
        if self.hashgraph.lockHashgraphGossip() is False:
            try:
                HandleACKMessage.lock.acquire()
                Logger.createLog(LogLevels.DEBUG, __file__, 'Try to unlock hashgraph receive lock..')
                self.hashgraph.unlockHashgraphReceive()
                if GossipProtocol.instance.unlockGossipProtocolEvent.is_set() is False:
                    GossipProtocol.instance.unlockGossipProtocolEvent.set()
                    Logger.createLog(LogLevels.DEBUG, __file__, 'unlockGossipProtocolEvent unlocked')
            finally:
                HandleACKMessage.lock.release()

