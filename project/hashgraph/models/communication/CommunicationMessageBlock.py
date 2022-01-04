from project.hashgraph.enums.CommunicationMessageTypes import CommunicationMessageTypes
from project.hashgraph.models.Block import Block
from project.hashgraph.models.communication.CommunicationMessage import CommunicationMessage


class CommunicationMessageBlock(CommunicationMessage):
    def __init__(self, block: Block):
        super().__init__()
        self.type = CommunicationMessageTypes.BLOCK
        self.block = block
