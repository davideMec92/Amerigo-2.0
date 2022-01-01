import time
from typing import List

from project.hashgraph.Event import Event
from project.hashgraph.EventPeerAssociation import EventPeerAssociation
from project.hashgraph.Peer import Peer
from project.hashgraph.Transaction import Transaction
from project.hashgraph.helpers.Hash import Hash


class EventBody:

    creatorAssociation: EventPeerAssociation
    selfParentHash: str
    otherParentHash: str
    transactions: List[Transaction]
    selfParent: EventPeerAssociation
    otherParent: EventPeerAssociation
    timestamp: float

    @staticmethod
    def createFirstPeerEventBody(creator: Peer):
        eventBody = EventBody()
        eventBody.creatorAssociation = EventPeerAssociation(creator.deviceId, creator.creatorIndex)
        eventBody.timestamp = time.time()
        return eventBody

    @staticmethod
    def createEventBody(transactions: List[Transaction], selfParent: Event, otherParent: Event, creator: Peer):
        eventBody = EventBody()
        eventBody.transactions = transactions
        eventBody.selfParent = EventPeerAssociation(selfParent.eventBody.creatorAssociation.peerDeviceId, selfParent.eventBody.creatorAssociation.eventCreatorIndex)
        eventBody.otherParent = EventPeerAssociation(otherParent.eventBody.creatorAssociation.peerDeviceId, otherParent.eventBody.creatorAssociation.eventCreatorIndex)
        eventBody.creatorAssociation = EventPeerAssociation(creator.deviceId, creator.creatorIndex)
        eventBody.timestamp = time.time()
        # TODO ADD TO JSON METHOD
        eventBody.selfParentHash = Hash.stringToHash(selfParent.getEventBody().toJson())
        # TODO ADD TO JSON METHOD
        eventBody.otherParentHash = Hash.stringToHash(otherParent.getEventBody().toJson())

