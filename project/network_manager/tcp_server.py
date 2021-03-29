
from communication_manager import CommunicationManager
from enum import Enum
from bluetooth_connection import BluetoothConnection
from tcp_connection import TCPConnection

class ConnectionMode(Enum):
    TCP_CONNECTION = 'TCP_CONNECTION'
    BLUETOOTH_CONNECTION = 'BLUETOOTH_CONNECTION'

class TcpServer():

    socket = None
    socketRun = False
    connectionMode = ConnectionMode.BLUETOOTH_CONNECTION

    def __init__(self):
        if self.connectionMode == ConnectionMode.BLUETOOTH_CONNECTION:
            self.socket = BluetoothConnection.initBluetoothConnection()
        elif self.connectionMode == ConnectionMode.TCP_CONNECTION:
            self.socket == TCPConnection.initTCPConnection()

    def start(self):
        self.socketRun = True
        print "The server is ready to receive"
        # Loop forever
        while self.socketRun:
            try:
                # server waits for incoming connections on accept()
                # for incoming requests, new socket created on return
                connectionSocket, addr = self.socket.accept()
                # receive sentence on newly established connectionSocket
                sentence = connectionSocket.recv(1024)
                print "Received: " + str(sentence)
                if sentence is not None:
                    CommunicationManager(connectionSocket).lineReceived(sentence)
            except OSError:
                pass

    def stop(self):
        self.socketRun = False

tcpServer = TcpServer()

try:
    tcpServer.start()
except KeyboardInterrupt, SystemExit:
    tcpServer.stop()
