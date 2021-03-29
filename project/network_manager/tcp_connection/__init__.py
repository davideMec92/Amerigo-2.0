from socket import *

class TCPConnection():

    COMMUNICATION_PORT = 1079

    @staticmethod
    def initTCPConnection(self):
        # create TCP socket
        socket = socket(AF_INET, SOCK_STREAM)
        # bind socket to local port number
        socket.bind(("", self.COMMUNICATION_PORT))
        # put socket in passive mode
        socket.listen(1)
        return socket