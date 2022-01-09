from typing import Type

from project.hashgraph.models.communication.CommunicationMessage import CommunicationMessage


class ServerMessageHandlerStrategy:
    def handleMessage(self, message: Type[CommunicationMessage]) -> None:
        raise Exception('Method not implemented')