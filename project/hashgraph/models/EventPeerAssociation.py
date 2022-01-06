from project.hashgraph.helpers.Hash import Hash


class EventPeerAssociation:
    def __init__(self, peerDeviceId: str, eventCreatorIndex: int):
        self.peerDeviceId: str = peerDeviceId
        self.eventCreatorIndex: int = eventCreatorIndex
        self.key: str = Hash.stringToHash(self.peerDeviceId + str(self.eventCreatorIndex))
