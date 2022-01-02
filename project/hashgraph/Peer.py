from project.hashgraph.EventBody import EventBody
from project.hashgraph.Event import Event
from project.hashgraph.enums.PeerStatus import PeerStatus


class Peer:
    # TODO IF NOT USED, REMOVE IT
    id: int
    deviceId: str
    address: str
    status: PeerStatus
    updatedTime: float
    creatorIndex: int = -1

    def incrementCreatorIndex(self):
        self.creatorIndex = self.creatorIndex + 1

    def createFirstEvent(self) -> Event:
        self.incrementCreatorIndex()

        if self.creatorIndex == 0:
            eventBody = EventBody.createFirstPeerEventBody(self)
            firstEvent = Event(eventBody)
            firstEvent.isWitness = True
            firstEvent.roundCreated = 1
            return firstEvent

        return None
