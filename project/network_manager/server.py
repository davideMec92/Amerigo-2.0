# Read username, output from non-empty factory, drop connections
# Use deferreds, to minimize synchronicity assumptions

from twisted.internet import protocol, reactor, defer, endpoints
from twisted.protocols import basic
import uuid

class FingerProtocol(basic.LineReceiver):

    def lineReceived(self, authenticationToken):
        self.createCallback(self.peerSignup(authenticationToken))
        #self.createCallback(self.factory.getUser(user))

    def onError(self, err):
        return 'Internal error in server'

    def writeResponse(self, message):
        self.transport.write(message + b'\r\n')
        self.transport.loseConnection()
        return True

    def createCallback(self, method):
        deferred = defer.Deferred()
        deferred.callback(method)
        deferred.addCallback(self.writeResponse)
        deferred.addErrback(self.onError)
        return deferred

    def peerSignup(self, authenticationToken):

        if authenticationToken is None:
            raise Exception('Authentication token cannot be null')

        if authenticationToken == 'ciao':
            return 'Siamo al top!'
        else:
            return 'Merda'

class FingerFactory(protocol.ServerFactory):
    protocol = FingerProtocol

    def __init__(self, users):
        self.users = users

    def generateUUID(self):
        return str(uuid.uuid4())

    def getUser(self, user):
        return self.generateUUID() if self.users.get(user, False) else 'User not found'

fingerEndpoint = endpoints.serverFromString(reactor, "tcp:1079")
fingerEndpoint.listen(FingerFactory({b'moshez': b'Happy and well'}))
reactor.run()
