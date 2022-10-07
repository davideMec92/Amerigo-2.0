from typing import Dict

from project.hashgraph.helpers.Hash import Hash
from project.hashgraph.interfaces.JsonPrintable import JsonPrintable


class EventPeerAssociation(JsonPrintable):
    def __init__(self, peerDeviceId: str, eventCreatorIndex: int):
        self.peerDeviceId: str = peerDeviceId
        self.eventCreatorIndex: int = eventCreatorIndex
        self.key: str = Hash.stringToHash(self.peerDeviceId + str(self.eventCreatorIndex))

    def toDict(self) -> Dict:
        return {
            'peerDeviceId': self.peerDeviceId,
            'eventCreatorIndex': self.eventCreatorIndex,
            'key': self.key
        }
