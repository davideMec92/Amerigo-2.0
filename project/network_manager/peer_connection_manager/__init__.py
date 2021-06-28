from peer import Peer, PeerStatus

class PeerConnectionManager():
    #authenticated = False
    address = None
    deviceId = None
    peer = None
    AUTH_TOKEN = 'Hs8GckGahlvzOTZBMpMLTa2gjMjEnRDf'

    #def isUserLogged(self):
        #return self.authenticated

    def clientSignup(self, authentication_token, address, port, deviceId):
        print(('New Client IP_ADDRESS: ' + str(address) + ' PORT: ' + str(port)))
        self.address = address

        if authentication_token is None:
            raise Exception('Authentication token cannot be null')

        if deviceId is None:
            raise Exception('Bluetooth mac token cannot be null')

        #TODO VALIDATE BLUETOOTH MAC ADDRESS
        self.deviceId = deviceId

        print(("Device id: " + str(deviceId)))

        #Check client authentication
        """if self.authenticated is False:
            print('Client not authenticated')
            if authentication_token == self.AUTH_TOKEN:
                self.authenticated = True
            else:
                print('AUTH_TOKEN not correct, by')"""

        return self.checkClientAuthToken(authentication_token)

    def checkClientAuthToken(self, authenticationToken):
        if authenticationToken == self.AUTH_TOKEN:
            return True
        else:
            print('AUTH_TOKEN not correct, by')
            return False

    def addPeer(self, callback = None):
        print('Creating new peer')
        peer = Peer(self.deviceId, self.address, PeerStatus.CONNECTED)
        print('Saving peer..')
        peer.upsert()
        if callback is not None:
            callback()
