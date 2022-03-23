from __future__ import annotations

from project.hashgraph.interfaces.Callbacks.CommunicationCallback import CommunicationCallback
from project.hashgraph.models.communication.CommunicationMessage import CommunicationMessage


class CommunicationCallbackClass(CommunicationCallback):

    def clientResponseCallback(self, message: CommunicationMessage) -> None:
        print('Received message: ' + str(message))