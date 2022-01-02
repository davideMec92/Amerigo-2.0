from typing import List

from project.hashgraph.EventPeerAssociation import EventPeerAssociation
from project.hashgraph.Transaction import Transaction


class EventBlock:
    consensusTimestamp: float
    transactions: List[Transaction]
    creatorAssociation: EventPeerAssociation
    