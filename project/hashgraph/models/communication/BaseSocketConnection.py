import time
from socket import socket
from threading import Thread
from typing import List

from project.Logger.Logger import LogLevels, Logger
from project.hashgraph.builders.CommunicationMessageBuilder import CommunicationMessageBuilder
from project.hashgraph.enums.CommunicationMessageTypes import CommunicationMessageTypes
from project.hashgraph.helpers.CommunicationMessageDecrypter import CommunicationMessageDecrypter
from project.hashgraph.helpers.FifoQueue import FifoQueue
from project.hashgraph.helpers.Hash import Hash
from project.hashgraph.interfaces.Callbacks.CommunicationCallback import CommunicationCallback
from project.hashgraph.interfaces.Callbacks.ServerConnectionRemoveCallback import ServerConnectionRemoveCallback
from project.hashgraph.models.communication.CommunicationMessage import CommunicationMessage
from project.hashgraph.models.communication.CommunicationMessageACK import CommunicationMessageACK
from project.hashgraph.models.communication.CommunicationMessageNACK import CommunicationMessageNACK
from project.hashgraph.validators.communicationMessage.CommunicationMessageSchemaValidator import \
    CommunicationMessageSchemaValidator


class BaseSocketConnection(Thread):

    def __int__(self):
        self.key: str = None
        self.socket: socket = None
        self.isMessageSenderEnabled: bool = False
        self.isMessageListenerEnabled: bool = False
        self.toSendMessages: FifoQueue[CommunicationMessage] = FifoQueue[CommunicationMessage]()
        self.connectionCallbacks: List[CommunicationCallback] = []
        self.serverConnectionRemoveCallback: ServerConnectionRemoveCallback = None
        self.isReceiveAvailable: bool = False
        self.clientAddress: str = None
        Thread.__init__(self)

    def initSocket(self) -> None:

        if self.socket is None:
            raise Exception('Socket not initialized')

        Logger.createLog(LogLevels.DEBUG, __file__, 'Device address: ' + str(self.clientAddress))
        self.key = Hash.stringToHash(str(self.clientAddress))
        self.isMessageSenderEnabled = True

        # Starting listening for sending messages
        messagesToSendListener = Thread(target=self.checkToSendMessages)
        messagesToSendListener.start()

    def sendNewMessage(self, message: CommunicationMessage) -> None:
        self.toSendMessages.push(message)


    def sendMessageToListeners(self, message: CommunicationMessage) -> None:
        Logger.createLog(LogLevels.DEBUG, __file__, 'Sending message to handlers..')
        for connectionCallback in self.connectionCallbacks:
            connectionCallback.clientResponseCallback(message)

    def checkToSendMessages(self):
        while self.isMessageSenderEnabled is True:
            try:
                if self.toSendMessages.isEmpty() is False:
                    communicationMessage: CommunicationMessage = self.toSendMessages.pop()
                    Logger.createLog(LogLevels.DEBUG, __file__, "Sending message: " + str(communicationMessage.toJson()) + 'to: ' + str(self.clientAddress))
                    encryptedMessage: str = communicationMessage.encrypt()
                    if type(encryptedMessage) is not str:
                        encryptedMessage = str(encryptedMessage)
                        encryptedMessage = encryptedMessage.lstrip('b')
                        encryptedMessage = encryptedMessage.replace("'", "")
                    # self.socket.send(str(encryptedMessage) + "\r\n")
                    self.socket.send(str(encryptedMessage))
                    Logger.createLog(LogLevels.DEBUG, __file__, "Sent encrypted: " + str(communicationMessage.type) + 'to: ' + str(self.clientAddress))

                    # If block sent, close socket
                    if communicationMessage.type == CommunicationMessageTypes.BLOCK:
                        Logger.createLog(LogLevels.DEBUG, "Block sent, closing socket..")
                        self.closeSocket()

            except Exception as e:
                Logger.createLog(LogLevels.ERROR, __file__, "Socket error while sending message to: " + str(self.socket.getpeername()) + ", " + str(e))

    def closeSocket(self) -> None:
        try:
            self.socket.close()
            self.isMessageSenderEnabled = False
            self.isMessageListenerEnabled = False
        except Exception as e:
            Logger.createLog(LogLevels.ERROR, __file__, 'Error closing socket: ' + str(e))
        finally:
            self.serverConnectionRemoveCallback.removeSocketConnection(self.key)

    def run(self):

        self.isMessageSenderEnabled = True
        print('Listening for new messages..')

        incomingMessage: str = None

        # Listening for incoming messages while mRun is True
        while self.isMessageSenderEnabled is True:
            try:

                # receive sentence on newly established connectionSocket
                incomingMessage = self.recv_timeout()

                if incomingMessage is None or incomingMessage == '':
                    Logger.createLog(LogLevels.INFO, __file__, 'Received None message!')
                    continue

                Logger.createLog(LogLevels.DEBUG, __file__, "New Message: " + str(incomingMessage))
                incomingMessage = self.parseReceivedString(incomingMessage)
                incomingMessage = CommunicationMessageDecrypter.decrypt(incomingMessage)

                # Validate received message
                if CommunicationMessageSchemaValidator.validate(incomingMessage) is False:
                    continue

                communicationMessage: CommunicationMessage = CommunicationMessageBuilder.build(incomingMessage)

                if self.isReceiveAvailable is False:
                    # Check if hashgraph received, then send NACK
                    self.sendNewMessage(CommunicationMessageNACK())
                    Logger.createLog(LogLevels.DEBUG, __file__, "NACK added to send messages queue, other hashgraph attempt when receive not available from peer: " + str(communicationMessage.peer.deviceId))
                else:

                    # Check if hashgraph received, then send ACK
                    if communicationMessage.type == CommunicationMessageTypes.HASHGRAPH:
                        self.isReceiveAvailable = False
                        self.toSendMessages(CommunicationMessageACK())
                        Logger.createLog(LogLevels.DEBUG, __file__, "ACK added to send messages queue, hashgraph received from peer: " + str(communicationMessage.peer.deviceId))

                    # Check if ACK or NACK received
                    if communicationMessage.type == CommunicationMessageTypes.ACK or communicationMessage.type == CommunicationMessageTypes.NACK:
                        self.isReceiveAvailable = False
                        self.closeSocket()

                    # Broadcast communication message to listeners
                    self.sendMessageToListeners(communicationMessage)


            except Exception as e:
                Logger.createLog(LogLevels.ERROR, __file__, "Error while receiving data from socket: " + str(e))
                pass

    def parseReceivedString(self, receivedString):
        receivedString = receivedString.replace("\\n", "")
        receivedString = receivedString.replace("\\r", "")
        receivedString = receivedString.lstrip('b')
        return receivedString
            
    def recv_timeout(self, timeout=2):
        # make socket non blocking
        self.socket.setblocking(0)

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
                data = self.socket.recv(8192)
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
