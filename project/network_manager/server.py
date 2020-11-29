from twisted.internet import protocol, reactor, defer, endpoints
from twisted.protocols import basic
from peer import Peer, PeerStatus
from peer_controller import PeerController
from communication_message import CommunicationMessage, CommunicationMessageTypes
import json

COMMUNICATION_PORT = '1079'
COMMUNICATION_PROTOCOL = 'tcp'

class FingerProtocol(basic.LineReceiver):

    communication_message = CommunicationMessage()

    def lineReceived(self, message):
        print('message: ' + str(message))
        self.managePeerMessage(str(message))

    def managePeerMessage(self, message):
        try:
            #print('Message: ' + str(json.loads(message)['type']))
            deserialized_message = self.communication_message.getMessage(message)

            if deserialized_message is None and 'type' not in deserialized_message:
                raise Exception('Cannot deserialize message')

            if deserialized_message['type'] == CommunicationMessageTypes.LOGIN.name:

                if self.factory.isUserLogged() is False:
                    ip, port = self.transport.client
                    if self.factory.clientSignup(deserialized_message['authToken'], ip, port, deserialized_message['macAddress']) is True:
                        out_message = {"type":CommunicationMessageTypes.INFO.name,"message":"Auth OK!"}
                        self.writeResponse(out_message, False)
                        #TODO: Close connection after this
                    else:
                        self.writeResponse('AUTH_TOKEN not correct, bye', False)
                        self.transport.loseConnection()
                        return False

                    self.factory.addPeer()
                    peers_list = PeerController.getPeers(PeerStatus.CONNECTED)
                    peers_message = {"type":CommunicationMessageTypes.PEERS_LIST.name,"peers": peers_list}
                    print 'PEERS_LIST: ' + str(peers_message)
                    self.notifyToPeers(peers_list, json.dumps(peers_message))
        except Exception, e:
            print('Error: ' + str(e))
            self.transport.loseConnection()

    def notifyToPeers(self, peers, message):

        if len(peers) == 0:
            raise Exception('Empty peers list provided')

        if message is None or len(message) == 0:
            raise Exception('Empyt or None message provided')

        print 'Sending message to peers..'

        for peer in peers:
            #TODO: Change this with sending message to ip:port of clients
            self.writeResponse(message, False)

    def writeResponse(self, message, encryption = True):
        self.communication_message = CommunicationMessage()
        self.transport.write(self.communication_message.setMessage(message, encryption) + b'\r\n')
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
