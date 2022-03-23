from __future__ import annotations

from project.Logger.Logger import Logger, LogLevels
from project.hashgraph.handlers.Communication.IncomingCommunicationMessageHandler import \
    IncomingCommunicationMessageHandler
from project.hashgraph.helpers.FifoQueue import FifoQueue
from project.hashgraph.interfaces.Callbacks.CommunicationCallback import CommunicationCallback
from project.hashgraph.interfaces.Callbacks.ServerConnectionRemoveCallback import ServerConnectionRemoveCallback
from project.hashgraph.managers.services.BluetoothConnectionStore import BluetoothConnectionStore
from project.hashgraph.services.bluetooth.BluetoothSocketConnection import BluetoothSocketConnection
from project.hashgraph.services.bluetooth.BluetoothSocketServerConnection import BluetoothSocketServerConnection


class BluetoothConnectionManager(ServerConnectionRemoveCallback):

    instance: BluetoothConnectionManager = None

    def __init__(self) -> None:
        self.bluetoothConnectionStore: BluetoothConnectionStore = BluetoothConnectionStore()
        self.incomingCommunicationMessageHandler: IncomingCommunicationMessageHandler = IncomingCommunicationMessageHandler()
        self.defaultConnectionCallbacks: FifoQueue[CommunicationCallback] = FifoQueue[CommunicationCallback]()
        self.defaultConnectionCallbacks.push(self.incomingCommunicationMessageHandler)
        self.bluetoothSocketServerConnection: BluetoothSocketServerConnection = BluetoothSocketServerConnection(self.defaultConnectionCallbacks)
        self.bluetoothSocketServerConnection.start()

    @staticmethod
    def getInstance() -> BluetoothConnectionManager:

        if BluetoothConnectionManager.instance is None:
            BluetoothConnectionManager.instance = BluetoothConnectionManager()

        return BluetoothConnectionManager.instance

    def getBluetoothSocketServerConnection(self) -> BluetoothSocketServerConnection:
        return self.bluetoothSocketServerConnection

    def getBluetoothConnectionStore(self) -> BluetoothConnectionStore:
        return self.bluetoothConnectionStore

    def addDefaultConnectionCallback(self, communicationCallback: CommunicationCallback) -> None:
        self.defaultConnectionCallbacks.push(communicationCallback)

    def addCallbackToBluetoothSocketServerConnection(self, communicationCallback: CommunicationCallback) -> None:
        self.bluetoothSocketServerConnection.addConnectionCallback(communicationCallback)

    def removeSocketConnection(self, connectionKey: str) -> None:
        self.bluetoothConnectionStore.deleteConnection(connectionKey)

    def storeBluetoothSocketConnection(self, bluetoothSocketConnection: BluetoothSocketConnection, startConnection: bool) -> None:
        self.bluetoothConnectionStore.bluetoothConnections[bluetoothSocketConnection.key, bluetoothSocketConnection]

        if startConnection is True:
            bluetoothSocketConnection.start()

    def newBluetoothSocketConnection(self, appUUID: str, remoteDeviceAddress, str, startConnection: bool) -> BluetoothSocketConnection:

        try:
            # Check if connection already exists
            if self.bluetoothConnectionStore.getConnection(remoteDeviceAddress) is not None:
                self.bluetoothConnectionStore.getConnection(remoteDeviceAddress).closeSocket()

            bluetoothSocketConnection: BluetoothSocketConnection = BluetoothSocketConnection.createFromUUIDAndMACAddress(appUUID, remoteDeviceAddress, self.defaultConnectionCallbacks, self)
            self.storeBluetoothSocketConnection(bluetoothSocketConnection, startConnection)
            return bluetoothSocketConnection
        except Exception as e:
            Logger.createLog(LogLevels.ERROR, __file__, 'Error while starting a new bluetooth socket connection: ' + str(e))
            return None
