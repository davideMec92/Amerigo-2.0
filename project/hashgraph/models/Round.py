from typing import List

from project.hashgraph.models.Event import Event
from project.hashgraph.helpers.ListHelper import ListHelper


class Round:
    roundCreated: int = -1
    roundReceived: int = -1
    events: List[str] = []
    determinedEvents: List[str] = []
    inRoundDeterminedEvents: List[str] = []
    witnesses: List[str] = []
    decidedWitnesses: List[str] = []
    peersInRound: int = None
    committed: bool = False

    def __init__(self, event: Event, peersInRound: int):
        if event is None:
            raise Exception('"event" parameter cannot be null')

        if peersInRound is None:
            raise Exception('"peersInRound" parameter cannot be null')

        self.roundCreated = event.roundCreated
        self.events.append(event.eventBody.creatorAssociation.key)
        self.peersInRound = peersInRound

        if event.isWitness is True:
            self.witnesses.append(event.eventBody.creatorAssociation.key)

    # def getEvents(self):
    #     return self.events
    #
    # def getWitnesses(self):
    #     return self.witnesses
    #
    # def getDeterminedEvents(self):
    #     return self.determinedEvents
    #
    # def getInRoundDeterminedEvents(self):
    #     return self.inRoundDeterminedEvents
    #
    # def getRoundCreated(self):
    #     return self.roundCreated
    #
    # def getRoundReceived(self):
    #     return self.roundReceived
    #
    # def isCommitted(self):
    #     return self.committed
    #
    # def getPeersInRound(self):
    #     return self.peersInRound

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
        return ListHelper.getListDiff(self.decidedWitnesses, self.witnesses).size() == 0

    def isDetermined(self):
        return ListHelper.getListDiff(self.determinedEvents, self.events).size() == 0
