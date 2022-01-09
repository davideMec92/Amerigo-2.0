from __future__ import annotations

from project.hashgraph.models.communication.CommunicationMessage import CommunicationMessage


class ServerMessageHandlerContext:

    def __init__(self, strategy: ServerMessageHandlerContext):
        self.strategy: ServerMessageHandlerContext = strategy

    def handleMessage(self, message: CommunicationMessage):
        self.strategy.handleMessage(message)
