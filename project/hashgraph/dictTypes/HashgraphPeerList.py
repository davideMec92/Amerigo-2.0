from typing import TypedDict

from project.hashgraph.models.Peer import Peer


class HashgraphPeerList(TypedDict):
    peerDeviceId: str
    peer: Peer
