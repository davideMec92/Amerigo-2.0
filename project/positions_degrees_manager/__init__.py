from position_degrees import PositionDegrees
from bluetooth_client import BluetoothClient
from communication_message import CommunicationMessage, CommunicationMessageTypes
from bluetooth_settings import BluetoothSettings

class PositionsDegreesManager():
    positionsDegrees = []

    def getPositionsDegrees(self):
        return self.positionsDegrees

    def getPositionDegreesDevicesIds(self):
        positionDegreesDevicesIds = []
        for positionDegreeDevice in self.positionsDegrees:
            positionDegreesDevicesIds.append(positionDegreeDevice.deviceId)
        return positionDegreesDevicesIds

    def getPositionsDegrees(self):
        bluetoothClientSocket = BluetoothClient(BluetoothSettings.serverBluetoothMAC, BluetoothSettings.serverAppUUID)
        positionDegreesGetCommunicationMessage = {
            'type': CommunicationMessageTypes.POSITIONS_DEGREES_GET.name,
            'authToken': BluetoothSettings.serverAuthToken
        }
        communication_message = CommunicationMessage()
        message = bluetoothClientSocket.sendMessageWithResponse(communication_message.setMessage(positionDegreesGetCommunicationMessage, True))
        decryptedMessage = communication_message.getMessage(message)
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