from peer import Peer, PeerStatus
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
print('key : ' + str(key))

#peer = Peer('MACK22', '192.168.1.5', PeerStatus.CONNECTED)
#peer.save()
#print(str(peer.toDict()))
#database_manager = DatabaseManager()
#database_manager.saveObject(peer.toDict())
object = Peer.getFromBluetoothMac('MACK22')
print(object.toDict())
object.status = PeerStatus.WARNING
#object.upsert()
#object.remove()
"""result = database_manager.getObject('id', '9d768e22-8e0b-4247-8790-405b12d9dc7f')
peer = result[0]
print(str(peer))
frank = Peer.createFromDict(**peer)
print(str(frank.toDict()))
database_manager.removeObject(frank.toDict())"""

#peer['bluetooth_mac'] = 'MACK2'
#print(str(peer))
