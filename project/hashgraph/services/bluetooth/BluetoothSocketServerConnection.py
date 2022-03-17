from __future__ import annotations

import os
from typing import List
from uuid import UUID

import bluetooth

from project.Logger.Logger import Logger, LogLevels
from project.hashgraph.interfaces.Callbacks.CommunicationCallback import CommunicationCallback
from project.hashgraph.models.communication.BaseSocketServerConnection import BaseSocketServerConnection

from dotenv import load_dotenv

from project.hashgraph.services.bluetooth.BluetoothSocketConnection import BluetoothSocketConnection

load_dotenv()

class BluetoothSocketServerConnection(BaseSocketServerConnection):

    def __int__(self, connectionCallbacks: List[CommunicationCallback]) -> BluetoothSocketServerConnection:
        super().__int__(connectionCallbacks)

        if os.getenv('DEVICE_ID') is None:
            raise Exception('DEVICE_ID not found')

        if os.getenv('BLUETOOTH_SERVER_APP_NAME') is None:
            raise Exception('BLUETOOTH_SERVER_APP_NAME not found')

        self.serverAppUUID: UUID = os.getenv('DEVICE_ID');
        self.serverAppName: str = os.getenv('BLUETOOTH_SERVER_APP_NAME');
        self.connectionCallbacks: List[CommunicationCallback] = connectionCallbacks

        return self

    def run(self):
        self.isRunning = True

        try:

            Logger.createLog(LogLevels.DEBUG, __file__, "Starting listening for incoming connections..")

            self.serverSocket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.serverSocket.bind(("", bluetooth.PORT_ANY))
            self.serverSocket.listen(1)
            port = self.serverSocket.getsockname()[1]

            bluetooth.advertise_service(self.serverSocket, self.serverAppName,
                                        service_id=self.serverAppUUID,
                                        service_classes=[self.serverAppUUID, bluetooth.SERIAL_PORT_CLASS],
                                        profiles=[bluetooth.SERIAL_PORT_PROFILE],
                                        # protocols=[bluetooth.OBEX_UUID]
                                        )

            Logger.createLog(LogLevels.DEBUG, __file__, "Waiting for connection on RFCOMM channel on port: " + str(port))

            while self.isRunning is True:
                connectionSocket, address = self.serverSocket.accept()
                bluetoothSocketConnection: BluetoothSocketConnection = BluetoothSocketConnection.createFromBluetoothSocket(self.serverAppUUID, connectionSocket, address, self.connectionCallbacks, self)
                Logger.createLog(LogLevels.DEBUG, __file__, "Added incoming connection socket")
                self.incomingConnections[bluetoothSocketConnection.key] = bluetoothSocketConnection
                bluetoothSocketConnection.start()


        except Exception as e:
            Logger.createLog(LogLevels.ERROR, __file__, "Error while receiving data from server socket: " + str(e))


