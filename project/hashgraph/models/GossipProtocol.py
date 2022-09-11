from __future__ import annotations

import threading
import random
from threading import Thread, Lock
from typing import List

from project.Logger.Logger import Logger, LogLevels
from project.hashgraph.models.Hashgraph import Hashgraph
from project.hashgraph.models.Peer import Peer
from project.hashgraph.models.communication.CommunicationMessageHashgraph import CommunicationMessageHashgraph
from project.hashgraph.services.bluetooth.BluetoothSocketConnection import BluetoothSocketConnection

class GossipProtocol(Thread):
    instance: GossipProtocol | None = None
    lock = Lock()

    def __init__(self, hashgraph: Hashgraph, peerDeviceId: str):
        from project.hashgraph.managers.services.BluetoothConnectionManager import BluetoothConnectionManager
        self.hashgraph: Hashgraph = hashgraph
        self.peerDeviceId = peerDeviceId
        self.peersKeys: List[str] = []
        self.isRunning: bool = True
        self.updatePeerKeys()
        self.bluetoothConnectionManager: BluetoothConnectionManager = BluetoothConnectionManager.getInstance()
        GossipProtocol.instance = self
        self.unlockGossipProtocolEvent = threading.Event()
        Thread.__init__(self)

    def updatePeerKeys(self) -> None:
        for peerDeviceId, peer in self.hashgraph.peers.items():
            if self.peerDeviceId == peerDeviceId:
                continue
            self.peersKeys.append(peerDeviceId)

    def getRandomPeer(self) -> Peer | None:
        if not self.peersKeys:
            return None

        return self.hashgraph.peers.get(self.peersKeys[random.randrange(len(self.peersKeys))])

    def run(self):
        while self.isRunning is True:
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

                    bluetoothSocketConnection: BluetoothSocketConnection = self.bluetoothConnectionManager.newBluetoothSocketConnection(randomPeer.deviceId, randomPeer.address, True)

                    if bluetoothSocketConnection is None:
                        Logger.createLog(LogLevels.ERROR, __file__, 'Cannot initialize bluetooth socket connection')
                        self.hashgraph.unlockHashgraphGossip()
                        continue

                    communicationMessageHashgraph: CommunicationMessageHashgraph = CommunicationMessageHashgraph.createFromHashgraph(self.hashgraph)
                    bluetoothSocketConnection.isReceiveAvailable = True
                    bluetoothSocketConnection.sendNewMessage(communicationMessageHashgraph)
                    Logger.createLog(LogLevels.DEBUG, __file__, 'Sending hashgraph to device with ID: ' + str(randomPeer.deviceId))

                except Exception as e:
                    print('Error while connection to peer for gossip: ' + str(e))
