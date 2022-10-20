from __future__ import annotations

from project.hashgraph.models.Transaction import Transaction

class TransactionManager:

    def getTransaction(self, lastTransactionKey: str = None) -> Transaction | None:
        if lastTransactionKey is not None:
            return Transaction.getFromKey(lastTransactionKey)
        else:
            return Transaction.getNextTransaction()