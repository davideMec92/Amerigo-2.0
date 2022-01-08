from __future__ import annotations
from typing import List
from typing import TYPE_CHECKING
from project.hashgraph.interfaces.JsonPrintable import JsonPrintable
from project.hashgraph.tests.helpers.DatetimeHelper import DatetimeHelper

if TYPE_CHECKING:
    from project.hashgraph.models.Event import Event
    from project.hashgraph.models.Peer import Peer

from project.hashgraph.models.EventPeerAssociation import EventPeerAssociation
from project.hashgraph.models.Transaction import Transaction
from project.hashgraph.helpers.Hash import Hash


class EventBody(JsonPrintable):
    def __init__(self):
        self.creatorAssociation: EventPeerAssociation | None = None
        self.selfParentHash: str | None = None
        self.otherParentHash: str | None = None
        self.transactions: List[Transaction] = []
        self.selfParent: EventPeerAssociation | None = None
        self.otherParent: EventPeerAssociation | None = None
        self.timestamp: int | None = None

    @staticmethod
    def createFirstPeerEventBody(creator: Peer) -> EventBody:
        eventBody = EventBody()
        eventBody.creatorAssociation = EventPeerAssociation(creator.deviceId, creator.creatorIndex)
        eventBody.timestamp = DatetimeHelper.getNowTimestamp()
        return eventBody

    @staticmethod
    def createEventBody(transactions: List[Transaction], selfParent: Event, otherParent: Event, creator: Peer) -> EventBody:
        eventBody = EventBody()
        eventBody.transactions = transactions
        eventBody.selfParent = EventPeerAssociation(selfParent.eventBody.creatorAssociation.peerDeviceId,
                                                    selfParent.eventBody.creatorAssociation.eventCreatorIndex)
        eventBody.otherParent = EventPeerAssociation(otherParent.eventBody.creatorAssociation.peerDeviceId,
                                                     otherParent.eventBody.creatorAssociation.eventCreatorIndex)
        eventBody.creatorAssociation = EventPeerAssociation(creator.deviceId, creator.creatorIndex)
        eventBody.timestamp = DatetimeHelper.getNowTimestamp()
        eventBody.selfParentHash = Hash.stringToHash(selfParent.eventBody.toJson())
        eventBody.otherParentHash = Hash.stringToHash(otherParent.eventBody.toJson())
        return eventBody

    def getCreator(self) -> str:
        return self.creatorAssociation.peerDeviceId

    def getCreatorIndex(self) -> int:
        return self.creatorAssociation.eventCreatorIndex
