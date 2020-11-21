from tinydb import TinyDB, Query, where

class DatabaseManager:

    #TODO INSTALL UNIQUE CONSTRAINT CHECKS TinyDB-CONSTRAINT

    #DB default settings
    DB_DEFAULT_PATH = './database_manager/'
    DB_DEFAULT_NAME = 'graph_db.json'

    db = None

    def __init__(self):
        print('Initializing DB..')
        self.db = TinyDB(self.DB_DEFAULT_PATH + self.DB_DEFAULT_NAME)

    def getObject(self, queryAttribute, attributeValue):
        return self.db.search(where(queryAttribute) == attributeValue)

    def upsertObject(self, objectDict):
        Peer = Query()
        self.db.upsert(objectDict, Peer.bluetooth_mac == objectDict['bluetooth_mac'])

    def saveObject(self, objectDict):
        self.db.insert(objectDict)

    def removeObject(self, objectDict):
        Peer = Query()
        return self.db.remove(Peer.id == objectDict['id'])
