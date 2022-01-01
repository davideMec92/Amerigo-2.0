import copy

from project.hashgraph.EventBody import EventBody
from project.hashgraph.dictTypes import LastAncestor
from project.hashgraph.dictTypes.FamousVote import FamousVote
from project.hashgraph.dictTypes.FisrtDescendant import FirstDiscendant
from project.hashgraph.helpers.Hash import Hash


class Event:
    roundCreated: int = -1
    isWitness: bool = False
    isFamous: bool = False
    isDecided: bool = False
    roundReceived: int = -1
    consensusTimestamp: float
    famousVote: FamousVote
    eventBody: EventBody
    lastAncestors: LastAncestor
    firstDiscendants: FirstDiscendant
    bodySignature: str

    def __init__(self, eventBody: EventBody):
        self.eventBody = eventBody
        # TODO ADD TO JSON METHOD
        self.bodySignature = Hash.stringToHash(eventBody.toJson())

    def copyLastAncestors(self, lastAncestors: LastAncestor):
        self.lastAncestors = copy.deepcopy(lastAncestors)

    def addLastAncestor(self, peerDeviceId: str, creatorIndex: int):
        self.lastAncestors[peerDeviceId] = creatorIndex

    def addFirstDiscendant(self, peerDeviceId: str, creatorIndex: int):
        self.firstDiscendants[peerDeviceId] = creatorIndex
