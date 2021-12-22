from collections import deque

from project.hashgraph.interfaces.StoreCallback import StoreCallback
from project.hashgraph.store import Store


class Hashgraph(StoreCallback):

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

    def __init__(self, peers, myPeer):
        self.peers = peers
        self.myPeer = myPeer
        self.store = Store(self)
        