from position_degrees import PositionDegrees
from bluetooth_client import BluetoothClient
from communication_message import CommunicationMessage, CommunicationMessageTypes
from bluetooth_settings import BluetoothSettings

class TransactionManager():
    def getTransaction(self, lastTransactionKey = None):
        print('serverBluetoothMAC: ' + str(BluetoothSettings.serverBluetoothMAC))
        print('serverAppUUID: ' + str(BluetoothSettings.serverAppUUID))
        bluetoothClientSocket = BluetoothClient(BluetoothSettings.serverBluetoothMAC, BluetoothSettings.serverAppUUID)
        transactionGetCommunicationMessage = {
            'type': CommunicationMessageTypes.TRANSACTION_GET.name,
            'authToken': BluetoothSettings.serverAuthToken
        }

        if lastTransactionKey is not None:
            transactionGetCommunicationMessage['lastTransactionKey'] = lastTransactionKey

        communication_message = CommunicationMessage()
        message = bluetoothClientSocket.sendMessageWithResponse(communication_message.setMessage(transactionGetCommunicationMessage, True))
        transaction = communication_message.getMessage(message)
        print('Message from server decrypted: ' + str(transaction))
        bluetoothClientSocket.close()

        if 'key' not in transaction and 'goalPeerDeviceId' not in transaction:
            return None

        return transaction