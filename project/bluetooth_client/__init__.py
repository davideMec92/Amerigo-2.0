import bluetooth
import sys
import time


class BluetoothClient():
    macAddress = None
    uuid = None
    socket = None
    socketRun = False

    def __init__(self, macAddress, uuid):
        self.macAddress = macAddress
        self.uuid = uuid

        try:
            service_matches = bluetooth.find_service(uuid=self.uuid, address=self.macAddress)

            if len(service_matches) == 0:
                print("Couldn't find the SampleServer service.")
                return None

            first_match = service_matches[0]
            port = first_match["port"]
            name = first_match["name"]
            host = first_match["host"]

            print(("Connecting to \"{}\" on {}".format(name, host)))

            # Create the client socket
            self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.socket.connect((host, port))

            print("Connected. Type something...")

        except Exception as e:
            print(("BluetoothClient error: " + str(e)))

    def sendMessage(self, message):
        try:
            print(("Sending message: " + str(message) + 'to: ' + str(self.macAddress)))
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

    def parseReceivedString(self, receivedString):
        receivedString = receivedString.replace("\\n", "")
        receivedString = receivedString.lstrip('b')
        return receivedString

    def sendMessageWithResponse(self, message):
        try:
            print(("Sending message: " + str(message) + 'to: ' + str(self.macAddress)))
            if type(message) is not str:
                message = str(message)
                message = message.lstrip('b')
                message = message.replace("'", "")
            self.socket.send(str(message) + "\n")

            self.socketRun = True

            # Loop forever
            while self.socketRun:
                # receive sentence on newly established connectionSocket
                sentence = self.recv_timeout(self.socket)

                print(("Received: " + str(sentence)))

                sentence = sentence.replace("\\n", "")
                sentence = sentence.lstrip('b')

                if sentence is not None:
                    return sentence
        except Exception as e:
            print("Socket error: " + str(e))
            self.socketRun = False
            return

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
            except Exception as e:
                pass

        # join all parts to make final string
        return ''.join(total_data)

    def close(self):
        self.socket.close()
