from tinydb import TinyDB, Query, where
import time
import datetime

class DatabaseManager:

    #TODO INSTALL UNIQUE CONSTRAINT CHECKS TinyDB-CONSTRAINT

    #DB default settings
    DB_DEFAULT_PATH = './database_manager/'
    DB_DEFAULT_NAME = 'graph_db.json'

    db = None

    def __init__(self, databaseName = None):
        print('Initializing DB..')
        self.db = TinyDB(self.DB_DEFAULT_PATH + databaseName if databaseName is not None else self.DB_DEFAULT_NAME)

    def getObject(self, queryAttribute, attributeValue):
        return self.db.search(where(queryAttribute) == attributeValue)

    def getAll(self):
        return self.db.all()

    def upsertObject(self, objectDict):
        Peer = Query()
        self.db.upsert(self.updateTime(objectDict), Peer.bluetooth_mac == objectDict['bluetooth_mac'])

    def saveObject(self, objectDict):
        self.db.insert(self.updateTime(objectDict))

    def removeObject(self, objectDict):
        Peer = Query()
        return self.db.remove(Peer.id == objectDict['id'])

    def updateTime(self, objectDict):
        objectDict['updatedTime'] = str(time.time())
        return objectDict
