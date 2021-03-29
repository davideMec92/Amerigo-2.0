from communication_message import CommunicationMessage, CommunicationMessageTypes
from peer_controller import PeerController
from peer_connection_manager import PeerConnectionManager
from peer import Peer, PeerStatus
from tcp_client import TcpClient
from block import Block

import json

class CommunicationManager():

    factory = None
    connectionSocket = None
    communication_message = CommunicationMessage()
    factory = PeerConnectionManager()

    def __init__(self, connectionSocket):
        self.connectionSocket = connectionSocket

    def lineReceived(self, message):
        print('message: ' + str(message))
        self.managePeerMessage(str(message))

    def managePeerMessage(self, message):
        try:
            deserialized_message = self.communication_message.getMessage(message)

            if deserialized_message is None and 'type' not in deserialized_message:
                raise Exception('Cannot deserialize message')

            if deserialized_message['type'] == CommunicationMessageTypes.LOGIN.name:

                ip, port = self.connectionSocket.getpeername()

                if self.factory.clientSignup(deserialized_message['authToken'], ip, port, deserialized_message['deviceId']) is True:
                    out_message = {"type":CommunicationMessageTypes.INFO.name,"message":"Auth OK!"}
                    self.writeResponse(out_message)
                    self.connectionSocket.close()
                else:
                    self.writeResponse('AUTH_TOKEN not correct, bye', False)
                    self.connectionSocket.close()
                    return False

                self.factory.addPeer(self.peersListCallback)
            elif deserialized_message['type'] == CommunicationMessageTypes.BLOCK.name:
                print 'Block message received: ' + str(deserialized_message)

                #Check if block received missing in db
                if Block.getFromRoundCreated(deserialized_message['block']['roundCreated']) is None:
                    newBlock = Block(deserialized_message['block'])
                    newBlock.upsert()
                    print 'New block saved! (Round created: ' + str(newBlock.roundCreated) + ')'

        except Exception, e:
            print('Error: ' + str(e.message))
            self.connectionSocket.close()

    def peersListCallback(self):
        peers_list = PeerController.getPeers(PeerStatus.CONNECTED)
        peers_message = {"type":CommunicationMessageTypes.PEERS_LIST.name, "peers": []}
        for peer in peers_list:
            peers_message["peers"].append(peer)
        self.notifyToPeers(peers_list, peers_message)

    def notifyToPeers(self, peers, message):

        if len(peers) == 0:
            raise Exception('Empty peers list provided')

        if message is None or len(message) == 0:
            raise Exception('Empyt or None message provided')

        print 'Sending message to peers..'

        message = self.buildResponseCommunicationMessage(message)

        for peer in peers:
            print('Connecting to: ' + str(peer['ipAddress']))
            try:
                tcpClient = TcpClient(peer['ipAddress'])
                tcpClient.sendMessage(message)
                tcpClient.close()
                tcpClient = None
            except Exception, e:
                print('Exception: ' + str(e))

    def writeResponse(self, message, encryption = True):
        print("Write response: " + str(message) + ',' + str(encryption))
        self.connectionSocket.send( self.buildResponseCommunicationMessage(message, encryption)+ "\r")
        return True

    def buildResponseCommunicationMessage(self, message, encryption = True):
        self.communication_message = CommunicationMessage()
        return self.communication_message.setMessage(message, encryption)
