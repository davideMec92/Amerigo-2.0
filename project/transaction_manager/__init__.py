from position_degrees import PositionDegrees
from bluetooth_client import BluetoothClient
from communication_message import CommunicationMessage, CommunicationMessageTypes
from bluetooth_settings import BluetoothSettings

class TransactionManager():
    def getTransaction(self, lastTransaction = None):
        bluetoothClientSocket = BluetoothClient(BluetoothSettings.serverBluetoothMAC, BluetoothSettings.serverAppUUID)
        transactionGetCommunicationMessage = {
            'type': CommunicationMessageTypes.TRANSACTION_GET.name,
            'authToken': BluetoothSettings.serverAuthToken
        }

        if lastTransaction is not None:
            transactionGetCommunicationMessage['lastTransactionKey'] = lastTransaction

        communication_message = CommunicationMessage()
        message = bluetoothClientSocket.sendMessageWithResponse(communication_message.setMessage(transactionGetCommunicationMessage, True))
        decryptedMessage = communication_message.getMessage(message)
        print('Message from server decrypted: ' + str(decryptedMessage))

        return True