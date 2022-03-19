from __future__ import annotations

import threading
from random import randrange
from threading import Thread, Lock

from typing import List

from project.Logger.Logger import Logger, LogLevels
from project.hashgraph.interfaces.Callbacks.ServerConnectionRemoveCallback import ServerConnectionRemoveCallback
from project.hashgraph.models.Hashgraph import Hashgraph
from project.hashgraph.models.Peer import Peer
from project.hashgraph.models.communication.CommunicationMessageHashgraph import CommunicationMessageHashgraph
from project.hashgraph.services.bluetooth.BluetoothSocketConnection import BluetoothSocketConnection


class GossipProtocol(Thread, ServerConnectionRemoveCallback):
    instance: GossipProtocol | None = None
    lock = Lock()

    def __init__(self, hashgraph: Hashgraph, peerDeviceId: str):
        self.hashgraph: Hashgraph = hashgraph
        self.peerDeviceId = peerDeviceId
        self.peersKeys: List[str] = []
        self.run = True
        # TODO ADD BLUETOOTH CONNECTION MANAGER
        self.instance = self
        self.unlockGossipProtocolEvent = threading.Event()
        Thread.__init__(self)

    def updatePeerKeys(self) -> None:
        for peerDeviceId, peer in self.hashgraph.peers.items():
            if self.peerDeviceId == peerDeviceId:
                continue
            self.peersKeys.append(peerDeviceId)

    def getRandomPeer(self) -> Peer | None:
        return None if not self.peersKeys else self.peersKeys[randrange(len(self.peersKeys))]

    def run(self) -> None:
        while self.run is True:
            if self.hashgraph.lockHashgraphGossip() is False:
                try:
                    print('Waiting for unlockGossipProtocolEvent unlock')
                    self.unlockGossipProtocolEvent.wait()
                    Logger.createLog(LogLevels.DEBUG, __file__, 'unlockGossipProtocolEvent set to wait()')
                except Exception as e:
                    print('unlockGossipProtocolEvent wait failed: ' + str(e))
            else:
                try:
                    # Getting a random peer from list
                    randomPeer: Peer = self.getRandomPeer()

                    if randomPeer is None:
                        self.hashgraph.unlockHashgraphGossip()
                        continue

                    print('Try connecting to: ' + randomPeer.deviceId)

                    bluetoothSocketConnection: BluetoothSocketConnection = BluetoothSocketConnection.createFromUUIDAndMACAddress(randomPeer.deviceId, randomPeer.address, [], self)

                    # TODO CHECK IF SOCKET IS CONNECTED AND IMPLEMENTE THIS LOGIC
                    """
                    if( bluetoothSocketConnection == null ){
                        System.out.println("Connection failed");
                        this.hashgraph.unlockHashgraphGossip();
                        continue;
                    }
                    """

                    communicationMessageHashgraph: CommunicationMessageHashgraph = CommunicationMessageHashgraph.createFromHashgraph(self.hashgraph)
                    bluetoothSocketConnection.isReceiveAvailable = True
                    bluetoothSocketConnection.sendNewMessage(communicationMessageHashgraph)
                    Logger.createLog(LogLevels.DEBUG, __file__, 'Sending hashgraph to device with ID: ' + str(randomPeer.deviceId))

                except Exception as e:
                    print('Error while connection to peer for gossip: ' + str(e))

    def removeSocketConnection(self, connectionKey: str) -> None:
        print('TO IMPLEMENT METHOD IN BLUETOOTH MANAGER')







