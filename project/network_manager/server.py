from socket import *
from communication_manager import CommunicationManager

class Server():

    COMMUNICATION_PORT = 1079

    serverSocket = None
    serverRun = False

    def __init__(self):
        # create TCP socket
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        # bind socket to local port number
        self.serverSocket.bind(("", self.COMMUNICATION_PORT))
        # put socket in passive mode
        self.serverSocket.listen(1)

    def start(self):
        self.serverRun = True
        print "The server is ready to receive"
        # Loop forever
        while self.serverRun:
            # server waits for incoming connections on accept()
            # for incoming requests, new socket created on return
            connectionSocket, addr = self.serverSocket.accept()
            # receive sentence on newly established connectionSocket
            sentence = connectionSocket.recv(1024)
            print "Received: " + str(sentence)
            if sentence is not None:
                CommunicationManager(connectionSocket).lineReceived(sentence)

    def stop(self):
        self.serverRun = False


Server().start()
