import unittest

from project.hashgraph.builders.CommunicationMessageBuilder import CommunicationMessageBuilder
from project.hashgraph.models.Peer import Peer
from project.hashgraph.models.Store import Store
from project.hashgraph.models.communication.CommunicationMessageACK import CommunicationMessageACK
from project.hashgraph.models.communication.CommunicationMessageHashgraph import CommunicationMessageHashgraph
from project.hashgraph.models.communication.CommunicationMessageNACK import CommunicationMessageNACK
from project.hashgraph.models.communication.CommunicationMessagePeersList import CommunicationMessagePeersList
from project.hashgraph.tests.helpers.models.communication.CommunicationMessageHashgraphDeserializerTest import \
    CommunicationMessageHashgraphDeserializerTest


class CommunicationMessageBuilderTest(unittest.TestCase):

    communicationMessagePeersList = """{
        "type": "PEERS_LIST",
        "peers": [
            {
                "deviceId": "DEVICE_ID_A",
                "address": "DEVICE_ADDRESS_A",
                "status": "CONNECTED",
                "creatorIndex": 1
            },{
                "deviceId": "DEVICE_ID_B",
                "address": "DEVICE_ADDRESS_B",
                "status": "DISCONNECTED",
                "creatorIndex": 2
            }
        ]
    }"""

    communicationMessageACK = """{
        "type": "ACK"
    }"""

    communicationMessageNACK = """{
        "type": "NACK"
    }"""

    def testCommunicationMessageHashgraphBuildOK(self):
        communicationMessageHashgraph: CommunicationMessageHashgraph = CommunicationMessageBuilder().build(CommunicationMessageHashgraphDeserializerTest.communicationMessageJSON)
        self.assertTrue(isinstance(communicationMessageHashgraph.peer, Peer))
        self.assertTrue(isinstance(communicationMessageHashgraph.store, Store))

    def testCommunicationMessagePeersListBuildOK(self):
        communicationMessagePeersList: CommunicationMessagePeersList = CommunicationMessageBuilder().build(self.communicationMessagePeersList)
        self.assertTrue(isinstance(communicationMessagePeersList.peers[0], Peer))

    def testCommunicationMessageACKOK(self):
        communicationMessageACK: CommunicationMessageACK = CommunicationMessageBuilder.build(self.communicationMessageACK)
        self.assertTrue(isinstance(communicationMessageACK, CommunicationMessageACK))

    def testCommunicationMessageNACKOK(self):
        communicationMessageNACK: CommunicationMessageNACK = CommunicationMessageBuilder.build(self.communicationMessageNACK)
        self.assertTrue(isinstance(communicationMessageNACK, CommunicationMessageNACK))

if __name__ == '__main__':
    unittest.main()
