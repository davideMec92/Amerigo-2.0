from __future__ import annotations

import json
from typing import Dict

from project.hashgraph.enums.TransactionStatus import TransactionStatus
from project.hashgraph.helpers.Hash import Hash
from project.hashgraph.helpers.DatetimeHelper import DatetimeHelper
from project.hashgraph.services.database.TinyDB.TinyDBModel import TinyDBModel
from project.hashgraph.services.database.TinyDB.TinyDBService import TinyDBService

class Transaction(TinyDBModel):
    primaryKey = "key"
    DB_NAME = 'transactions'

    tinyDBService: TinyDBService = TinyDBService(DB_NAME)

    def __init__(self, goalPeerDeviceId: str):
        super().__init__(Transaction.tinyDBService, Transaction.primaryKey)
        self.key: str = None
        self.goalPeerDeviceId: str = goalPeerDeviceId
        self.creationTime: int = DatetimeHelper.getNowTimestamp()
        self.status: TransactionStatus = TransactionStatus.READY
        self.executedAt: int = 0
        # Set key automatically
        self.setKey()

    def setKey(self):
        self.key = Hash.stringToHash(self.goalPeerDeviceId + str(self.creationTime))

    def setCreationTimeAtNow(self) -> int:
        self.creationTime = DatetimeHelper.getNowTimestamp()

    def setExecutedAtNow(self) -> int:
        self.executedAt = DatetimeHelper.getNowTimestamp()

    def toDict(self) -> Dict:
        return {
            'creationTime': self.creationTime,
            'goalPeerDeviceId': self.goalPeerDeviceId,
            'key': self.key,
            'status': self.status,
            'executedAt': self.executedAt,
            'updatedTime': self.updatedTime
        }

    def toJson(self) -> str:
        return json.dumps(self.toDict(), allow_nan=False, sort_keys=True, separators=(',',':'))

    def toPrettyJson(self) -> str:
        return json.dumps(self.toDict(), allow_nan=False, sort_keys=True, indent=4)

    @staticmethod
    def getFromKey(key: str) -> Transaction | None:
        tinyDBModel = TinyDBModel(Transaction.tinyDBService, Transaction.primaryKey)
        return tinyDBModel.getFromPrimaryKey(key)

    @staticmethod
    def getNextTransaction() -> Transaction | None:
        tinyDBModel = TinyDBModel(Transaction.tinyDBService, Transaction.primaryKey)
        result = tinyDBModel.db.search(tinyDBModel.modelQuery['status'] == TransactionStatus.READY.name)
        return None if not result else tinyDBModel.createFromDict(sorted( result, key=lambda d: d['creationTime'])[0])


