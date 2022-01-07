from __future__ import annotations
import json
from json import JSONEncoder
from typing import TYPE_CHECKING, List, Dict

from project.hashgraph.models.Event import Event
from project.hashgraph.models.EventBody import EventBody
from project.hashgraph.models.EventPeerAssociation import EventPeerAssociation

if TYPE_CHECKING:
    from project.hashgraph.models.Store import Store

TO_ENCODE_EVENT_PROPERTIES = ['roundCreated', 'isWitness', 'isFamous', 'isDecided', 'bodySignature', 'roundReceived', 'consensusTimestamp', 'consensusTimestamp', 'eventBody', 'lastAncestors', 'firstDiscendants', 'bodySignature']
TO_ENCODE_EVENTBODY_PROPERTIES = ['creatorAssociation', 'selfParentHash', 'otherParentHash', 'transactions',
                                  'selfParent', 'otherParent', 'timestamp']
TO_ENCODE_EVENTPEERASSOCIATION_PROPERTIES = ['peerDeviceId', 'eventCreatorIndex', 'key']
TO_ENCODE_ROUND_PROPERTIES = ['roundCreated', 'roundReceived', 'events', 'determinedEvents', 'inRoundDeterminedEvents', 'witnesses', 'decidedWitnesses', 'peersInRound', 'committed']


class StoreJSONEncoder(json.JSONEncoder):

    def default(self, store: Store) -> Dict:

        jsonEncoder = JSONEncoder()
        jsonEncoder.sort_keys = True
        jsonEncoder.indent = 4
        tempDict = {'events': {}, 'rounds': {}}

        for eventKey, event in store.events.items():
            tempDict['events'][eventKey] = self.buildClassObjectDict(event, TO_ENCODE_EVENT_PROPERTIES)
        for roundCreated, toEncodeRound in store.rounds.items():
            tempDict['rounds'][roundCreated] = self.buildClassObjectDict(toEncodeRound, TO_ENCODE_ROUND_PROPERTIES)

        return tempDict

    def buildClassObjectDict(self, object, toEncodeProperties: List[str]):
        toReturnObjectDict = {}
        for toAddObjectProperty in toEncodeProperties:
            if hasattr(object, toAddObjectProperty):
                objectAttribute = getattr(object, toAddObjectProperty)
                if isinstance(objectAttribute, Event):
                    toReturnObjectDict[toAddObjectProperty] = self.buildClassObjectDict(objectAttribute,
                                                                                        TO_ENCODE_EVENT_PROPERTIES)
                elif isinstance(objectAttribute, EventBody):
                    toReturnObjectDict[toAddObjectProperty] = self.buildClassObjectDict(objectAttribute,
                                                                                        TO_ENCODE_EVENTBODY_PROPERTIES)
                elif isinstance(objectAttribute, EventPeerAssociation):
                    toReturnObjectDict[toAddObjectProperty] = self.buildClassObjectDict(objectAttribute,
                                                                                        TO_ENCODE_EVENTPEERASSOCIATION_PROPERTIES)
                else:
                    if isinstance(objectAttribute, dict):
                        if bool(objectAttribute) is False:
                            continue
                    elif objectAttribute is None:
                        continue
                    """elif isinstance(objectAttribute, list):
                        if len(objectAttribute) == 0:
                            continue"""

                    toReturnObjectDict[toAddObjectProperty] = objectAttribute

        return toReturnObjectDict
