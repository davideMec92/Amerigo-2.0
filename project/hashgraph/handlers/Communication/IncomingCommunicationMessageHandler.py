from project.hashgraph.contexts.communication.ServerMessageHandlerContext import ServerMessageHandlerContext
from project.hashgraph.enums.CommunicationMessageTypes import CommunicationMessageTypes
from project.hashgraph.interfaces.Callbacks.CommunicationCallback import CommunicationCallback
from project.hashgraph.models.communication.CommunicationMessage import CommunicationMessage
from project.hashgraph.strategies.communication.HandleACKMessage import HandleACKMessage
from project.hashgraph.strategies.communication.HandleHashgraphStoreMessage import HandleHashgraphStoreMessage
from project.hashgraph.strategies.communication.HandleNACKMessage import HandleNACKMessage
from project.hashgraph.strategies.communication.HandlePeersListMessage import HandlePeersListMessage


class IncomingCommunicationMessageHandler(CommunicationCallback):

    def clientResponseCallback(self, message: CommunicationMessage) -> None:

        serverMessageHandlerContext: ServerMessageHandlerContext = None

        if message.type == CommunicationMessageTypes.PEERS_LIST:
            serverMessageHandlerContext = ServerMessageHandlerContext(HandlePeersListMessage())
        elif message.type == CommunicationMessageTypes.HASHGRAPH:
            serverMessageHandlerContext = ServerMessageHandlerContext(HandleHashgraphStoreMessage())
        elif message.type == CommunicationMessageTypes.ACK:
            serverMessageHandlerContext = ServerMessageHandlerContext(HandleACKMessage())
        elif message.type == CommunicationMessageTypes.NACK:
            serverMessageHandlerContext = ServerMessageHandlerContext(HandleNACKMessage())

        if serverMessageHandlerContext is not None:
            serverMessageHandlerContext.handleMessage(message)