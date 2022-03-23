from threading import Lock
from typing import List

from project.Logger.Logger import Logger, LogLevels
from project.hashgraph.interfaces.Strategies.ServerMessageHandlerStrategy import ServerMessageHandlerStrategy
from project.hashgraph.models.GossipProtocol import GossipProtocol
from project.hashgraph.models.Hashgraph import Hashgraph
from project.hashgraph.models.Store import Store
from project.hashgraph.models.Transaction import Transaction
from project.hashgraph.models.communication.CommunicationMessageHashgraph import CommunicationMessageHashgraph


class HandleHashgraphStoreMessage(ServerMessageHandlerStrategy):

    lock = Lock()

    def __init__(self):
        self.hashgraph: Hashgraph = Hashgraph.instance
        self.transactions: List[Transaction] = []

    def handleMessage(self, message: CommunicationMessageHashgraph) -> None:

        if self.hashgraph is None:
            Logger.createLog(LogLevels.DEBUG, __file__, 'Peer list not initialized, hashgraph null')
            print('Peer list not initialized, hashgraph null')
            return

        isErrorHappend: bool = False
        transactionToSendFound: bool = False

        try:
            Logger.createLog(LogLevels.DEBUG, __file__, 'Getting actual peer hashgraph..')
            otherHashgraphStore: Store = message.store

            if self.hashgraph.getToSendTransaction(True) is not None:
                self.transactions.append(self.hashgraph.getToSendTransaction(True))
                transactionToSendFound = True

            self.hashgraph.getNewOtherRounds(otherHashgraphStore)
            self.hashgraph.getNewOtherUndeterminedEvents(otherHashgraphStore)
            self.hashgraph.createEvent(message.peer, self.transactions)

        except Exception as e:
            print('HandleHashgraphStoreMessage exception: ' + str(e))
            isErrorHappend = True
        finally:

            if isErrorHappend is False and transactionToSendFound is True:
                self.hashgraph.removeTransactionsToSendHead()

            HandleHashgraphStoreMessage.lock.acquire()
            Logger.createLog(LogLevels.DEBUG, __file__, 'Try to unlock hashgraph gossip lock..')
            self.hashgraph.unlockHashgraphGossip()
            if GossipProtocol.instance.unlockGossipProtocolEvent.is_set() is False:
                GossipProtocol.instance.unlockGossipProtocolEvent.set()
                Logger.createLog(LogLevels.DEBUG, __file__, 'unlockGossipProtocolEvent unlocked')
            HandleHashgraphStoreMessage.lock.release()





