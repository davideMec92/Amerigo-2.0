import unittest

from typing import List, Dict

from project.hashgraph.enums.PeerStatus import PeerStatus
from project.hashgraph.models.Hashgraph import Hashgraph
from project.hashgraph.models.Peer import Peer
from project.hashgraph.models.Transaction import Transaction


class HashgraphTest(unittest.TestCase):

    transactions: List[Transaction] = []

    peerA: Peer = Peer()
    peerB: Peer = Peer()
    peerC: Peer = Peer()
    peerD: Peer = Peer()

    hashgraph_peerA: Hashgraph | None = None
    hashgraph_peerB: Hashgraph | None = None
    hashgraph_peerC: Hashgraph | None = None
    hashgraph_peerD: Hashgraph | None = None

    peersList: Dict[str, Peer] = {}

    @classmethod
    def setUpClass(cls) -> None:

        print('Init Hashgraph tests..')

        cls.peerA.address = "192.168.1.1"
        cls.peerA.deviceId = "A"
        cls.peerA.status = PeerStatus.CONNECTED
        cls.transactions.append(Transaction(cls.peerA.deviceId))

        cls.peerB.address = "192.168.1.2"
        cls.peerB.deviceId = "B"
        cls.peerB.status = PeerStatus.CONNECTED

        cls.peerC.address = "192.168.1.3"
        cls.peerC.deviceId = "C"
        cls.peerC.status = PeerStatus.CONNECTED

        cls.peerD.address = "192.168.1.4"
        cls.peerD.deviceId = "D"
        cls.peerD.status = PeerStatus.CONNECTED

        cls.peersList[cls.peerA.deviceId] = cls.peerA
        cls.peersList[cls.peerB.deviceId] = cls.peerB
        cls.peersList[cls.peerC.deviceId] = cls.peerC
        cls.peersList[cls.peerD.deviceId] = cls.peerD

        cls.hashgraph_peerA = Hashgraph(cls.peersList, cls.peerA)
        cls.hashgraph_peerA.addUndeterminedEvents(cls.peerA.createFirstEvent())

        cls.hashgraph_peerB = Hashgraph(cls.peersList, cls.peerB)
        cls.hashgraph_peerB.addUndeterminedEvents(cls.peerB.createFirstEvent())

        """cls.hashgraph_peerC = Hashgraph(cls.peersList, cls.peerC)
        cls.hashgraph_peerC.addUndeterminedEvents(cls.peerC.createFirstEvent())

        cls.hashgraph_peerD = Hashgraph(cls.peersList, cls.peerD)
        cls.hashgraph_peerD.addUndeterminedEvents(cls.peerD.createFirstEvent())"""

    def testSimple(self):
        print('MY PEER A: ' + str(self.hashgraph_peerA.myPeer.deviceId))
        print('MY PEER B: ' + str(self.hashgraph_peerB.myPeer.deviceId))
        print('TO JSON: ' + self.hashgraph_peerA.store.toJson())
        self.assertTrue(True)

    """def talksWith(selfHashGraph: Hashgraph, otherHashgraph: Hashgraph, otherPeer: Peer){
        Store deserializedOtherStore = gson.fromJson(otherHashgraph.getStore().toJson(), Store.class);
        selfHashGraph.getNewOtherRounds(deserializedOtherStore);
        selfHashGraph.getNewOtherUndeterminedEvents(deserializedOtherStore);
        try {
            sleep(500);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        selfHashGraph.createEvent(otherPeer, transactions);
    }"""


    def test_something(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
