import json
import unittest

from project.hashgraph.Peer import Peer
from project.hashgraph.Round import Round
from project.hashgraph.Hashgraph import Hashgraph


class StoreTest(unittest.TestCase):
    def testRoundPut(self):
        peer1 = Peer()
        peer1.deviceId = 'PEER_A'
        peer2 = Peer()
        peer2.deviceId = 'PEER_B'
        peerList = [peer1, peer2]
        event = peer1.createFirstEvent()
        round = Round(event, 1)
        hashgraph = Hashgraph(peerList, peer1)
        hashgraph.store.putRound(round)
        self.assertIsNotNone(hashgraph.store.rounds.get(round.roundCreated))  # add assertion here


if __name__ == '__main__':
    unittest.main()
