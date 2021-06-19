from communication_message import CommunicationMessage, CommunicationMessageTypes
from peer_controller import PeerController
from peer_connection_manager import PeerConnectionManager
from peer import Peer, PeerStatus
from tcp_client import TcpClient
from bluetooth_client import BluetoothClient
from block import Block
from block_queue import BlockQueue

import json

class CommunicationManager():

    factory = None
    connectionSocket = None
    communication_message = CommunicationMessage()
    factory = PeerConnectionManager()
    blockQueue = BlockQueue()

    def __init__(self, connectionSocket, blockQueue):
        self.connectionSocket = connectionSocket
        self.blockQueue = blockQueue

    def lineReceived(self, message):
        print('message: ' + str(message))
        self.managePeerMessage(message)

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
                    #self.connectionSocket.close()
                else:
                    self.writeResponse('AUTH_TOKEN not correct, bye', False)
                    self.connectionSocket.close()
                    return False

                self.factory.addPeer(self.peersListCallback)
            elif deserialized_message['type'] == CommunicationMessageTypes.BLOCK.name:
                print ('Block message received: ' + str(deserialized_message))
                print ('Block round created: ' + str(deserialized_message['block']['roundCreated']))

                #Check if block received missing in db
                if Block.getFromRoundCreated(deserialized_message['block']['roundCreated']) is None:
                    #newBlock = Block(deserialized_message['block'])
                    self.blockQueue.putBlock(deserialized_message['block'])
                    print('######### PUT TASK IN QUEUE ########')
                    """print ('Events: ' + str(newBlock.events))
                    print ('Block to dict: ' + str(newBlock.toDict()))
                    newBlock.save()
                    print ('Block to dict: ' + str(newBlock.toDict()))
                    print ('New block saved! (Round created: ' + str(newBlock.roundCreated) + ')')"""
            #TODO ADD POSITIONS_DEGREES ELIF HANDLER
        except Exception as e:
            print('Error: ' + str(e))
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

        print ('Sending message to peers..')

        print('Peer list new: ' + str(message))
        message = self.buildResponseCommunicationMessage(message)


        for peer in peers:
            print('Connecting to: ' + str(peer['address']))
            try:
                #tcpClient = TcpClient(peer['address'])
                tcpClient = BluetoothClient(peer['address'], peer['deviceId'])
                if tcpClient is None:
                    continue
                tcpClient.sendMessage(message)
                tcpClient.close()
                tcpClient = None
            except Exception as e:
                print('Exception: ' + str(e))

    def writeResponse(self, message, encryption = True):
        print("Write response: " + str(message) + ',' + str(encryption))
        #self.connectionSocket.send( self.buildResponseCommunicationMessage(message, encryption))
        self.connectionSocket.send( self.buildResponseCommunicationMessage(message, encryption))
        return True

    def buildResponseCommunicationMessage(self, message, encryption = True):
        self.communication_message = CommunicationMessage()
        return self.communication_message.setMessage(message, encryption)
