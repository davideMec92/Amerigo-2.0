from typing import List

from project.hashgraph.enums.CommunicationMessageTypes import CommunicationMessageTypes
from project.hashgraph.models.Peer import Peer
from project.hashgraph.models.communication.CommunicationMessage import CommunicationMessage


class CommunicationMessagePeersList(CommunicationMessage):
    def __init__(self):
        super().__init__()
        self.type = CommunicationMessageTypes.PEERS_LIST
        self.peers: List[Peer] = []
