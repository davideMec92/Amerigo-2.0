import unittest

from project.hashgraph.models.Peer import Peer
from project.hashgraph.models.Round import Round
from project.hashgraph.models.Hashgraph import Hashgraph


class StoreTest(unittest.TestCase):
    peer1 = Peer()
    peer1.deviceId = 'PEER_A'
    peer2 = Peer()
    peer2.deviceId = 'PEER_B'
    peerList = [peer1, peer2]

    def testRoundPutOK(self):
        event = self.peer1.createFirstEvent()
        eventRound = Round(event, 1)
        hashgraph = Hashgraph(self.peerList, self.peer1)
        hashgraph.store.putRound(eventRound)
        self.assertIsNotNone(hashgraph.store.rounds.pop(eventRound.roundCreated))

if __name__ == '__main__':
    unittest.main()
