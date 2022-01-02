from typing import List

from project.hashgraph.models.Event import Event
from project.hashgraph.models.EventBlock import EventBlock
from project.hashgraph.models.Round import Round
from project.hashgraph.models.Store import Store
from project.hashgraph.models.Transaction import Transaction
from project.network_manager.block import Block


class Block:

    roundCreated: int = -1
    events: List[Event]
    store: Store
    eventRound: Round
    TAG = "Block"
    isBlockBuilt: bool = False
    isCommitted: bool = False

    def __init__(self, store: Store, eventRound: Round):
        self.store = store
        self.eventRound = eventRound
        self.roundCreated = self.eventRound.roundCreated

    def build(self) -> Block:

        if self.isBlockBuilt is True:
            return self

        for determinedEventKey in self.eventRound.determinedEvents:
            determinedEvent = self.store.getEventFromEventPeerAssociationKey(determinedEventKey)

            if determinedEvent is None:
                continue

            eventBlock = EventBlock()
            eventBlock.consensusTimestamp = determinedEvent.consensusTimestamp

            # Check if list is not empty
            if determinedEvent.eventBody.transactions:
                for transaction in determinedEvent.eventBody.transactions:
                    newTransaction: Transaction = Transaction(transaction.goalPeerDeviceId)
                    newTransaction.creationTime = determinedEvent.consensusTimestamp
                    newTransaction.setKey()
                    eventBlock.transactions.append(newTransaction)

            eventBlock.creatorAssociation = determinedEvent.eventBody.creatorAssociation
            self.events.append(eventBlock)

        self.isBlockBuilt = True
        return self
