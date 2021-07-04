
from communication_manager import CommunicationManager
from enum import Enum
from bluetooth_connection import BluetoothConnection
from tcp_connection import TCPConnection
from block_queue import BlockQueue
import time

class ConnectionMode(Enum):
    TCP_CONNECTION = 'TCP_CONNECTION'
    BLUETOOTH_CONNECTION = 'BLUETOOTH_CONNECTION'

class Server():

    socket = None
    socketRun = False
    connectionMode = ConnectionMode.BLUETOOTH_CONNECTION
    blockQueue = BlockQueue()

    def __init__(self):
        if self.connectionMode == ConnectionMode.BLUETOOTH_CONNECTION:
            self.socket = BluetoothConnection.initBluetoothConnection()
        elif self.connectionMode == ConnectionMode.TCP_CONNECTION:
            self.socket == TCPConnection.initTCPConnection()
        #Starting block queue
        self.blockQueue.start()

    def start(self):
        self.socketRun = True
        # Loop forever
        while self.socketRun:
            try:
                # server waits for incoming connections on accept()
                # for incoming requests, new socket created on return
                connectionSocket, addr = self.socket.accept()
                # receive sentence on newly established connectionSocket
                sentence = self.recv_timeout(connectionSocket)

                print(("Received: " + str(sentence)))

                if self.connectionMode == ConnectionMode.BLUETOOTH_CONNECTION:
                    sentence = sentence.replace("\\n", "")
                    sentence = sentence.lstrip('b')

                if sentence is not None:
                    CommunicationManager(connectionSocket, self.blockQueue).lineReceived(sentence)
            except OSError:
                pass

    def parseReceivedString(self, receivedString):
        receivedString = receivedString.replace("\\n", "")
        receivedString = receivedString.lstrip('b')
        return receivedString

    def recv_timeout(self, socket, timeout=2):
        # make socket non blocking
        socket.setblocking(0)

        # total data partwise in an array
        total_data = [];
        data = '';

        # beginning time
        begin = time.time()
        while 1:
            # if you got some data, then break after timeout
            if total_data and time.time() - begin > timeout:
                break

            # if you got no data at all, wait a little longer, twice the timeout
            elif time.time() - begin > timeout * 2:
                break

            # recv something
            try:
                data = socket.recv(8192)
                if data:
                    total_data.append(self.parseReceivedString(str(data)))
                    # change the beginning time for measurement
                    begin = time.time()
                else:
                    # sleep for sometime to indicate a gap
                    time.sleep(0.1)
            except:
                pass

        # join all parts to make final string
        return ''.join(total_data)

    def stop(self):
        self.socketRun = False

server = Server()

try:
    server.start()
except (KeyboardInterrupt, SystemExit):
    server.stop()
