import unittest

from typing import Dict

from project.hashgraph.models.Peer import Peer
from project.hashgraph.models.Round import Round
from project.hashgraph.models.Hashgraph import Hashgraph


class StoreTest(unittest.TestCase):
    peer1 = Peer()
    peer1.deviceId = 'PEER_A'
    peer2 = Peer()
    peer2.deviceId = 'PEER_B'
    peerList: Dict[str, Peer] = {peer1.deviceId: peer1, peer2.deviceId: peer2}
    hashgraph: Hashgraph = Hashgraph(peerList, peer1)

    @classmethod
    def tearDownClass(cls) -> None:
        print('Stopping hashgraph block manager..')
        cls.hashgraph.blockManager.stopSending()

    def testRoundPutOK(self):
        event = self.peer1.createFirstEvent()
        eventRound = Round.create(event, 1)
        self.hashgraph.store.putRound(eventRound)
        self.assertIsNotNone(self.hashgraph.store.rounds.pop(eventRound.roundCreated))

if __name__ == '__main__':
    unittest.main()
