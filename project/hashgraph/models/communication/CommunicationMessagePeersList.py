from __future__ import annotations
from typing import List

from project.hashgraph.enums.CommunicationMessageTypes import CommunicationMessageTypes
from project.hashgraph.models.Peer import Peer
from project.hashgraph.models.communication.CommunicationMessage import CommunicationMessage


class CommunicationMessagePeersList(CommunicationMessage):
    def __init__(self):
        super().__init__()
        self.type = CommunicationMessageTypes.PEERS_LIST
        self.peers: List[Peer] = []

    def createFromDict(self, entries: dict) -> CommunicationMessagePeersList:
        if entries['peers'] is None:
            raise Exception('"peers" property cannot be null')

        communicationMessagePeersList: CommunicationMessagePeersList = CommunicationMessagePeersList()

        for peerDict in entries['peers']:
            communicationMessagePeersList.peers.append(Peer().createFromDict(peerDict))

        return communicationMessagePeersList


