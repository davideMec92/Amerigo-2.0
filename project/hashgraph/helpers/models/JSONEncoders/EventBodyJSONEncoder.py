from __future__ import annotations

import json
from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from project.hashgraph.models.EventBody import EventBody


class EventBodyJSONEncoder(json.JSONEncoder):

    def default(self, eventBody: EventBody) -> Dict:

        tempDict = {
            'creatorAssociation': eventBody.creatorAssociation.toDict() if eventBody.creatorAssociation is not None else None,
            'timestamp': eventBody.timestamp  if eventBody.timestamp is not None else None,
            'transactions': []
        }

        if eventBody.otherParent is not None:
            tempDict['otherParent'] = eventBody.otherParent.toDict()

        if eventBody.otherParentHash is not None:
            tempDict['otherParentHash'] = eventBody.otherParentHash

        if eventBody.selfParent is not None:
            tempDict['selfParent'] = eventBody.selfParent.toDict()

        if eventBody.selfParentHash is not None:
            tempDict['selfParentHash'] = eventBody.selfParentHash

        for transaction in eventBody.transactions:
            tempDict['transactions'].append({
            'creationTime': transaction.creationTime,
            'goalPeerDeviceId': transaction.goalPeerDeviceId,
            'key': transaction.key
        })

        return tempDict