from aenum import Enum
from database_manager import DatabaseManager

class PeerStatus(Enum):
    CONNECTED = 0
    WARNING = 1
    DISCONNECTED = 2

class Peer:

    deviceId = None
    ipAddress = None
    status = PeerStatus(0)
    updatedTime = None

    DB_NAME = 'peers_db'

    database_manager = DatabaseManager(DB_NAME)

    def __init__(self, deviceId, ipAddress, peerStatus, updatedTime = None):

        if deviceId is None:
            raise Exception('deviceId cannot be null')

        if ipAddress is None:
            raise Exception('ipAddress cannot be null')

        if isinstance(peerStatus, PeerStatus) is False:
            raise Exception(peerStatus + ' is not a valid PeerStatus value')

        self.updatedTime = updatedTime
        self.deviceId = deviceId
        self.ipAddress = ipAddress
        self.status = peerStatus

    @staticmethod
    def createFromDict(status, updatedTime, ipAddress, deviceId):
        return Peer(deviceId, ipAddress, PeerStatus[status], updatedTime)

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
        self.database_manager.upsertObject(self.toDict())

    def remove(self):
        self.database_manager.removeObject(self.toDict())

    def toDict(self):
        return {'deviceId':self.deviceId, 'ipAddress':self.ipAddress, 'status':self.status.name, 'updatedTime':self.updatedTime}
