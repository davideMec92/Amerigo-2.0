from project.hashgraph.models.EventPeerAssociation import EventPeerAssociation
from project.hashgraph.models.Transaction import Transaction


class EventBlock:
    def __init__(self):
        self.consensusTimestamp: int
        self.transactions: list[Transaction] = []
        self.creatorAssociation: EventPeerAssociation | None = None
