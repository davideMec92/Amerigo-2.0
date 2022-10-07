import json
from typing import Dict

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
        self.creationTime: int = 0

    def setKey(self):
        self.key = Hash.stringToHash(self.goalPeerDeviceId + str(self.creationTime))

    def setCreationTimeAtNow(self):
        self.creationTime = DatetimeHelper.getNowTimestamp()

    def toDict(self) -> Dict:
        return {
            'creationTime': self.creationTime,
            'goalPeerDeviceId': self.goalPeerDeviceId,
            'key': self.key
        }

    def toJson(self) -> str:
        return json.dumps(self.toDict(), allow_nan=False, sort_keys=True, separators=(',',':'))

    def toPrettyJson(self) -> str:
        return json.dumps(self.toDict(), allow_nan=False, sort_keys=True, indent=4)


