from __future__ import annotations

import json
from json import JSONEncoder
from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from project.hashgraph.models.EventBody import EventBody


class EventBodyJSONEncoder(json.JSONEncoder):

    def default(self, eventBody: EventBody) -> Dict:
        jsonEncoder = JSONEncoder()
        # jsonEncoder.sort_keys = True
        # jsonEncoder.indent = 4

        tempDict = {
            'creatorAssociation': eventBody.creatorAssociation.toDict() if eventBody.creatorAssociation is not None else None,
            'otherParent': eventBody.otherParent.toDict()  if eventBody.otherParent is not None else None,
            'otherParentHash': eventBody.otherParentHash  if eventBody.otherParentHash is not None else None,
            'selfParent': eventBody.selfParent.toDict()  if eventBody.selfParent is not None else None,
            'selfParentHash': eventBody.selfParentHash  if eventBody.selfParentHash is not None else None,
            'timestamp': eventBody.timestamp  if eventBody.timestamp is not None else None,
            'transactions': []
        }

        for transaction in eventBody.transactions:
            tempDict['transactions'].append(transaction.toDict())

        return tempDict