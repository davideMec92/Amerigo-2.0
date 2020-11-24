from twisted.internet import protocol, reactor, defer, endpoints
from twisted.protocols import basic
from cryptography.fernet import Fernet
from peer import Peer, PeerStatus

class FingerProtocol(basic.LineReceiver):

    ENCRYPTION_KEY = 'Jli5assvwZKQBWxm0n3DYPqT27wWrpqcjWyOcXNUSAQ='

    def lineReceived(self, message):
        print('message: ' + str(message))
        if self.factory.isUserLogged() is False:
            ip, port = self.transport.client
            if self.factory.clientSignup(message, ip, port) is True:
                self.writeResponse(self.ENCRYPTION_KEY)
            else:
                self.writeResponse('AUTH_TOKEN not correct, by')
                self.transport.loseConnection()
        else:
            self.factory.addPeer()

    def writeResponse(self, message):
        self.transport.write(message + b'\r\n')
        return True


class FingerFactory(protocol.ServerFactory):
    protocol = FingerProtocol
    authenticated = False
    ip_address = None
    bluetooth_mac = 'sciaobela'
    peer = None
    AUTH_TOKEN = 'Hs8GckGahlvzOTZBMpMLTa2gjMjEnRDf'

    def isUserLogged(self):
        return self.authenticated

    def clientSignup(self, authenticationToken, ip_address, port):
        print('New Client IP_ADDRESS: ' + str(ip_address) + ' PORT: ' + str(port))
        self.ip_address = ip_address

        if authenticationToken is None:
            raise Exception('Authentication token cannot be null')

        #Check client authentication
        if self.authenticated is False:
            print('Client not authenticated')
            if authenticationToken == self.AUTH_TOKEN:
                self.authenticated = True
            else:
                print('AUTH_TOKEN not correct, by')

        return self.authenticated

    def addPeer(self):
        print('Creating new peer')
        peer = Peer(self.bluetooth_mac, self.ip_address, PeerStatus.CONNECTED)
        print('Saving peer..')
        peer.upsert()

fingerEndpoint = endpoints.serverFromString(reactor, "tcp:1079")
fingerEndpoint.listen(FingerFactory())
reactor.run()
