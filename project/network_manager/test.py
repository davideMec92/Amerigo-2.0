from peer import Peer, PeerStatus
from database_manager import DatabaseManager
from communication_message import CommunicationMessage, CommunicationMessageTypes
from peer_controller import PeerController
from block import Block
from position_degrees import PositionDegrees
from transaction import Transaction
import json
import re

token = 'gAAAAABg4essM5LN7pugT2ZOnh32CdKaoy1JpBlbJM_Hw67yBXmNL-GTkRNLWLOD-0B6Go1qTx7geNsAzrDw7rcqE4VAsbxguwt2x3fSg1dXqssuHZaaZwmxi8F0ybpVUL5iW7WS2FxxkRBEizsanR1MnGCZtzhaPyHOw8ud4LANKa_X9yLFQeP7I4WBU1CQVrtToAFEK2P8UFR6MFByVEAiP9zmlQlkKEcmZY13Sofr77_CGTuWNk4ERYQ_2R8tlU2MKOZY0NF0b-YmgN96OCMuv9Krt6PhXWQE2eszExa09_h_LWgMnYZBC9Tw4iCC-l-fIJ4i6jbT8zEyxMSCIUdeFcInmfK5sx8n7JlLHzxxLw1_kXHH-9sy7LOj3UY7xuqQxD0Zu94zEhN6cZJhnGk7wukkPgGsDXBjBkJTWxsNSk_kvfZdrEyPMABsSlF81BcpRsTrWvrSc6BX8SEEFCYPN-2d9Bboxf35ME4c1zaseZCwbAfeUGO-AlFFIY702_Wy8Xx2_6L6YFFoAoVrQUZhZGkqwhyBbLZ3-7b0JV1qhd5qFC04aZI4VEO4xeknQpg_-axJ_CDaiR53Eq-gT96-WlXB4gsTjbcfJlwpe1qAyIXuzSrWRYjlqqSlNajW-V6XLzuea4qpN3nLHk1kQrQaIpn2GKuiDGHrT7pcUS3R5HoJPY66zj8NNAzbi68IBN_jeTMKouOH1Ldf7WYLMXdMvv7yMaqOqa4QjP1Jqqjk6KgzZlQ9ANRxDvQzfQoszrB4sM701RXwBJSy3Iy2O6pXZ8BtxwuYtgHjOZvOeZh_zKi--SP5xm-xs3SRGvY5KhH4t2isua6FF7QpNl7RsMQX_6UEcJgdsJu1c6ZfqbXfdetZv051gpNaXtqfS0Wkr9oh_w6OsEoxQQ9NS2IUNjAz5CUnHpoTBOxJZQE7_2kyAlu4TGmeY1sTfKFw2qhqwn04d0Ovw2EIUm-Eg86YMcXCLNIyEFL8WnaQjphueoOq3NUPQYvd4IzFV8o7Jzl4P-pxcRad0smCDQsqYl6DHlQC7jCv0bXRtQ=='
print('MESSAGE: ' + str(CommunicationMessage().getMessage(token)))

"""peers_list = PeerController.getPeers(PeerStatus.CONNECTED)
#print(str(peers_list))
return_dict = {"type":CommunicationMessageTypes.PEERS_LIST.name, "peers": []}
for peer in peers_list:
    return_dict["peers"].append(peer)


print(str(return_dict))"""
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
