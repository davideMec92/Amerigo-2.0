from __future__ import annotations

import json
from json import JSONEncoder
from typing import Dict, TYPE_CHECKING

from project.hashgraph.helpers.models.JSONEncoders.StoreJSONEncoder import StoreJSONEncoder

if TYPE_CHECKING:
    from project.hashgraph.models.communication.CommunicationMessageHashgraph import CommunicationMessageHashgraph


class CommunicationMessageHashgraphJSONEncoder(json.JSONEncoder):

    def default(self, communicationMessageHashgraph: CommunicationMessageHashgraph) -> Dict:
        jsonEncoder = JSONEncoder()
        jsonEncoder.sort_keys = True
        jsonEncoder.indent = 4
        return {'type': communicationMessageHashgraph.type,
                    'store': StoreJSONEncoder().default(communicationMessageHashgraph.store),
                    'peer': communicationMessageHashgraph.peer.toDict()}