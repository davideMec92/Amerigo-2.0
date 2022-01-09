from project.hashgraph.enums.CommunicationMessageTypes import CommunicationMessageTypes
from project.hashgraph.models.Hashgraph import Hashgraph
from project.hashgraph.models.Peer import Peer
from project.hashgraph.models.Store import Store
from project.hashgraph.models.communication.CommunicationMessage import CommunicationMessage


class CommunicationMessageHashgraph(CommunicationMessage):
    def __init__(self, hashgraph: Hashgraph):
        super().__init__()
        self.type = CommunicationMessageTypes.HASHGRAPH
        self.store: Store = hashgraph.store
        self.peer: Peer = hashgraph.myPeer
