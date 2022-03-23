from typing import Dict

from project.hashgraph.helpers.Hash import Hash
from project.hashgraph.services.bluetooth.BluetoothSocketConnection import BluetoothSocketConnection


class BluetoothConnectionStore:

    bluetoothConnections: Dict[str, BluetoothSocketConnection] = {}

    def getConnection(self, remoteDeviceAddress: str) -> BluetoothSocketConnection:
        connectionKey: str = Hash.stringToHash(remoteDeviceAddress)
        return self.bluetoothConnections.get(connectionKey) if connectionKey in self.bluetoothConnections else None

    def deleteConnection(self, connectionKey: str):
        if self.bluetoothConnections[connectionKey] is not None:
            del self.bluetoothConnections[connectionKey]