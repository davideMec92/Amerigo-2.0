from typing import List

from tinydb.table import Document

from project.hashgraph.models.Peer import Peer


class PeerController:

    @staticmethod
    def getAll() -> List[Peer]:
        peers: List[Peer] = []
        dbPeers: List[Document] = Peer.tinyDBService.db.all()

        if len(dbPeers) > 0:
            for dbPeer in dbPeers:
                peers.append(Peer().createFromDict(dbPeer))

        return peers

    @staticmethod
    def storeAll(peers: List[Peer]) -> None:
        Peer.tinyDBService.db.drop_tables()
        for peer in peers:
            peer.save()
