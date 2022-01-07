from __future__ import annotations

import json
from functools import reduce
from lib2to3.pgen2.grammar import op
from threading import Lock
from typing import Dict

from project.Logger.Logger import LogLevels, Logger
from project.hashgraph.dictTypes.StoreRound import StoreRound
from project.hashgraph.helpers.Hash import Hash
from project.hashgraph.helpers.ListHelper import ListHelper
from project.hashgraph.helpers.models.JSONEncoders.StoreJSONEncoder import StoreJSONEncoder
from project.hashgraph.interfaces.JsonPrintable import JsonPrintable
from project.hashgraph.interfaces.StoreCallback import StoreCallback
from project.hashgraph.models.Event import Event
from project.hashgraph.models.Round import Round


class Store(JsonPrintable):
    ROUND_DELETE_MARGIN = 1
    lock = Lock()

    def __init__(self, storeCallback: StoreCallback | None):
        self.events: Dict[str, Event] = {}
        self.rounds: Dict[int, Round] = {}
        self.lastMissingEvents: list[Event] = []
        self.storeCallback: StoreCallback = storeCallback

    # TODO ADD STORE CLONE FUNCTION

    def getEvents(self):
        return self.events

    def getRounds(self) -> StoreRound:
        return self.rounds

    def getLastMissingEvents(self):
        return self.getLastMissingEvents

    def clearLastMissingEvents(self):
        self.lastMissingEvents = []

    def setEvents(self, events):
        self.events = events

    def setRounds(self, rounds):
        self.rounds = rounds

    def putRound(self, newRound: Round):
        # Check if round exists in order to add a single missing event
        if newRound.roundCreated in self.rounds:
            # TODO TO TEST
            for eventKey in ListHelper.getListDiff(self.rounds.get(newRound.roundCreated).events, newRound.events):
                self.rounds.get(newRound.roundCreated).witnesses.append(eventKey)

            # TODO TO TEST
            for witnessEventKey in ListHelper.getListDiff(self.rounds.get(newRound.roundCreated).witnesses, newRound.witnesses):
                self.rounds.get(newRound.roundCreated).witnesses.append(witnessEventKey)
        else:
            self.rounds[newRound.roundCreated] = newRound

    def deleteEventFromKey(self, eventKey):
        self.events.pop(eventKey, None)

    def deleteRoundFromRoundCreatedIndex(self, roundCreated):
        try:
            self.lock.acquire()
            self.rounds.pop(roundCreated, None)
        finally:
            self.lock.release()

    def storeEvent(self, event):
        self.events[event.eventBody.creatorAssociation.key] = event
        Logger.createLog(LogLevels.DEBUG, __file__, 'Added event with key: ' + event.eventBody.creatorAssociation.key)

        if self.storeCallback is not None:
            self.storeCallback.eventStoredCallback(self.events.get(event.eventBody.creatorAssociation.key))

    def updateEvent(self, event):
        self.events[event.eventBody.creatorAssociation.key] = event

    def addEventInRound(self, event):
        self.rounds.get(event.roundCreated).addEvent(event.eventBody.creatorAssociation.key)

    # TODO TO TEST
    def storeMissingEvents(self, otherHashgraph: "Store", peerDeviceId: str, firstMissingEventCreatorIndex: int):
        missingCreatorEventIndex: int = firstMissingEventCreatorIndex
        missingEvent: Event = otherHashgraph.getEventFromPeerAndCreatorIndex(peerDeviceId, missingCreatorEventIndex)

        while missingEvent is not None:
            self.storeEvent(missingEvent)
            missingCreatorEventIndex = missingCreatorEventIndex + 1
            missingEvent = otherHashgraph.getEventFromPeerAndCreatorIndex(peerDeviceId, missingCreatorEventIndex)

            if missingEvent is None:
                self.lastMissingEvents.append(
                    self.getEventFromPeerAndCreatorIndex(peerDeviceId, missingCreatorEventIndex - 1))

    def getEventFromPeerAndCreatorIndex(self, peerDeviceId, peerCreatorIndex) -> Event | None:
        hashKey = Hash.stringToHash(peerDeviceId + str(peerCreatorIndex))
        return self.getEventFromEventPeerAssociationKey(hashKey)

    def getEventFromEventPeerAssociationKey(self, eventPeerAssociationKey) -> Event:
        return self.events.get(eventPeerAssociationKey) if eventPeerAssociationKey in self.events else None

    def getRoundFromRoundCreated(self, roundCreated):
        return self.rounds.get(roundCreated) if roundCreated in self.rounds else None

    def removeRoundsBeforeRoundCreatedIndex(self, roundCreatedIndex):
        toRemoveRoundCreatedIndex = (roundCreatedIndex - self.ROUND_DELETE_MARGIN)

        # Check if difference is negative
        if toRemoveRoundCreatedIndex < 0:
            return

        # TODO TO TEST!
        for k, v in self.rounds.items():
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

    def toPrettyJson(self) -> str:
        return json.dumps(self, cls=StoreJSONEncoder, indent=4, sort_keys=True)

    def toJson(self) -> str:
        return json.dumps(self, cls=StoreJSONEncoder)
