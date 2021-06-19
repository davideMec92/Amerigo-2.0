from database_manager import DatabaseManager
from peer_position import PeerPosition

class PositionDegrees:
    primaryKey = "deviceId"
    deviceId = None
    positions = []
    updatedTime = None

    DB_NAME = 'position_degrees'

    database_manager = DatabaseManager(DB_NAME)

    def __init__(self, deviceId, positions, updatedTime = None):

        if deviceId is None:
            raise Exception('deviceId cannot be null')

        if positions is None:
            raise Exception('positions cannot be null')

        self.updatedTime = updatedTime
        self.deviceId = deviceId
        self.positions = []

        for peerPositionData in positions:
            self.positions.append(PeerPosition(peerPositionData).toDict())

    @staticmethod
    def createFromDict(status, updatedTime, address, deviceId):
        return Peer(deviceId, address, PeerStatus[status], updatedTime)

    @staticmethod
    def getFromDeviceId(deviceId):
        result = PositionDegrees.database_manager.getObject('deviceId', deviceId)
        if len(result) == 0:
            return None
        else:
            return PositionDegrees.createFromDict(**result[0])

    def save(self):
        self.database_manager.saveObject(self.toDict())

    def upsert(self):
        self.database_manager.upsertObject(self.toDict(), self.primaryKey)

    def remove(self):
        self.database_manager.removeObject(self.toDict(), self.primaryKey)

    def toDict(self):
        return {'deviceId': self.deviceId, 'positions': self.positions,'updatedTime': self.updatedTime}
