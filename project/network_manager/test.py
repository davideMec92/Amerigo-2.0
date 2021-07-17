from peer import Peer, PeerStatus
from database_manager import DatabaseManager
from communication_message import CommunicationMessage, CommunicationMessageTypes
from peer_controller import PeerController
from block import Block
from position_degrees import PositionDegrees
from position_degrees_controller import PositionDegreesController
from responses import PositionsDegreesGetResponse
from transaction import Transaction
import json
import re
from block_queue import BlockQueue

positionsDegrees = PositionDegreesController.getPositionsDegrees()
print('positions degrees GET ALL: ' + str(PositionsDegreesGetResponse().build(positionsDegrees)))


"""positionDegrees = {
        'type': 'POSITIONS_DEGREES',
        'deviceId': 'DEVICE_ID_TEST_1',
        'positions': [
            {
                "deviceId": 'DEVICE_ID_TEST_2',
                "degrees": 186,
            }
        ]
    }

PositionDegrees(positionDegrees['deviceId'], positionDegrees['positions']).save()"""

"""blockQueue = BlockQueue()
blockQueue.start()
blockZeroDict = {'events': [{'consensusTimestamp': 1626381938, 'creatorAssociation': {'eventCreatorIndex': 2, 'key': '5400cf1fa28a4407338e84a8beb618f1084be964a345db74aaa453551740a443', 'peerDeviceId': '8756bf0c-0307-4da4-ab73-354e80d299f0'}, 'transactions': [{'creationTime': 1626381938, 'goalPeerDeviceId': '8756bf0c-0307-4da4-ab73-354e80d299f0', 'key': 'fe44c7b3378640ab993b8be1911e36d58e229fada4ee2dd1dfb3252ae9e7f9c3'}]}, {'consensusTimestamp': 1626381939, 'creatorAssociation': {'eventCreatorIndex': 3, 'key': '1187a87de1ab898dc7ac1565bc5ce7b053b4b6f82ed621c1866933411111c9ac', 'peerDeviceId': 'd2291975-ea30-46e6-b555-42578bcef41b'}, 'transactions': []}], 'roundCreated': 2}
blockQueue.putBlock(blockZeroDict)"""


"""print(str(return_dict))"""
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
"""object = Peer.getFromDeviceId("MACK22")
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
