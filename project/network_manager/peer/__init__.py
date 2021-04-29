from aenum import Enum
from database_manager import DatabaseManager

class PeerStatus(Enum):
    CONNECTED = 0
    WARNING = 1
    DISCONNECTED = 2

class Peer:

    primaryKey = "deviceId"
    deviceId = None
    address = None
    status = PeerStatus(0)
    updatedTime = None

    DB_NAME = 'peers_db'

    database_manager = DatabaseManager(DB_NAME)

    def __init__(self, deviceId, address, peerStatus, updatedTime = None):

        if deviceId is None:
            raise Exception('deviceId cannot be null')

        if address is None:
            raise Exception('address cannot be null')

        if isinstance(peerStatus, PeerStatus) is False:
            raise Exception(peerStatus + ' is not a valid PeerStatus value')

        self.updatedTime = updatedTime
        self.deviceId = deviceId
        self.address = address
        self.status = peerStatus

    @staticmethod
    def createFromDict(status, updatedTime, address, deviceId):
        return Peer(deviceId, address, PeerStatus[status], updatedTime)

    @staticmethod
    def getFromDeviceId(deviceId):
        result = Peer.database_manager.getObject('deviceId', deviceId)
        if len(result) == 0:
            return None
        else:
            return Peer.createFromDict(**result[0])

    def save(self):
        self.database_manager.saveObject(self.toDict())

    def upsert(self):
        self.database_manager.upsertObject(self.toDict(), self.primaryKey)

    def remove(self):
        self.database_manager.removeObject(self.toDict(), self.primaryKey)

    def toDict(self):
        return {'deviceId':self.deviceId, 'address':self.address, 'status':self.status.name, 'updatedTime':self.updatedTime}
