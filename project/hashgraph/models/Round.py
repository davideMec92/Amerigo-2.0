from typing import List

from project.hashgraph.models.Event import Event
from project.hashgraph.helpers.ListHelper import ListHelper


class Round:

    def __init__(self, event: Event, peersInRound: int):
        if event is None:
            raise Exception('"event" parameter cannot be null')

        if peersInRound is None:
            raise Exception('"peersInRound" parameter cannot be null')

        self.roundCreated: int = event.roundCreated
        self.roundReceived: int = -1
        self.events: list[str] = []
        self.events.append(event.eventBody.creatorAssociation.key)
        self.determinedEvents: list[str] = []
        self.inRoundDeterminedEvents: list[str] = []
        self.witnesses: list[str] = []
        self.decidedWitnesses: list[str] = []
        self.peersInRound: int = peersInRound
        self.committed: bool = False

        if event.isWitness is True:
            self.witnesses.append(event.eventBody.creatorAssociation.key)

    def addEvent(self, eventKey: str):
        return self.events.append(eventKey)

    def addDeterminedEvent(self, eventKey: str):
        self.determinedEvents.append(eventKey)

    def addInRoundDeterminedEvent(self, eventKey: str):
        self.inRoundDeterminedEvents.append(eventKey)

    def addEvents(self, events: List[str]):
        if len(events) > 0:
            self.events.extend(events)

    def addWitnesses(self, witnesses: List[str]):
        if len(witnesses) > 0:
            self.witnesses.extend(witnesses)

    def addWitness(self, eventKey: str):
        self.witnesses.append(eventKey)

    def addDecidedWitness(self, eventKey: str):
        self.decidedWitnesses.append(eventKey)

    def getNotDecidedWitnesses(self):
        return ListHelper.getListDiff(self.decidedWitnesses, self.witnesses)

    def getPeersInSetSupermajority(self):
        return (self.peersInRound * 2) / 3.00

    def isDecided(self):
        return len(ListHelper.getListDiff(self.decidedWitnesses, self.witnesses)) == 0

    def isDetermined(self):
        return len(ListHelper.getListDiff(self.determinedEvents, self.events)) == 0
