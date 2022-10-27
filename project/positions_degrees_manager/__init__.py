import json
import os
from json import JSONDecodeError

from dotenv import load_dotenv

from project.bluetooth_client import BluetoothClient
from project.hashgraph.helpers.CommunicationMessageDecrypter import CommunicationMessageDecrypter
from project.hashgraph.models.communication.CommunicationMessageGetPositionDegrees import \
    CommunicationMessageGetPositionDegrees
from project.hashgraph.validators.communicationMessage.CommunicationMessageSchemaValidator import \
    CommunicationMessageSchemaValidator
from project.position_degrees import PositionDegrees

load_dotenv()

class PositionsDegreesManager:

    positionsDegrees = []

    def getPositionsDegrees(self):
        return self.positionsDegrees

    def getPositionDegreesDevicesIds(self):
        positionDegreesDevicesIds = []
        for positionDegreeDevice in self.positionsDegrees:
            positionDegreesDevicesIds.append(positionDegreeDevice.deviceId)
        return positionDegreesDevicesIds

    def getPositionsDegreesFromServer(self):

        if os.getenv('BluetoothServerUUID') is None:
            raise Exception('BluetoothServerUUID not found')

        if os.getenv('BluetoothServerBluetoothMAC') is None:
            raise Exception('BluetoothServerBluetoothMAC not found')

        bluetoothClientSocket = BluetoothClient(os.getenv('BluetoothServerBluetoothMAC'), os.getenv('BluetoothServerUUID'))

        message = bluetoothClientSocket.sendMessageWithResponse(CommunicationMessageGetPositionDegrees().encrypt())
        decryptedMessage = CommunicationMessageDecrypter.decrypt(message)

        if CommunicationMessageSchemaValidator.validate(decryptedMessage) is False:
            raise Exception('POSITIONS_DEGREES_GET_RESPONSE schema validation error')

        try:
            decryptedMessage = json.loads(CommunicationMessageDecrypter.decrypt(message))
        except JSONDecodeError as e:
            print('Cannot decode returned message to json')
            return False

        bluetoothClientSocket.stop()

        print('Message from server decrypted: ' + str(decryptedMessage))

        bluetoothClientSocket.close()
        self.clearPositionsDegrees()

        #Check if server has some positionDegrees
        if len(decryptedMessage['positionsDegrees']) == 0:
            return False

        for positionDegrees in decryptedMessage['positionsDegrees']:
            print('positionDegrees' + str(positionDegrees))
            tempPositionDegrees = PositionDegrees(positionDegrees)
            tempPositionDegrees.upsert()
            self.positionsDegrees.append(tempPositionDegrees)

        return True

    def clearPositionsDegrees(self):
        if len(self.positionsDegrees) > 0:
            self.positionsDegrees = []
