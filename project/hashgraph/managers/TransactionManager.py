from project.Logger.Logger import Logger, LogLevels
from project.hashgraph.interfaces.StoreCallback import StoreCallback
from project.hashgraph.models.Event import Event

class TransactionManager(StoreCallback):
    def eventStoredCallback(self, event: Event):

        # Check if event has transactions with robot commands
        if event.eventBody.transactions:
            Logger.createLog(LogLevels.DEBUG, __file__,
                             'New transactions found in event with creator association key: ' + str(
                                 event.eventBody.creatorAssociation.key))
            for transaction in event.eventBody.transactions:
                transaction.save()
                Logger.createLog(LogLevels.DEBUG, __file__, 'Stored transaction with key: ' + str(transaction.key))
