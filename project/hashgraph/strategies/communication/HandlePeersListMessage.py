from project.Logger.Logger import LogLevels, Logger
from project.hashgraph.interfaces.Strategies.ServerMessageHandlerStrategy import ServerMessageHandlerStrategy
from project.hashgraph.models.GossipProtocol import GossipProtocol
from project.hashgraph.models.Hashgraph import Hashgraph
from project.hashgraph.models.communication.CommunicationMessagePeersList import CommunicationMessagePeersList


class HandlePeersListMessage(ServerMessageHandlerStrategy):

    def __init__(self):
        self.hashgraph: Hashgraph = Hashgraph.instance
        self.gossipProtocol: GossipProtocol | None = None
        self.myPeerDeviceId: str | None = None

    def handleMessage(self, message: CommunicationMessagePeersList) -> None:
        print('Saving peers list..')
        Logger.createLog(LogLevels.DEBUG, __file__, 'Try to unlock hashgraph gossip lock..')

