from typing import List

from project.hashgraph.models.EventBody import EventBody
from project.hashgraph.models.Event import Event
from project.hashgraph.enums.PeerStatus import PeerStatus
from project.hashgraph.models.Transaction import Transaction
from project.hashgraph.services.database.TinyDB.TinyDBModel import TinyDBModel
from project.hashgraph.services.database.TinyDB.TinyDBService import TinyDBService


class Peer(TinyDBModel):
    primaryKey = "deviceId"
    DB_NAME = 'peers_list'

    tinyDBService: TinyDBService = TinyDBService(DB_NAME)

    def __init__(self):
        super().__init__(Peer.tinyDBService, Peer.primaryKey)
        # TODO IF NOT USED, REMOVE IT
        self.id: int | None = None
        self.deviceId: str | None = None
        self.address: str | None = None
        self.status: PeerStatus | None = None
        self.updatedTime: int | None = None
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
        eventBody: EventBody = EventBody.createEventBody(transactions, myPeerLastEvent, otherPeerLastEvent, self)
        event: Event = Event(eventBody)
        return event
