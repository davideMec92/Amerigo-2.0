from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from project.hashgraph.models.Hashgraph import Hashgraph


class LockInitHelper:
    @staticmethod
    def initHashgraphGossipLocks(hashgraph: Hashgraph):
        count: int = 1
        for deviceId, peer in hashgraph.peers.items():
            if hashgraph.myPeer.deviceId == deviceId:
                if count % 2 == 0:
                    hashgraph.isHashgraphReceiveLocked = True
                    hashgraph.isHashgraphGossipLocked = False
                else:
                    hashgraph.isHashgraphGossipLocked = True
                    hashgraph.isHashgraphReceiveLocked = False
            count = count + 1
