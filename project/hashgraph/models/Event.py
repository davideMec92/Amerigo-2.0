from __future__ import annotations

import copy
from typing import Dict

from project.hashgraph.dictTypes import LastAncestor
from project.hashgraph.helpers.Hash import Hash
from project.hashgraph.models.EventBody import EventBody


class Event:

    def __init__(self, eventBody: EventBody):
        self.roundCreated: int = -1
        self.isWitness: bool = False
        self.isFamous: bool = False
        self.isDecided: bool = False
        self.roundReceived: int = -1
        self.consensusTimestamp: int = 0
        self.famousVote: Dict[Event, bool] = {}
        self.eventBody: EventBody = eventBody
        """Dict[Peer device ID, Creator Index]"""
        self.lastAncestors: Dict[str, int] = {}
        self.firstDiscendants: Dict[str, int] = {}
        # TODO ADD TO JSON METHOD
        # self.bodySignature = Hash.stringToHash(eventBody.toJson())
        # ATTENTION FOR TEST ONLY !!!!!!!
        self.bodySignature: str = Hash.stringToHash('test body payload')

    def copyLastAncestors(self, lastAncestors: LastAncestor):
        self.lastAncestors = copy.deepcopy(lastAncestors)

    def addLastAncestor(self, peerDeviceId: str, creatorIndex: int):
        self.lastAncestors[peerDeviceId] = creatorIndex

    def addFirstDiscendant(self, peerDeviceId: str, creatorIndex: int):
        self.firstDiscendants[peerDeviceId] = creatorIndex
