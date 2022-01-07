from __future__ import annotations
from random import random
from threading import Lock
from typing import List, Dict

from project.hashgraph.dictTypes import HashgraphPeerList
from project.hashgraph.dictTypes.HashgraphLastPeerCreatorIndex import HashgraphLastPeerCreatorIndex
from project.hashgraph.helpers.FifoQueue import FifoQueue
from project.hashgraph.helpers.ListHelper import ListHelper
from project.hashgraph.helpers.LockInitHelper import LockInitHelper
from project.hashgraph.interfaces.StoreCallback import StoreCallback
from project.hashgraph.managers.BlockManager import BlockManager
from project.hashgraph.models.Block import Block
from project.hashgraph.models.Event import Event
from project.hashgraph.models.Peer import Peer
from project.hashgraph.models.Round import Round
from project.hashgraph.models.Store import Store
from project.hashgraph.models.Transaction import Transaction
from project.hashgraph.models.VotesTable import VotesTable


class Hashgraph(StoreCallback):
    COIN_ROUND_FREQ = 10
    # TODO CHECK IF IT WORKS, IF IS NOT IN __init__ IT'S SHARED BETWEEN ALL INSTANCES OF THIS CLASS
    __instance: Hashgraph | None = None
    lock = Lock()

    def __init__(self, peers: List[Peer], myPeer: Peer) -> None:
        self.peers: Dict[str, Peer] = peers
        self.lastConsensusRound = -1
        self.lastDecidedRound = -1
        self.lastPeersCreatorIndex: HashgraphLastPeerCreatorIndex = {}
        self.myPeer: Peer = myPeer
        self.myPeerLastEvent: Event | None = None
        self.store: Store = Store(self)
        self.blockManager: BlockManager = BlockManager()
        self.blockManager.start()
        self.toSendTransactions: FifoQueue[Transaction] = []
        self.isHashgraphGossipLocked = None
        self.isHashgraphReceiveLocked = None

        # Init locks at first creation
        if self.isHashgraphReceiveLocked is None and self.isHashgraphGossipLocked is None:
            LockInitHelper.initHashgraphGossipLocks(self)

    # TODO CHECK IF INSTANCE IS RETURNED
    @staticmethod
    def getInstance(peers: HashgraphPeerList, myPeer: Peer) -> Hashgraph:
        if Hashgraph.__instance is None:
            Hashgraph.__instance = Hashgraph(peers, myPeer)
        return Hashgraph.__instance

    def getToSendTransaction(self, peekOnly: bool) -> Transaction | None:
        if peekOnly is True:
            return self.toSendTransactions.peek()
        else:
            return self.toSendTransactions.pop()

    # TODO TEST IF IS CORRECT
    def removeTransactionsToSendHead(self) -> None:
        self.toSendTransactions.remove()

    def lockHashgraphGossip(self) -> bool:
        try:
            self.lock.acquire()
            print('Try acquiring gossip lock..')
            if self.isHashgraphGossipLocked is True:
                print('False')
                return False
            else:
                self.isHashgraphGossipLocked = True
                print('True')
                return True
        finally:
            self.lock.release()

    def unlockHashgraphGossip(self) -> None:
        try:
            self.lock.acquire()
            if self.isHashgraphGossipLocked is True:
                print('Unlocked gossip lock')
                self.isHashgraphGossipLocked = False
        finally:
            self.lock.release()

    def lockHashgraphReceive(self) -> bool:
        try:
            self.lock.acquire()
            print('Try acquiring receive lock..')
            if self.isHashgraphReceiveLocked is True:
                print('False')
                return False
            else:
                self.isHashgraphReceiveLocked = True
                print('True')
                return True
        finally:
            self.lock.release()

    def unlockHashgraphReceive(self) -> None:
        try:
            self.lock.acquire()
            if self.isHashgraphReceiveLocked is True:
                print('Unlocked receive lock')
                self.isHashgraphReceiveLocked = False
        finally:
            self.lock.release()

    def updateEventIndexes(self, event: Event):
        self.lastPeersCreatorIndex[event.eventBody.getCreator()] = event.eventBody.getCreatorIndex()
        # Updating myPeer last event
        if event.eventBody.getCreator() == self.myPeer.deviceId:
            self.myPeerLastEvent = event

    def addUndeterminedEvents(self, event: Event):
        self.initLastAncestorsAndFirstDescendants(event)
        self.store.storeEvent(event)
        self.updateAncestorFirstDescendant(event)
        event.roundCreated = self.roundCreated(event)
        self.store.updateEvent(event)
        if event.isWitness is True:
            newRound: Round = Round.create(event, len(self.peers))
            self.store.rounds[newRound.roundCreated] = newRound
        else:
            self.store.addEventInRound(event)

        self.decideFame(event.roundCreated)
        self.decideRoundReceived()

    def createEvent(self, otherPeer: Peer, transactions: List[Transaction]) -> None:
        # TODO CHECK IF CAST TO INT NECESSARY FOR self.lastPeersCreatorIndex.get(otherPeer.deviceId)
        newEvent: Event = self.myPeer.createEvent(transactions, self.myPeerLastEvent, self.store.getEventFromPeerAndCreatorIndex(otherPeer.deviceId, self.lastPeersCreatorIndex.get(otherPeer.deviceId)))
        self.addUndeterminedEvents(newEvent)

    def getNewOtherUndeterminedEvents(self, otherHashgraphStore: Store) -> None:
        for deviceId, event in otherHashgraphStore.events:
            if event.roundCreated < self.lastConsensusRound - 1:
                continue

            if event.eventBody.creatorAssociation.peerDeviceId not in self.lastPeersCreatorIndex:
                # Adding all missing peer events
                self.store.storeMissingEvents(otherHashgraphStore, event.eventBody.creatorAssociation.peerDeviceId, 0)
            elif event.eventBody.creatorAssociation.eventCreatorIndex > self.lastPeersCreatorIndex.get(event.eventBody.creatorAssociation.peerDeviceId):
                # Adding missing peer events
                self.store.storeMissingEvents(otherHashgraphStore, event.eventBody.creatorAssociation.peerDeviceId, self.lastPeersCreatorIndex.get(event.eventBody.creatorAssociation.peerDeviceId) + 1)

        for event in self.store.lastMissingEvents:
            self.updateAncestorFirstDescendant(event)

        self.store.clearLastMissingEvents()

    def getNewOtherRounds(self, otherHashgraphStore: Store) -> None:
        for roundCreated, otherStoreRound in otherHashgraphStore.rounds:

            if otherStoreRound.roundCreated < self.lastConsensusRound - 1:
                continue

            # Try to get other peer event round's from our Store
            myStoreRound: Round = self.store.getRoundFromRoundCreated(roundCreated)

            if myStoreRound is None:
                # Saving other peer event round's
                self.store.putRound(myStoreRound)
            else:

                if otherStoreRound.roundReceived != myStoreRound.roundReceived and myStoreRound.roundReceived == -1:
                    myStoreRound.roundReceived = otherStoreRound.roundReceived

                if otherStoreRound.committed is True:
                    myStoreRound.committed = True

                myStoreRound.addEvents(ListHelper.getListDiff(myStoreRound.events, otherStoreRound.events))
                myStoreRound.addWitnesses(ListHelper.getListDiff(myStoreRound.witnesses, otherStoreRound.witnesses))

    def eventStoredCallback(self, event: Event):
        self.updateEventIndexes(event)

    def initLastAncestorsAndFirstDescendants(self, event: Event) -> None:
        if event.eventBody.selfParent is None and event.eventBody.otherParent is None:
            event.lastAncestors[event.eventBody.getCreator()] = event.eventBody.getCreatorIndex()
        else:
            selfParentEvent: Event = self.store.getEventFromEventPeerAssociationKey(event.eventBody.selfParent.key)
            event.copyLastAncestors(selfParentEvent.lastAncestors)
            otherParentEvent: Event = self.store.getEventFromEventPeerAssociationKey(event.eventBody.otherParent.key)

            for peerDeviceId, peer in self.peers.items():

                if peerDeviceId not in event.lastAncestors and peerDeviceId in otherParentEvent.lastAncestors:
                    event.lastAncestors[peerDeviceId] = otherParentEvent.lastAncestors.get(peerDeviceId)
                elif peerDeviceId in event.lastAncestors and peerDeviceId in otherParentEvent.lastAncestors:
                    if event.lastAncestors.get(peerDeviceId) < otherParentEvent.lastAncestors.get(peerDeviceId):
                        event.lastAncestors[peerDeviceId] = otherParentEvent.lastAncestors.get(peerDeviceId)

            event.lastAncestors[event.eventBody.getCreator()] = event.eventBody.getCreatorIndex()
            event.firstDiscendants[event.eventBody.getCreator()] = event.eventBody.getCreatorIndex()

    def updateAncestorFirstDescendant(self, event: Event):
        isWitness: bool = False

        for peerDeviceId, creatorIndex in event.lastAncestors.items():
            isWitness = False
            lastAncestorEvent: Event = self.store.getEventFromPeerAndCreatorIndex(peerDeviceId, creatorIndex)

            while isWitness is False:
                if lastAncestorEvent is None:
                    print('Last ancestor event not found!!!')
                    break

                lastAncestorEvent.firstDiscendants[event.eventBody.getCreator()] = event.eventBody.getCreatorIndex()
                isWitness = lastAncestorEvent.isWitness

                if isWitness is False:
                    lastAncestorEvent = self.store.getEventFromEventPeerAssociationKey(lastAncestorEvent.eventBody.selfParent.key)

    def roundCreated(self, event: Event):
        roundCreated: int = 0
        selfParentRoundCreated: int = 0

        if event.eventBody.selfParent is not None:
            selfParentRoundCreated = self.store.getEventFromEventPeerAssociationKey(event.eventBody.selfParent.key).roundCreated
            roundCreated = selfParentRoundCreated
        else:
            event.isWitness = True

        if event.eventBody.otherParent is not None:
            otherParentRound: int = self.store.getEventFromEventPeerAssociationKey(event.eventBody.otherParent.key).roundCreated
            if otherParentRound > roundCreated:
                roundCreated = otherParentRound

        """
        Now check if event strongly sees roundCreated witnesses
        """
        if event.isWitness is False:

            c: int = 0
            round: Round = self.store.getRoundFromRoundCreated(roundCreated)
            supermajority: float = (round.peersInRound*2)/3.00

            for roundWitness in round.witnesses:
                if self.stronglySee(event, self.store.getEventFromEventPeerAssociationKey(roundWitness)) is True:
                    c = c + 1

            if c >= supermajority:
                roundCreated = roundCreated + 1

        if roundCreated > selfParentRoundCreated:
            event.isWitness = True

        return roundCreated


    def see(self, x: Event, y: Event) -> bool:

        if x is None or y is None:
            return False

        if y.eventBody.getCreator() not in x.lastAncestors:
            return False

        return x.lastAncestors.get(y.eventBody.getCreator()) >= y.eventBody.getCreatorIndex()

    def stronglySee(self, x: Event, y: Event) -> bool:
        c: int = 0
        supermajority: float = (len(self.peers)*2)/3.00

        for peerDeviceId, peer in self.peers.items():
            try:
                if peerDeviceId in x.lastAncestors and peerDeviceId in y.firstDiscendants:
                    xLastAncestorCreatorIndex: int = x.lastAncestors.get(peerDeviceId)
                    yFirstDescendatCreatorIndex: int = y.firstDiscendants.get(peerDeviceId)

                    if xLastAncestorCreatorIndex >= yFirstDescendatCreatorIndex:
                        c = c + 1
            except Exception as e:
                print('Exception: ' + str(e))

        return c >= supermajority

    def setFame(self, event: Event, isFamous: bool):
        event.isFamous = isFamous
        event.isDecided = True
        self.store.updateEvent(event)

    def decideFame(self, lastRoundCreationIndex: int):
        votesTable: VotesTable = VotesTable()
        roundIndex: int = self.lastDecidedRound + 1

        round: Round = self.store.getRoundFromRoundCreated(roundIndex)

        # Loop each round not decided
        while round is not None:
            # Loop each witness not decided in round
            for notDecidedWitness in round.getNotDecidedWitnesses():
                # Loop each round after not decided round
                for i in range(roundIndex + 1, lastRoundCreationIndex + 1, 1):
                    nextRound: Round = self.store.getRoundFromRoundCreated(i)

                    # Loop each nextRound witness
                    for nextRoundWitness in nextRound.witnesses:
                        roundDistance: int = i - round.roundCreated

                        # First round of voting
                        if roundDistance == 1:
                            votesTable.setVote(nextRoundWitness, notDecidedWitness, self.see(self.store.getEventFromEventPeerAssociationKey(nextRoundWitness), self.store.getEventFromEventPeerAssociationKey(notDecidedWitness)))
                        else:
                            # Vote counting round
                            previousRound: Round = self.store.getRoundFromRoundCreated(i-1)
                            stronglySeenWitnesses: List[str] = []

                            # Loop each witness in previous round of next round
                            for previousRoundWitness in previousRound.witnesses:
                                # Check if next round witness strongly sees previous round witness
                                if self.stronglySee(self.store.getEventFromEventPeerAssociationKey(nextRoundWitness), self.store.getEventFromEventPeerAssociationKey(previousRoundWitness)) is True:
                                    stronglySeenWitnesses.append(previousRoundWitness)

                            yesses: int = 0
                            noes: int = 0

                            for stronglySeenWitness in stronglySeenWitnesses:
                                if votesTable.getVote(stronglySeenWitness, notDecidedWitness) is True:
                                    yesses = yesses + 1
                                else:
                                    noes = noes + 1

                            vote: bool = False
                            total: int = noes

                            if yesses >= noes:
                                vote = True
                                total = yesses

                            # Counting votes
                            if roundDistance % self.COIN_ROUND_FREQ > 0:

                                if total >= nextRound.getPeersInSetSupermajority():
                                    self.setFame(self.store.getEventFromEventPeerAssociationKey(notDecidedWitness), vote)

                                    # Add notDecidedRound to notDecidedRounds list in round
                                    round.addDecidedWitness(notDecidedWitness)

                                    votesTable.setVote(nextRoundWitness, notDecidedWitness, vote)

                                    # Break VOTE_LOOP
                                    i = lastRoundCreationIndex
                                else:
                                    votesTable.setVote(nextRoundWitness, nextRoundWitness, vote)
                            else:
                                # Coin Round
                                if total >= nextRound.getPeersInSetSupermajority():
                                    votesTable.setVote(nextRoundWitness, notDecidedWitness, vote)
                                else:
                                    # Random vote
                                    random_bit = random.getrandbits(1)
                                    votesTable.setVote(nextRoundWitness, notDecidedWitness, bool(random_bit))

            if round.isDecided() is True:
                self.lastDecidedRound = round.roundCreated

            roundIndex = roundIndex + 1

            round = self.store.getRoundFromRoundCreated(roundIndex)

    def decideRoundReceived(self):

        roundIndex: int = self.lastConsensusRound + 1

        round: Round = self.store.getRoundFromRoundCreated(roundIndex)
        lastDecidedRoundCreatedIndex: int = -1

        # Loop each round not decided
        while round is not None:
            for eventKey in ListHelper.getListDiff(round.determinedEvents, round.events):
                event: Event = self.store.getEventFromEventPeerAssociationKey(eventKey)
                nextRoundIndex: int = roundIndex + 1
                nextRoundEvent: Round = self.store.getRoundFromRoundCreated(nextRoundIndex)

                # Loop each round not decided
                while nextRoundEvent is not None:

                    # Check if all events in round are decided
                    if nextRoundEvent.isDecided() is False:
                        break

                    receivedWitnesses: List[str] = []
                    famousNextRoundWitnessCount: int = 0

                    for nextRoundWitnessEventKey in nextRoundEvent.witnesses:
                        nextRoundWitnessEvent: Event = self.store.getEventFromEventPeerAssociationKey(nextRoundWitnessEventKey)

                        if nextRoundWitnessEvent.isFamous is False:
                            continue

                        if self.see(nextRoundWitnessEvent, event) is True:
                            receivedWitnesses.append(nextRoundWitnessEventKey)

                        famousNextRoundWitnessCount = famousNextRoundWitnessCount + 1

                    if famousNextRoundWitnessCount == len(receivedWitnesses):
                        event.roundReceived = nextRoundIndex
                        nextRoundEvent.inRoundDeterminedEvents.append(eventKey)
                        round.determinedEvents.append(eventKey)

                        # Calculating consensus timestamp
                        receivedTimestamps: List[int] = []

                        for receivedWitness in receivedWitnesses:
                            receivedSelfParentEvent: event = self.store.getEventFromEventPeerAssociationKey(receivedWitness)
                            previousEvent: Event = receivedSelfParentEvent

                            while self.see(receivedSelfParentEvent, event) is True:
                                previousEvent = receivedSelfParentEvent

                                if receivedSelfParentEvent.eventBody.selfParent is not None:
                                    receivedSelfParentEvent = self.store.getEventFromEventPeerAssociationKey(receivedSelfParentEvent.eventBody.selfParent.key)
                                else:
                                    # Reached first event case
                                    break

                            receivedTimestamps.append(previousEvent.eventBody.timestamp)

                        consensusTimestamp: int = 0

                        for receivedTimestamp in receivedTimestamps:
                            consensusTimestamp = consensusTimestamp + receivedTimestamp

                        # TODO CHECK IF THIS IS CORRECT
                        consensusTimestamp = int(consensusTimestamp / len(receivedTimestamps))
                        event.consensusTimestamp = consensusTimestamp

                        if len(ListHelper.getListDiff(round.determinedEvents, round.events)) == 0:
                            self.lastConsensusRound = roundIndex
                            block: Block = Block(self.store, round)
                            self.blockManager.sendBlock(block)
                            round.committed = True
                            lastDecidedRoundCreatedIndex = roundIndex

                        break

                nextRoundIndex = nextRoundIndex + 1
                nextRoundEvent = self.store.getRoundFromRoundCreated(nextRoundIndex)

            roundIndex = roundIndex + 1
            round = self.store.getRoundFromRoundCreated(roundIndex)

