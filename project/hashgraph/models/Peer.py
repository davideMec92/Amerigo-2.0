from typing import List

from project.hashgraph.models.EventBody import EventBody
from project.hashgraph.models.Event import Event
from project.hashgraph.enums.PeerStatus import PeerStatus
from project.hashgraph.models.Transaction import Transaction


class Peer:
    def __init__(self):
        # TODO IF NOT USED, REMOVE IT
        self.id: int | None = None
        self.deviceId: str | None = None
        self.address: str | None = None
        self.status: PeerStatus | None = None
        self.updatedTime: float | None = None
        self.creatorIndex: int = -1

    def incrementCreatorIndex(self):
        self.creatorIndex = self.creatorIndex + 1

    def createFirstEvent(self) -> Event | None:
        self.incrementCreatorIndex()

        if self.creatorIndex == 0:
            eventBody = EventBody.createFirstPeerEventBody(self)
            firstEvent = Event(eventBody)
            firstEvent.isWitness = True
            firstEvent.roundCreated = 1
            return firstEvent

        return None

    def createEvent(self, transactions: List[Transaction], myPeerLastEvent: Event, otherPeerLastEvent: Event) -> Event:
        self.incrementCreatorIndex()
        eventBody: EventBody = EventBody(transactions, myPeerLastEvent, otherPeerLastEvent, self)
        event: Event = Event(eventBody)
        return event
