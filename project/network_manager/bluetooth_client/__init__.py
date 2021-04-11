import bluetooth
import sys

class BluetoothClient():

    macAddress = None
    uuid = None
    socket = None

    def __init__(self, macAddress, uuid):
        self.macAddress = macAddress
        self.uuid = uuid

        try:
            service_matches = bluetooth.find_service(uuid=self.uuid, address=self.macAddress)

            if len(service_matches) == 0:
                print("Couldn't find the SampleServer service.")
                sys.exit(0)

            first_match = service_matches[0]
            port = first_match["port"]
            name = first_match["name"]
            host = first_match["host"]

            print("Connecting to \"{}\" on {}".format(name, host))

            # Create the client socket
            self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.socket.connect((host, port))

            print("Connected. Type something...")

        except(Exception, e):
            print("BluetoothClient error: " + str(e))

    def sendMessage(self, message):
        try:
            print("Sending message: " + str(message) + 'to: ' + str(self.macAddress))
            if type(message) is not str:
                message = str(message)
                message = message.lstrip('b')
                message = message.replace("'", "")
            self.socket.send(str(message) + "\r\n")
        except socket.timeout:
            print("Socket timeout")
            return
        except socket.error:
            print("Socket timeout")
            return

    def close(self):
        self.socket.close()
