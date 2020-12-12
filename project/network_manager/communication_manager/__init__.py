from communication_message import CommunicationMessage, CommunicationMessageTypes
from peer_controller import PeerController
from peer_connection_manager import PeerConnectionManager
from peer import Peer, PeerStatus

import json

class CommunicationManager():

    factory = None
    connectionSocket = None
    communication_message = CommunicationMessage()

    def __init__(self, connectionSocket):
        self.factory = PeerConnectionManager()
        self.connectionSocket = connectionSocket

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
                    ip, port = self.connectionSocket.getpeername()
                    if self.factory.clientSignup(deserialized_message['authToken'], ip, port, deserialized_message['macAddress']) is True:
                        out_message = {"type":CommunicationMessageTypes.INFO.name,"message":"Auth OK!"}
                        self.writeResponse(out_message)
                        #TODO: Close connection after this
                    else:
                        self.writeResponse('AUTH_TOKEN not correct, bye', False)
                        self.connectionSocket.close()
                        return False

                    self.factory.addPeer()
                    peers_list = PeerController.getPeers(PeerStatus.CONNECTED)
                    peers_message = {"type":CommunicationMessageTypes.PEERS_LIST.name,"peers": peers_list}
                    print 'PEERS_LIST: ' + str(peers_message)
                    self.notifyToPeers(peers_list, json.dumps(peers_message))
        except Exception, e:
            print('Error: ' + str(e))
            self.connectionSocket.close()

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
        self.connectionSocket.send(self.communication_message.setMessage(message, encryption) + "\n")
        return True
