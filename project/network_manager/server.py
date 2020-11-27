from twisted.internet import protocol, reactor, defer, endpoints
from twisted.protocols import basic
from peer import Peer, PeerStatus
from communication_message import CommunicationMessage, CommunicationMessageTypes
import json

COMMUNICATION_PORT = '1079'
COMMUNICATION_PROTOCOL = 'tcp'

class FingerProtocol(basic.LineReceiver):
    def lineReceived(self, message):
        print('message: ' + str(message))
        self.managePeerMessage(str(message))

    def managePeerMessage(self, message):
        try:
            print('Message: ' + str(json.loads(message)['type']))
            deserialized_message = json.loads(message)
            print type(message)
            print type(deserialized_message)
            print str(deserialized_message)

            if deserialized_message is None and 'type' not in deserialized_message:
                print('Cannot deserialize message')
                self.transport.loseConnection()

            if deserialized_message['type'] == CommunicationMessageTypes.LOGIN.name:
                if CommunicationMessage.check(CommunicationMessage.LOGIN_CONF_SCHEMA, deserialized_message) is False:
                    print('Login data validation failed')
                    self.transport.loseConnection()

                if self.factory.isUserLogged() is False:
                    ip, port = self.transport.client
                    if self.factory.clientSignup(deserialized_message['authToken'], ip, port, deserialized_message['macAddress']) is True:
                        self.writeResponse(CommunicationMessage.ENCRYPTION_KEY, False)
                    else:
                        self.writeResponse('AUTH_TOKEN not correct, by', False)
                        self.transport.loseConnection()
                        return False

                    self.factory.addPeer()
        except Exception, e:
            print('Error: ' + str(e))
            self.transport.loseConnection()

    def writeResponse(self, message, encryption = True):
        communication_message = CommunicationMessage()
        self.transport.write(communication_message.setMessage(message, encryption) + b'\r\n')
        return True


class FingerFactory(protocol.ServerFactory):
    protocol = FingerProtocol
    authenticated = False
    ip_address = None
    bluetooth_mac = None
    peer = None
    AUTH_TOKEN = 'Hs8GckGahlvzOTZBMpMLTa2gjMjEnRDf'

    def isUserLogged(self):
        return self.authenticated

    def clientSignup(self, authentication_token, ip_address, port, bluetooth_mac):
        print('New Client IP_ADDRESS: ' + str(ip_address) + ' PORT: ' + str(port))
        self.ip_address = ip_address

        if authentication_token is None:
            raise Exception('Authentication token cannot be null')

        if bluetooth_mac is None:
            raise Exception('Bluetooth mac token cannot be null')

        #TODO VALIDATE BLUETOOTH MAC ADDRESS
        self.bluetooth_mac = bluetooth_mac

        #Check client authentication
        if self.authenticated is False:
            print('Client not authenticated')
            if authentication_token == self.AUTH_TOKEN:
                self.authenticated = True
            else:
                print('AUTH_TOKEN not correct, by')

        return self.authenticated

    def addPeer(self):
        print('Creating new peer')
        peer = Peer(self.bluetooth_mac, self.ip_address, PeerStatus.CONNECTED)
        print('Saving peer..')
        peer.upsert()

fingerEndpoint = endpoints.serverFromString(reactor, COMMUNICATION_PROTOCOL + ":" + COMMUNICATION_PORT)
fingerEndpoint.listen(FingerFactory())
reactor.run()
