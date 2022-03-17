from socket import socket
from threading import Thread
from typing import Dict, List

from project.Logger.Logger import Logger, LogLevels
from project.hashgraph.interfaces.Callbacks.CommunicationCallback import CommunicationCallback
from project.hashgraph.interfaces.Callbacks.ServerConnectionRemoveCallback import ServerConnectionRemoveCallback
from project.hashgraph.models.communication.BaseSocketConnection import BaseSocketConnection


class BaseSocketServerConnection(Thread, ServerConnectionRemoveCallback):

    def __int__(self, connectionCallbacks: List[CommunicationCallback]):
        self.isRunning = False
        self.connectionCallbacks: List[CommunicationCallback] = connectionCallbacks
        self.incomingConnections: Dict[str, BaseSocketConnection] = {}
        self.serverSocket: socket = None
        self.port: int = None
        Thread.__init__(self)

    def addConnectionCallback(self, connectionCallback: CommunicationCallback) -> None:
        self.connectionCallbacks.append(connectionCallback)

    def stopServer(self) -> None:
        Logger.createLog(LogLevels.DEBUG, __file__, 'Closing all incoming connections..')

        for socketConnectionId, socketConnection in self.incomingConnections.items():
            socketConnection.closeSocket()

        self.incomingConnections = {}
        self.serverSocket.close()
        self.isRunning = False

    def run(self):
        raise Exception("Implement server socket logic")

    def removeSocketConnection(self, connectionKey: str) -> None:
        super().removeSocketConnection(connectionKey)
        if connectionKey in self.incomingConnections:
            self.incomingConnections.pop(connectionKey)
            Logger.createLog(LogLevels.DEBUG, __file__, "Removed connection with key: " + str(connectionKey))


