from typing import Dict

from project.hashgraph.helpers.Hash import Hash
from project.hashgraph.services.bluetooth.BluetoothSocketConnection import BluetoothSocketConnection


class BluetoothConnectionStore:

    bluetoothConnections: Dict[str, BluetoothSocketConnection] = []

    def getConnection(self, remoteDeviceAddress: str) -> BluetoothSocketConnection:
        return self.bluetoothConnections[Hash.stringToHash(remoteDeviceAddress)] if self.bluetoothConnections[Hash.stringToHash(remoteDeviceAddress)] else None

    def deleteConnection(self, connectionKey: str):

        if self.bluetoothConnections[connectionKey] is not None:
            del self.bluetoothConnections[connectionKey]