from __future__ import annotations

import json
import traceback
from typing import Dict
from project.hashgraph.models.Event import Event
from project.hashgraph.models.EventBody import EventBody
from project.hashgraph.models.EventPeerAssociation import EventPeerAssociation
from project.hashgraph.models.Round import Round
from project.hashgraph.models.Store import Store
from project.hashgraph.models.Transaction import Transaction
from project.hashgraph.validators.EventValidator import EventValidator


class StoreJSONDecoder:

    def decodeFromJsonString(self, jsonString: str) -> Store:
        try:
            storeDict = json.loads(jsonString)
            store: Store = Store(None)
            store.events = self.addEvents(storeDict.get('events'))
            store.rounds = self.addRounds(storeDict.get('rounds'))
        except Exception as e:
            print('StoreJSONDecoder exception: ' + str(e))
            traceback.print_exc()

        return store

    def decodeFromDict(self, storeDict: Dict) -> Store:
        try:
            store: Store = Store(None)
            store.events = self.addEvents(storeDict.get('events'))
            store.rounds = self.addRounds(storeDict.get('rounds'))
        except Exception as e:
            print('StoreJSONDecoder exception: ' + str(e))
            traceback.print_exc()

        return store

    def addRounds(self, rounds: Dict) -> Dict[int, round]:
        storeRounds: Dict[int, round] = {}

        for roundCreated, roundDict in rounds.items():
            newRound: Round = self.createRound(roundDict)
            storeRounds[newRound.roundCreated] = newRound

        return storeRounds

    def createRound(self, roundDict: Dict) -> Round:

        newRound: Round = Round()
        newRound.roundCreated = roundDict.get('roundCreated')
        newRound.roundReceived = roundDict.get('roundReceived')

        for eventKey in roundDict.get('events'):
            newRound.addEvent(eventKey)

        for determinedEventKey in roundDict.get('determinedEvents'):
            newRound.addDeterminedEvent(determinedEventKey)

        for inRoundDeterminedEventKey in roundDict.get('inRoundDeterminedEvents'):
            newRound.addInRoundDeterminedEvent(inRoundDeterminedEventKey)

        for eventKey in roundDict.get('witnesses'):
            newRound.addWitness(eventKey)

        for eventKey in roundDict.get('decidedWitnesses'):
            newRound.addDecidedWitness(eventKey)

        newRound.peersInRound = roundDict.get('peersInRound')
        newRound.committed = roundDict.get('committed')
        return newRound

    def addEvents(self, events: Dict) -> Dict[str, Event]:
        storeEvents: Dict[str, Event] = {}

        for eventKey, event in events.items():
            newEvent: Event = self.createEvent(event)
            storeEvents[eventKey] = newEvent

        return storeEvents

    def createEvent(self, eventDict: Dict) -> Event:
        eventBody: EventBody = self.createEventBody(eventDict.get('eventBody'))
        EventValidator.validateEventBodyHash(eventDict.get('bodySignature'), eventBody)

        event: Event = Event(eventBody)
        event.roundCreated = eventDict.get("roundCreated")
        event.isWitness = eventDict.get("isWitness")
        event.isFamous = eventDict.get("isFamous")
        event.isDecided = eventDict.get("isDecided")
        event.roundReceived = eventDict.get("roundReceived")
        event.consensusTimestamp = eventDict.get("consensusTimestamp")
        event.bodySignature = eventDict.get("bodySignature")

        for peerDeviceId, creatorIndex in eventDict.get('lastAncestors').items():
            event.addLastAncestor(peerDeviceId, creatorIndex)

        for peerDeviceId, creatorIndex in eventDict.get('firstDiscendants').items():
            event.addFirstDiscendant(peerDeviceId, creatorIndex)

        return event

    def createEventBody(self, eventBodyDict: Dict) -> EventBody:
        eventBody: EventBody = EventBody()
        eventBody.creatorAssociation = self.addEventPeerAssociation(eventBodyDict.get('creatorAssociation'))

        if 'selfParent' in eventBodyDict:
            eventBody.selfParent = self.addEventPeerAssociation(eventBodyDict.get('selfParent'))

        if 'otherParent' in eventBodyDict:
            eventBody.otherParent = self.addEventPeerAssociation(eventBodyDict.get('otherParent'))

        if 'selfParentHash' in eventBodyDict:
            eventBody.selfParentHash = eventBodyDict.get('selfParentHash')

        if 'otherParentHash' in eventBodyDict:
            eventBody.otherParentHash = eventBodyDict.get('otherParentHash')

        if 'transactions' in eventBodyDict:
            for transaction in eventBodyDict.get('transactions'):
                eventBody.transactions.append(self.addTransaction(transaction))

        eventBody.timestamp = eventBodyDict.get('timestamp')

        return eventBody

    def addEventPeerAssociation(self, eventPeerAssociationDict: Dict) -> EventPeerAssociation:
        return EventPeerAssociation(eventPeerAssociationDict.get('peerDeviceId'),
                                    eventPeerAssociationDict.get('eventCreatorIndex'))

    def addTransaction(self, transactionDict: Dict) -> Transaction:
        transaction: Transaction = Transaction(transactionDict.get('goalPeerDeviceId'))
        transaction.creationTime = transactionDict.get('creationTime')
        transaction.key = transactionDict.get('key')
        return transaction
