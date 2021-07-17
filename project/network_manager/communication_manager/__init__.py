from communication_message import CommunicationMessage, CommunicationMessageTypes
from peer_controller import PeerController
from peer_connection_manager import PeerConnectionManager
from peer import Peer, PeerStatus
from tcp_client import TcpClient
from bluetooth_client import BluetoothClient
from block import Block
from position_degrees import PositionDegrees
from block_queue import BlockQueue
from peer_position import PeerPosition
from position_degrees_controller import PositionDegreesController
from transaction import Transaction

import json

from responses import PositionsDegreesGetResponse


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
        print(('message: ' + str(message)))
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
                print(('Block message received: ' + str(deserialized_message)))
                print(('Block round created: ' + str(deserialized_message['block']['roundCreated'])))

                #Check if block received missing in db
                if Block.getFromRoundCreated(deserialized_message['block']['roundCreated']) is None:
                    self.blockQueue.putBlock(deserialized_message['block'])
            elif deserialized_message['type'] == CommunicationMessageTypes.POSITIONS_DEGREES.name:
                print(('Position degrees message received: ' + str(deserialized_message)))
                positionDegrees = PositionDegrees(deserialized_message["deviceId"], deserialized_message["positions"])
                positionDegrees.upsert()
            elif deserialized_message['type'] == CommunicationMessageTypes.TRANSACTION_GET.name:
                print(('Transaction get message received: ' + str(deserialized_message)))
                #Check if client auth token is authorized
                if( self.factory.checkClientAuthToken(deserialized_message["authToken"]) is True ):
                    transaction = Transaction.getFirst()
                    if transaction is not None:
                        positionDegrees = PositionDegrees.getFromDeviceId(transaction.goalPeerDeviceId)
                        if positionDegrees is not None:
                            peerGoalPosition = None
                            for peerPosition in positionDegrees.positions:
                                if peerPosition.deviceId == transaction.goalPeerDeviceId:
                                    peerGoalPosition = PeerPosition(peerPosition)

                            if peerGoalPosition is not None:
                                self.writeResponse(peerPosition.toDict())
            elif deserialized_message['type'] == CommunicationMessageTypes.POSITIONS_DEGREES_GET.name:
                print(('Position degrees GET message received: ' + str(deserialized_message)))
                peers = PeerController.getPeers()
                peerPositionsDegrees = PositionDegreesController.getPositionsDegrees()
                if len(peers) == len(peerPositionsDegrees):
                    self.writeResponse(PositionsDegreesGetResponse().build(peerPositionsDegrees))
                else:
                    self.writeResponse(PositionsDegreesGetResponse.baseSchema)


        except Exception as e:
            print(('Error: ' + str(e)))
        finally:
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

        print(('Peer list new: ' + str(message)))
        message = self.buildResponseCommunicationMessage(message)


        for peer in peers:
            print(('Connecting to: ' + str(peer['address'])))
            try:
                #tcpClient = TcpClient(peer['address'])
                tcpClient = BluetoothClient(peer['address'], peer['deviceId'])
                if tcpClient is None:
                    continue
                tcpClient.sendMessage(message)
                tcpClient.close()
                tcpClient = None
            except Exception as e:
                print(('Exception: ' + str(e)))

    def writeResponse(self, message, encryption = True):
        print(("Write response: " + str(message) + ',' + str(encryption)))
        self.connectionSocket.send( self.buildResponseCommunicationMessage(message, encryption))
        return True

    def buildResponseCommunicationMessage(self, message, encryption = True):
        self.communication_message = CommunicationMessage()
        return self.communication_message.setMessage(message, encryption)
