import socket

class TcpClient():

    COMMUNICATION_PORT = 2034
    SOCKET_TIMEOUT = 2

    socket = None
    host = None
    socketRun = False

    def __init__(self, host):
        self.host = host

        try:
            self.socket = socket.create_connection((self.host, self.COMMUNICATION_PORT), timeout=self.SOCKET_TIMEOUT)
        except socket.timeout:
            print("Socket timeout")
            raise Exception('Socket timeout raised')
        except socket.error:
            print("Socket timeout")
            raise Exception('Socket error raised')

    def sendMessage(self, message):
        try:
            print("Sending message: " + str(message) + 'to: ' + str(self.host))
            self.socket.send(message + "\n")
        except socket.timeout:
            print("Socket timeout")
            return
        except socket.error:
            print("Socket timeout")
            return

    def close(self):
        self.socket.close()
