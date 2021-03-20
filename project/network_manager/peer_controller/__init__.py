from database_manager import DatabaseManager
from peer import PeerStatus, Peer


class PeerController:

    #database_manager = DatabaseManager(Peer.DB_NAME)
    database_manager = Peer.database_manager

    @staticmethod
    def getPeers(peerStatus = None):

        if peerStatus is not None:
            if isinstance(peerStatus, PeerStatus) is False:
                raise Exception(peerStatus + ' is not a valid PeerStatus value')

            return PeerController.database_manager.getObject('status', peerStatus.name)

        return PeerController.database_manager.getAll()
