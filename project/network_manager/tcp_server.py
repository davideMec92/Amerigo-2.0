from socket import *
from communication_manager import CommunicationManager

class TcpServer():

    COMMUNICATION_PORT = 1079

    socket = None
    host = None
    socketRun = False

    def __init__(self):
        # create TCP socket
        self.socket = socket(AF_INET, SOCK_STREAM)
        # bind socket to local port number
        self.socket.bind(("", self.COMMUNICATION_PORT))
        # put socket in passive mode
        self.socket.listen(1)

    def start(self):
        self.socketRun = True
        print "The server is ready to receive"
        # Loop forever
        while self.socketRun:
            # server waits for incoming connections on accept()
            # for incoming requests, new socket created on return
            connectionSocket, addr = self.socket.accept()
            # receive sentence on newly established connectionSocket
            sentence = connectionSocket.recv(1024)
            print "Received: " + str(sentence)
            if sentence is not None:
                CommunicationManager(connectionSocket).lineReceived(sentence)

    def stop(self):
        self.socketRun = False

tcpServer = TcpServer()
try:
    tcpServer.start()
except KeyboardInterrupt, SystemExit:
    tcpServer.stop()
