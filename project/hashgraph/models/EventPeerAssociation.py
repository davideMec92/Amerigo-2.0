from project.hashgraph.helpers.Hash import Hash


class EventPeerAssociation:

    peerDeviceId: str
    eventCreatorIndex: int
    key: str

    def __init__(self, peerDeviceId: str, eventCreatorIndex: int):
        self.peerDeviceId = peerDeviceId
        self.eventCreatorIndex = eventCreatorIndex
        self.key = Hash.stringToHash(self.peerDeviceId + str(self.eventCreatorIndex))
