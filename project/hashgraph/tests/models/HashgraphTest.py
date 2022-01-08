import unittest
from typing import List, Dict

from project.hashgraph.enums.PeerStatus import PeerStatus
from project.hashgraph.helpers.models.JSONDecoders.StoreJSONDecoder import StoreJSONDecoder
from project.hashgraph.models.Hashgraph import Hashgraph
from project.hashgraph.models.Peer import Peer
from project.hashgraph.models.Store import Store
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

        cls.hashgraph_peerC = Hashgraph(cls.peersList, cls.peerC)
        cls.hashgraph_peerC.addUndeterminedEvents(cls.peerC.createFirstEvent())

        cls.hashgraph_peerD = Hashgraph(cls.peersList, cls.peerD)
        cls.hashgraph_peerD.addUndeterminedEvents(cls.peerD.createFirstEvent())

        # PeerB talkswith PeerD
        cls.talksWith(cls.hashgraph_peerD, cls.hashgraph_peerB, cls.peerB)

        # PeerD talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerD, cls.peerD)

        # PeerB talks with PeerD
        cls.talksWith(cls.hashgraph_peerD, cls.hashgraph_peerB, cls.peerB)

        # PeerB talks with PeerA
        cls.talksWith(cls.hashgraph_peerA, cls.hashgraph_peerB, cls.peerB)

        # PeerC talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerC, cls.peerC)

        # PeerB talks with PeerD
        cls.talksWith(cls.hashgraph_peerD, cls.hashgraph_peerB, cls.peerB)

        # PeerB talks with PeerC
        cls.talksWith(cls.hashgraph_peerC, cls.hashgraph_peerB, cls.peerB)

        # PeerD talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerD, cls.peerD)

        # Starts Round 1

        # PeerA talks with PeerD
        cls.talksWith(cls.hashgraph_peerD, cls.hashgraph_peerA, cls.peerA)

        # PeerD talks with PeerA
        cls.talksWith(cls.hashgraph_peerA, cls.hashgraph_peerD, cls.peerD)

        # PeerC talks with PeerA
        cls.talksWith(cls.hashgraph_peerA, cls.hashgraph_peerC, cls.peerC)

        # PeerD talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerD, cls.peerD)

        # PeerA talks with PeerC
        cls.talksWith(cls.hashgraph_peerC, cls.hashgraph_peerA, cls.peerA)

        # PeerB talks with PeerD
        cls.talksWith(cls.hashgraph_peerD, cls.hashgraph_peerB, cls.peerB)

        # PeerB talks with PeerA
        cls.talksWith(cls.hashgraph_peerA, cls.hashgraph_peerB, cls.peerB)

        # PeerA talks with PeerD
        cls.talksWith(cls.hashgraph_peerD, cls.hashgraph_peerA, cls.peerA)

        # PeerA talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerA, cls.peerA)

        # Starts round 2

        # PeerD talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerD, cls.peerD)

        # PeerB talks with PeerD
        cls.talksWith(cls.hashgraph_peerD, cls.hashgraph_peerB, cls.peerB)

        # PeerB talks with PeerA
        cls.talksWith(cls.hashgraph_peerA, cls.hashgraph_peerB, cls.peerB)

        # PeerA talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerA, cls.peerA)

        # PeerA talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerA, cls.peerA)

        # PeerC talks with PeerD
        cls.talksWith(cls.hashgraph_peerD, cls.hashgraph_peerC, cls.peerC)

        # PeerD talks with PeerC
        cls.talksWith(cls.hashgraph_peerC, cls.hashgraph_peerD, cls.peerD)

        # PeerB talks with PeerA
        cls.talksWith(cls.hashgraph_peerA, cls.hashgraph_peerB, cls.peerB)

        # PeerC talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerC, cls.peerC)

        # PeerB talks with PeerA
        cls.talksWith(cls.hashgraph_peerA, cls.hashgraph_peerB, cls.peerB)

        # PeerB talks with PeerD
        cls.talksWith(cls.hashgraph_peerD, cls.hashgraph_peerB, cls.peerB)

        # PeerA talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerA, cls.peerA)

        # Starts round 3

        # PeerC talks with PeerD
        cls.talksWith(cls.hashgraph_peerD, cls.hashgraph_peerC, cls.peerC)

        # PeerD talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerD, cls.peerD)

        # PeerB talks with PeerC
        cls.talksWith(cls.hashgraph_peerC, cls.hashgraph_peerB, cls.peerB)

        # TEST
        # PeerD talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerD, cls.peerD)

        # PeerB talks with PeerD
        cls.talksWith(cls.hashgraph_peerD, cls.hashgraph_peerB, cls.peerB)

        # PeerB talks with PeerA
        cls.talksWith(cls.hashgraph_peerA, cls.hashgraph_peerB, cls.peerB)

        # PeerA talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerA, cls.peerA)

        # PeerA talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerA, cls.peerA)

        # PeerC talks with PeerD
        cls.talksWith(cls.hashgraph_peerD, cls.hashgraph_peerC, cls.peerC)

        # PeerD talks with PeerC
        cls.talksWith(cls.hashgraph_peerC, cls.hashgraph_peerD, cls.peerD)

        # PeerB talks with PeerA
        cls.talksWith(cls.hashgraph_peerA, cls.hashgraph_peerB, cls.peerB)

        # PeerC talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerC, cls.peerC)

        # PeerB talks with PeerA
        cls.talksWith(cls.hashgraph_peerA, cls.hashgraph_peerB, cls.peerB)

        # PeerB talks with PeerD
        cls.talksWith(cls.hashgraph_peerD, cls.hashgraph_peerB, cls.peerB)

        # PeerA talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerA, cls.peerA)

        # PeerD talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerD, cls.peerD)

        # PeerB talks with PeerD
        cls.talksWith(cls.hashgraph_peerD, cls.hashgraph_peerB, cls.peerB)

        # PeerB talks with PeerA
        cls.talksWith(cls.hashgraph_peerA, cls.hashgraph_peerB, cls.peerB)

        # PeerA talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerA, cls.peerA)

        # PeerA talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerA, cls.peerA)

        # PeerC talks with PeerD
        cls.talksWith(cls.hashgraph_peerD, cls.hashgraph_peerC, cls.peerC)

        # PeerD talks with PeerC
        cls.talksWith(cls.hashgraph_peerC, cls.hashgraph_peerD, cls.peerD)

        # PeerB talks with PeerA
        cls.talksWith(cls.hashgraph_peerA, cls.hashgraph_peerB, cls.peerB)

        # PeerC talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerC, cls.peerC)

        # PeerB talks with PeerA
        cls.talksWith(cls.hashgraph_peerA, cls.hashgraph_peerB, cls.peerB)

        # PeerB talks with PeerD
        cls.talksWith(cls.hashgraph_peerD, cls.hashgraph_peerB, cls.peerB)

        # PeerA talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerA, cls.peerA)

        # PeerD talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerD, cls.peerD)

        # PeerB talks with PeerD
        cls.talksWith(cls.hashgraph_peerD, cls.hashgraph_peerB, cls.peerB)

        # PeerC talks with PeerA
        cls.talksWith(cls.hashgraph_peerA, cls.hashgraph_peerC, cls.peerC)

        # PeerA talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerA, cls.peerA)

        # PeerA talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerA, cls.peerA)

        # PeerB talks with PeerC
        cls.talksWith(cls.hashgraph_peerC, cls.hashgraph_peerB, cls.peerB)

        # PeerC talks with PeerA
        cls.talksWith(cls.hashgraph_peerA, cls.hashgraph_peerC, cls.peerC)

        # PeerA talks with PeerD
        cls.talksWith(cls.hashgraph_peerD, cls.hashgraph_peerA, cls.peerA)

        # PeerD talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerD, cls.peerD)

        # PeerB talks with PeerC
        cls.talksWith(cls.hashgraph_peerC, cls.hashgraph_peerB, cls.peerB)

        # PeerA talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerA, cls.peerA)

        # PeerB talks with PeerC
        cls.talksWith(cls.hashgraph_peerC, cls.hashgraph_peerB, cls.peerB)

        # PeerC talks with PeerA
        cls.talksWith(cls.hashgraph_peerA, cls.hashgraph_peerC, cls.peerC)

        # PeerA talks with PeerD
        cls.talksWith(cls.hashgraph_peerD, cls.hashgraph_peerA, cls.peerA)

        # PeerD talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerD, cls.peerD)

        # PeerB talks with PeerC
        cls.talksWith(cls.hashgraph_peerC, cls.hashgraph_peerB, cls.peerB)

        # PeerA talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerA, cls.peerA)

        # PeerB talks with PeerC
        cls.talksWith(cls.hashgraph_peerC, cls.hashgraph_peerB, cls.peerB)

        # PeerC talks with PeerA
        cls.talksWith(cls.hashgraph_peerA, cls.hashgraph_peerC, cls.peerC)

        # PeerA talks with PeerD
        cls.talksWith(cls.hashgraph_peerD, cls.hashgraph_peerA, cls.peerA)

        # PeerD talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerD, cls.peerD)

        # PeerB talks with PeerC
        cls.talksWith(cls.hashgraph_peerC, cls.hashgraph_peerB, cls.peerB)

        # PeerA talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerA, cls.peerA)

        # PeerB talks with PeerC
        cls.talksWith(cls.hashgraph_peerC, cls.hashgraph_peerB, cls.peerB)

        # PeerC talks with PeerA
        cls.talksWith(cls.hashgraph_peerA, cls.hashgraph_peerC, cls.peerC)

        # PeerA talks with PeerD
        cls.talksWith(cls.hashgraph_peerD, cls.hashgraph_peerA, cls.peerA)

        # PeerD talks with PeerB
        cls.talksWith(cls.hashgraph_peerB, cls.hashgraph_peerD, cls.peerD)

        # PeerB talks with PeerC
        cls.talksWith(cls.hashgraph_peerC, cls.hashgraph_peerB, cls.peerB)

    @classmethod
    def talksWith(cls, selfHashGraph: Hashgraph, otherHashgraph: Hashgraph, otherPeer: Peer):
        print('Peer ' + otherPeer.deviceId + ' talks with' + selfHashGraph.myPeer.deviceId)
        deserializedOtherStore: Store = StoreJSONDecoder().decode(otherHashgraph.store.toJson())
        selfHashGraph.getNewOtherRounds(deserializedOtherStore)
        selfHashGraph.getNewOtherUndeterminedEvents(deserializedOtherStore)
        selfHashGraph.createEvent(otherPeer, cls.transactions)

    def testPeerSeesOK(self):
        self.assertFalse(self.hashgraph_peerC.see(
            self.hashgraph_peerC.store.getEventFromPeerAndCreatorIndex("B", 1),
            self.hashgraph_peerC.store.getEventFromPeerAndCreatorIndex("A", 1)
        ))

        self.assertFalse(self.hashgraph_peerC.see(
            self.hashgraph_peerC.store.getEventFromPeerAndCreatorIndex("D", 4),
            self.hashgraph_peerC.store.getEventFromPeerAndCreatorIndex("C", 1)
        ))

        self.assertTrue(self.hashgraph_peerC.see(
            self.hashgraph_peerC.store.getEventFromPeerAndCreatorIndex("D", 9),
            self.hashgraph_peerC.store.getEventFromPeerAndCreatorIndex("A", 5)
        ))

    def testPeerStronglySeesOK(self):
        self.assertTrue(
            self.hashgraph_peerC.stronglySee(
                self.hashgraph_peerC.store.getEventFromPeerAndCreatorIndex("C", 2),
                self.hashgraph_peerC.store.getEventFromPeerAndCreatorIndex("B", 0)
            )
        )

        self.assertFalse(
            self.hashgraph_peerC.stronglySee(
                self.hashgraph_peerC.store.getEventFromPeerAndCreatorIndex("B", 5),
                self.hashgraph_peerC.store.getEventFromPeerAndCreatorIndex("A", 2)
            )
        )

    def testEncodeDecodeOK(self):
        toJson = self.hashgraph_peerA.store.toJson()
        decodedStore = StoreJSONDecoder().decode(toJson)
        self.assertTrue(toJson == decodedStore.toJson())


if __name__ == '__main__':
    unittest.main()
