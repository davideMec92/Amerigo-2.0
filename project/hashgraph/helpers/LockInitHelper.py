from project.hashgraph.models.Hashgraph import Hashgraph


class LockInitHelper:
    @staticmethod
    def initHashgraphGossipLocks(hashgraph: Hashgraph):
        count: int = 1
        for deviceId, peer in hashgraph.peers:
            if hashgraph.myPeer.deviceId == deviceId:
                if count % 2 == 0:
                    hashgraph.isHashgraphReceiveLocked = True
                    hashgraph.isHashgraphGossipLocked = False
                else:
                    hashgraph.isHashgraphGossipLocked = True
                    hashgraph.isHashgraphReceiveLocked = False
            count = count + 1
