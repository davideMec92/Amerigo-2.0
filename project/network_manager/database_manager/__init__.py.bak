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
        TinyDB.DEFAULT_TABLE_KWARGS = {'cache_size': 0}

        if databaseName is not None:
            self.DB_DEFAULT_NAME = databaseName

        print('Initializing ' + str(self.DB_DEFAULT_NAME) + ' DB..')

        self.db = TinyDB(self.DB_DEFAULT_PATH + self.DB_DEFAULT_NAME)

    def getObject(self, queryAttribute, attributeValue):
        return self.db.search(where(queryAttribute) == attributeValue)

    def getAll(self):
        return self.db.all()

    def upsertObject(self, objectDict, primaryKey):
        self.db.upsert(self.updateTime(objectDict), Query()[primaryKey] == objectDict[primaryKey])

    def saveObject(self, objectDict):
        self.db.insert(self.updateTime(objectDict))

    def removeObject(self, objectDict, primaryKey):
        return self.db.remove(Query()[primaryKey] == objectDict[primaryKey])

    def updateTime(self, objectDict):
        objectDict['updatedTime'] = str(time.time())
        return objectDict
