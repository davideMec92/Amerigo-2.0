from database_manager import DatabaseManager

class Transaction:

    primaryKey = "key"
    key = None
    goalPeerDeviceId = None
    creationTime = None
    updatedTime = None

    DB_NAME = 'transactions_db'

    database_manager = DatabaseManager(DB_NAME)

    def __init__( self, dict ):
        self.key = dict["key"]
        self.goalPeerDeviceId = dict["goalPeerDeviceId"]
        self.creationTime = dict["creationTime"]
        if 'updatedTime' in dict:
            self.updatedTime = dict["updatedTime"]

    @staticmethod
    def getFromKey(key):
        result = Transaction.database_manager.getObject('key', key)
        if len(result) == 0:
            return None
        else:
            return Transaction(result[0])

    @staticmethod
    def getFirst():
        result = Transaction.database_manager.getAll()
        if len(result) == 0:
            return None
        else:
            first = None
            for transaction in result:
                if first is None:
                    first = transaction
                elif transaction["creationTime"] < first["creationTime"]:
                    first = transaction

            return Transaction(first) if first is not None else None

    def save(self):
        self.database_manager.saveObject(self.toDict())

    def upsert(self):
        self.database_manager.upsertObject(self.toDict(), self.primaryKey)

    def remove(self):
        self.database_manager.removeObject(self.toDict(), self.primaryKey)

    def toDict(self):
        return {'key':self.key, 'goalPeerDeviceId': self.goalPeerDeviceId, 'creationTime': self.creationTime, 'updatedTime': self.updatedTime}
