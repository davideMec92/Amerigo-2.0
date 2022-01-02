from typing import List

from project.hashgraph.models.EventPeerAssociation import EventPeerAssociation
from project.hashgraph.models.Transaction import Transaction


class EventBlock:
    consensusTimestamp: float
    transactions: List[Transaction]
    creatorAssociation: EventPeerAssociation
    