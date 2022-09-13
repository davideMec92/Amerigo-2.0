from __future__ import annotations

import json

from project.hashgraph.enums.CommunicationMessageTypes import CommunicationMessageTypes
from project.hashgraph.helpers.models.JSONEncoders.CommunicationMessageHashgraphJSONEncoder import \
    CommunicationMessageHashgraphJSONEncoder
from project.hashgraph.models.Hashgraph import Hashgraph
from project.hashgraph.models.Peer import Peer
from project.hashgraph.models.Store import Store
from project.hashgraph.models.communication.CommunicationMessage import CommunicationMessage


class CommunicationMessageHashgraph(CommunicationMessage):

    def __init__(self):
        super().__init__()
        self.type = CommunicationMessageTypes.HASHGRAPH
        self.store: Store = None
        self.peer: Peer = None

    @staticmethod
    def createFromHashgraph(hashgraph: Hashgraph) -> CommunicationMessageHashgraph:
        communicationMessageHashgraph: CommunicationMessageHashgraph = CommunicationMessageHashgraph()
        communicationMessageHashgraph.type = CommunicationMessageTypes.HASHGRAPH
        communicationMessageHashgraph.store: Store = hashgraph.store
        communicationMessageHashgraph.peer: Peer = hashgraph.myPeer
        return communicationMessageHashgraph

    def toJson(self) -> str:
        return json.dumps(self, cls=CommunicationMessageHashgraphJSONEncoder)

    def toPrettyJson(self) -> str:
        return json.dumps(self, cls=CommunicationMessageHashgraphJSONEncoder, sort_keys=True, separators=(',', ':'))
