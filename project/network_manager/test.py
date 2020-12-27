from peer import Peer, PeerStatus
from database_manager import DatabaseManager
from communication_message import CommunicationMessage, CommunicationMessageTypes
from peer_controller import PeerController
import json


peers_list = PeerController.getPeers(PeerStatus.CONNECTED)
#print(str(peers_list))
return_dict = {"type":CommunicationMessageTypes.PEERS_LIST.name, "peers": []}
for peer in peers_list:
    return_dict["peers"].append(peer)


print(str(return_dict))
"""communication_message = CommunicationMessage()
deserialized_message = {"type":"LOGIN","authToken":"Hs8GckGahlvzOTZBMpMLTa2gjMjEnRDf","macAddress":"macAddress_1"}
encrypt_token = communication_message.setMessage(deserialized_message)
print(communication_message.setMessage(deserialized_message))

print(communication_message.getMessage(encrypt_token))"""

#print 'PEERS_LIST: ' + str(peers_list)
"""deserialized_message = {"type":"LOGIN","authToken":"Hs8GckGahlvzOTZBMpMLTa2gjMjEnRDf","macAddress":"macAddress_1"}
test = CommunicationMessage.check(CommunicationMessage.LOGIN_CONF_SCHEMA, deserialized_message)
print type(deserialized_message)
print(test)"""
#peer = Peer("MACK22", "192.168.1.5", PeerStatus.CONNECTED)
#peer.save()

#print("get all: " + str(peer.database_manager.getAll()))
#print(str(peer.toDict()))
#database_manager = DatabaseManager()
#database_manager.saveObject(peer.toDict())
"""object = Peer.getFromBluetoothMac("MACK22")
print(object.toDict())
object.status = PeerStatus.WARNING"""
#object.upsert()
#object.remove()
"""result = database_manager.getObject("id", "9d768e22-8e0b-4247-8790-405b12d9dc7f")
peer = result[0]
print(str(peer))
frank = Peer.createFromDict(**peer)
print(str(frank.toDict()))
database_manager.removeObject(frank.toDict())"""

#peer["bluetooth_mac"] = "MACK2"
#print(str(peer))
