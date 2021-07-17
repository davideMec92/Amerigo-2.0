from position_degrees import PositionDegrees
from bluetooth_client import BluetoothClient
from communication_message import CommunicationMessage, CommunicationMessageTypes

class PositionsDegreesManager:

    serverAppUUID = '94f39d29-7d6d-437d-973b-fba39e49d4ee'
    serverBluetoothMAC = 'DC:A6:32:A4:B2:C3'
    serverAuthToken = 'Hs8GckGahlvzOTZBMpMLTa2gjMjEnRDf'

    def getPositionsDegrees(self):
        bluetoothClientSocket = BluetoothClient(self.serverBluetoothMAC, self.serverAppUUID)
        positionDegreesGetCommunicationMessage = {
            'type': CommunicationMessageTypes.POSITIONS_DEGREES_GET.name,
            'authToken': self.serverAuthToken
        }
        communication_message = CommunicationMessage()
        message = bluetoothClientSocket.sendMessageWithResponse(communication_message.setMessage(positionDegreesGetCommunicationMessage, True))
        decryptedMessage = communication_message.getMessage(message)
        print('Message from server decrypted: ' + str(decryptedMessage))

        for positionDegrees in decryptedMessage['positionsDegrees']:
            print('positionDegrees' + str(positionDegrees))
            PositionDegrees(positionDegrees).upsert()

        return decryptedMessage['positionsDegrees']