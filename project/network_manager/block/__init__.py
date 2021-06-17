from database_manager import DatabaseManager
from event import Event

class Block:

    primaryKey = "roundCreated"
    roundCreated = None
    events = []
    updatedTime = None

    DB_NAME = 'blocks_db'

    database_manager = DatabaseManager(DB_NAME)

    def __init__( self, dict ):
        self.roundCreated = dict["roundCreated"]
        self.events = []
        for eventData in dict["events"]:
            self.events.append(Event(eventData).toDict())

    @staticmethod
    def getFromRoundCreated(roundCreated):
        result = Block.database_manager.getObject('roundCreated', roundCreated)
        if len(result) == 0:
            return None
        else:
            return Block(result[0])

    def save(self):
        self.database_manager.saveObject(self.toDict())

    def upsert(self):
        self.database_manager.upsertObject(self.toDict(), self.primaryKey)

    def remove(self):
        self.database_manager.removeObject(self.toDict(), self.primaryKey)

    def toDict(self):
        return {'roundCreated':self.roundCreated, 'events': self.events, 'updatedTime': self.updatedTime}
