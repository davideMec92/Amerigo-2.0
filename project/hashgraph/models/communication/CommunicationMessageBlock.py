from project.hashgraph.enums.CommunicationMessageTypes import CommunicationMessageTypes
from project.hashgraph.models.communication.CommunicationMessage import CommunicationMessage


class CommunicationMessageACK(CommunicationMessage):
    def __init__(self):
        super().__init__()
        self.type = CommunicationMessageTypes.ACK
