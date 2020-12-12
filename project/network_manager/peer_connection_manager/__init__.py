from peer import Peer, PeerStatus

class PeerConnectionManager():
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
