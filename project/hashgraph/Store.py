from __future__ import annotations

from multiprocessing.sharedctypes import synchronized
from typing import List

from project.hashgraph.Event import Event
from project.hashgraph.Round import Round
from project.hashgraph.dictTypes.StoreEvent import StoreEvent
from project.hashgraph.dictTypes.StoreRound import StoreRound
from project.hashgraph.helpers.Hash import Hash
from project.hashgraph.helpers.ListHelper import ListHelper
from project.hashgraph.interfaces.StoreCallback import StoreCallback


class Store:
    events: StoreEvent
    rounds: StoreRound
    lastMissingEvents: List[Event]
    storeCallback: StoreCallback

    ROUND_DELETE_MARGIN = 1

    # TODO ADD CALLBACK FOR storeCallback
    def __init__(self, storeCallback: StoreCallback):
        self.storeCallback = storeCallback

    # TODO ADD STORE CLONE FUNCTION

    def getEvents(self):
        return self.events

    def getRounds(self):
        return self.rounds

    def getLastMissingEvents(self):
        return self.getLastMissingEvents

    def clearLastMissingEvents(self):
        self.lastMissingEvents = []

    def setEvents(self, events):
        self.events = events

    def setRounds(self, rounds):
        self.rounds = rounds

    # TODO ADD putRound METHOD
    def putRound(self, round: Round):

        # Check if round exists in order to add a single missing event
        if  round.roundCreated in self.rounds:

            # TODO TO TEST
            for eventKey in ListHelper.getListDiff(self.rounds.get(round.roundCreated).events, round.events):
                self.rounds.get(round.roundCreated).witnesses.append(eventKey)

            # for(String eventKey: ListHelper.getListDiff(this.rounds.get(round.getRoundCreated()).getEvents(), round.getEvents())){
            #     this.rounds.get(round.getRoundCreated()).getEvents().add(eventKey);
            # }

            # TODO TO TEST
            for witnessEventKey in ListHelper.getListDiff(self.rounds.get(round.roundCreated).witnesses, round.witnesses):
                self.rounds.get(round.roundCreated).witnesses.append(witnessEventKey)

            # for(String witnessEventKey: ListHelper.getListDiff(this.rounds.get(round.getRoundCreated()).getWitnesses(), round.getWitnesses())){
            #     this.rounds.get(round.getRoundCreated()).getWitnesses().add(witnessEventKey);
            # }

        else:
            self.rounds.append(round.roundCreated, round)

    def deleteEventFromKey(self, eventKey):
        self.events.pop(eventKey, None)

    @synchronized
    def deleteRoundFromRoundCreatedIndex(self, roundCreated):
        self.rounds.pop(roundCreated, None)

    def storeEvent(self, event):
        self.events[event.getEventBody().getCreatorAssociation().getKey()] = event
        self.storeCallback.eventStoredCallback(self.events.get((event.getEventBody().getCreatorAssociation().getKey())))

    def updateEvent(self, event):
        self.events[event.getEventBody().getCreatorAssociation().getKey()] = event

    def addEventInRound(self, event):
        self.rounds.get(event.getRoundCreated()).addEvent(event.getEventBody().getCreatorAssociation().getKey())

    # TODO TO TEST
    def storeMissingEvents(self, otherHashgraph: "Store", peerDeviceId: str, firstMissingEventCreatorIndex: int):
        missingCreatorEventIndex: int = firstMissingEventCreatorIndex
        missingEvent: Event = otherHashgraph.getEventFromPeerAndCreatorIndex(peerDeviceId, missingCreatorEventIndex)

        while missingEvent is not None:
            self.storeEvent(missingEvent)
            missingCreatorEventIndex = missingCreatorEventIndex + 1
            missingEvent = otherHashgraph.getEventFromPeerAndCreatorIndex(peerDeviceId, missingCreatorEventIndex)

            if missingEvent is None:
                self.lastMissingEvents.append(self.getEventFromPeerAndCreatorIndex(peerDeviceId, missingCreatorEventIndex - 1))

    def getEventFromPeerAndCreatorIndex(self, peerDeviceId, peerCreatorIndex) -> Event | None:
        hashKey = Hash.stringToHash(peerDeviceId + peerCreatorIndex)
        return self.getEventFromEventPeerAssociationKey(hashKey)

    def getEventFromEventPeerAssociationKey(self, eventPeerAssociationKey):
        return self.events.get(eventPeerAssociationKey) if eventPeerAssociationKey in self.events else None

    def getRoundFromRoundCreated(self, roundCreated):
        return self.rounds.get(roundCreated) if roundCreated in self.rounds else None

    def removeRoundsBeforeRoundCreatedIndex(self, roundCreatedIndex):
        toRemoveRoundCreatedIndex = (roundCreatedIndex - self.ROUND_DELETE_MARGIN)

        # Check if difference is negative
        if toRemoveRoundCreatedIndex < 0:
            return

        # TODO TO TEST!
        for k, v in self.rounds:
            if k < toRemoveRoundCreatedIndex:
                # Remove all events in round
                for eventKey in v.getEvents():
                    self.deleteEventFromKey(eventKey)

        # TODO TO TEST!
        for i in range(toRemoveRoundCreatedIndex - 1, 0, -1):
            if self.rounds.get(i) is None:
                break

            # Delete round
            self.deleteRoundFromRoundCreatedIndex(i)
