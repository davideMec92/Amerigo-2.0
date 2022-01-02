from abc import ABC
from collections import deque
from typing import List

from project.hashgraph.Peer import Peer
from project.hashgraph.Store import Store
from project.hashgraph.interfaces.StoreCallback import StoreCallback


class Hashgraph(StoreCallback):

    def eventStoredCallback(self):
        pass

    peers = {}
    lastConsensusRound = -1
    lastDecidedRound = -1
    lastPeersCreatorIndex = {}
    myPeer = None
    myPeerLastEvent = None
    store = None
    COIN_ROUND_FREQ = 10
    instance = None
    blockManager = None
    toSendTransactions = deque()

    isHashgraphGossipLocked = None
    isHashgraphReceiveLocked = None

    def __init__(self, peers: List[Peer], myPeer: Peer):
        self.peers = peers
        self.myPeer = myPeer
        self.store = Store(self)
