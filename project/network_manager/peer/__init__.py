from aenum import Enum
from database_manager import DatabaseManager
import uuid

class PeerStatus(Enum):
    CONNECTED = 0
    WARNING = 1
    DISCONNECTED = 2

class Peer:

    #DB default settings
    id = None
    bluetooth_mac = None
    ip_address = None
    status = PeerStatus(0)
    updatedTime = None

    database_manager = DatabaseManager()

    def __init__(self, bluetooth_mac, ip_address, peerStatus, updatedTime = None, id = None):

        type(peerStatus)
        if bluetooth_mac is None:
            raise Exception('bluetooth_mac cannot be null')

        if ip_address is None:
            raise Exception('ip_address cannot be null')

        if isinstance(peerStatus, PeerStatus) is False:
            raise Exception(peerStatus + ' is not a valid PeerStatus value')

        #TODO VALIDATE FIELDS IP AND MAC WITH REGEX

        if id is None:
            self.id = str(uuid.uuid4())
        else:
            self.id = id

        self.updatedTime = updatedTime
        self.bluetooth_mac = bluetooth_mac
        self.ip_address = ip_address
        self.status = peerStatus

    @staticmethod
    def createFromDict(status, updatedTime, ip_address, bluetooth_mac, id):
        return Peer(bluetooth_mac, ip_address, PeerStatus[status], updatedTime, id)

    @staticmethod
    def get(peerId):
        result = Peer.database_manager.getObject('id', peerId)
        if len(result) == 0:
            return None
        else:
            return Peer.createFromDict(**result[0])

    @staticmethod
    def getFromBluetoothMac(bluetoothMac):
        result = Peer.database_manager.getObject('bluetooth_mac', bluetoothMac)
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
        return {'id':self.id, 'bluetooth_mac':self.bluetooth_mac, 'ip_address':self.ip_address, 'status':self.status.name, 'updatedTime':self.updatedTime}
