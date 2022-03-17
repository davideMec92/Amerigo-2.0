from __future__ import annotations

import os
from socket import socket
from typing import List
from uuid import UUID

import bluetooth
from dotenv import load_dotenv

from project.Logger.Logger import Logger, LogLevels
from project.hashgraph.interfaces.Callbacks.CommunicationCallback import CommunicationCallback
from project.hashgraph.interfaces.Callbacks.ServerConnectionRemoveCallback import ServerConnectionRemoveCallback
from project.hashgraph.models.Hashgraph import Hashgraph
from project.hashgraph.models.communication.BaseSocketConnection import BaseSocketConnection

load_dotenv()

class BluetoothSocketConnection(BaseSocketConnection):

    def __int__(self) -> BluetoothSocketConnection:
        BaseSocketConnection.__int__(self)
        self.appUUID: UUID = None
        return self

    def initReceiveStatus(self) -> None:
        if self.clientAddress == os.getenv('BluetoothServerBluetoothMAC') or (
                self.clientAddress != os.getenv(
            'BluetoothServerBluetoothMAC') and Hashgraph.instance is not None and Hashgraph.instance.isHashgraphReceiveLocked is False):
            self.isReceiveAvailable = True

    @staticmethod
    def createFromBluetoothSocket(appUUID: UUID, bluetoothSocket: socket, clientAddress: str, bluetoothConnectionCallbacks: List[CommunicationCallback], serverConnectionRemoveCallback: ServerConnectionRemoveCallback) -> BluetoothSocketConnection:
        bluetoothSocketConnection: BluetoothSocketConnection = BluetoothSocketConnection().__int__()
        bluetoothSocketConnection.appUUID: UUID = appUUID
        bluetoothSocketConnection.socket = bluetoothSocket
        bluetoothSocketConnection.serverConnectionRemoveCallback = serverConnectionRemoveCallback
        bluetoothSocketConnection.clientAddress: str = clientAddress
        bluetoothSocketConnection.isReceiveAvailable: bool = None
        bluetoothSocketConnection.initReceiveStatus()

        Logger.createLog(LogLevels.DEBUG, __file__, "Client mac address: " + str(bluetoothSocketConnection.clientAddress))

        bluetoothSocketConnection.connectionCallbacks = bluetoothConnectionCallbacks
        bluetoothSocketConnection.initSocket()
        return bluetoothSocketConnection

    @staticmethod
    def createFromUUIDAndMACAddress(appUUID: UUID, clientAddress: str, bluetoothConnectionCallbacks: List[CommunicationCallback], serverConnectionRemoveCallback: ServerConnectionRemoveCallback) -> BluetoothSocketConnection:

        bluetoothSocketConnection: BluetoothSocketConnection = BluetoothSocketConnection().__int__()
        bluetoothSocketConnection.appUUID = appUUID
        bluetoothSocketConnection.clientAddress = clientAddress
        bluetoothSocketConnection.serverConnectionRemoveCallback = serverConnectionRemoveCallback
        bluetoothSocketConnection.connectionCallbacks = bluetoothConnectionCallbacks

        try:
            service_matches = bluetooth.find_service(uuid=bluetoothSocketConnection.appUUID, address=bluetoothSocketConnection.clientAddress)

            if len(service_matches) == 0:
                raise Exception("Couldn't find the specified server service.")

            first_match = service_matches[0]
            port = first_match["port"]
            name = first_match["name"]
            host = first_match["host"]

            print(("Connecting to \"{}\" on {}".format(name, host)))

            # Create the client socket
            bluetoothSocketConnection.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            bluetoothSocketConnection.socket.connect((host, port))
            bluetoothSocketConnection.initReceiveStatus()
            bluetoothSocketConnection.initSocket()

            return bluetoothSocketConnection
        except Exception as e:
            Logger.createLog(LogLevels.ERROR, __file__, "Cannot initialize bluetooth client socket: " + str(e))
            return None