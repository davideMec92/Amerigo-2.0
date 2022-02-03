import json
from typing import Dict

from project.Logger.Logger import Logger, LogLevels
from project.hashgraph.enums.CommunicationMessageTypes import CommunicationMessageTypes
from project.hashgraph.helpers.models.JSONDecoders.StoreJSONDecoder import StoreJSONDecoder
from project.hashgraph.models.Peer import Peer
from project.hashgraph.models.communication.CommunicationMessageHashgraph import CommunicationMessageHashgraph

class CommunicationMessageHashgraphDeserializer:

    @staticmethod
    def deserialize(communicationMessageHashgraphJson: str) -> CommunicationMessageHashgraph:
        try:
            communicationMessageHashgraphDict: Dict = json.loads(communicationMessageHashgraphJson)
            communicationMessageHashgraph: CommunicationMessageHashgraph = CommunicationMessageHashgraph()
            communicationMessageHashgraph.store = StoreJSONDecoder().decode(json.dumps(communicationMessageHashgraphDict['store']))
            communicationMessageHashgraph.type = CommunicationMessageTypes[communicationMessageHashgraphDict['type']]
            communicationMessageHashgraph.peer = Peer().createFromDict(communicationMessageHashgraphDict['peer'])
            return communicationMessageHashgraph
        except Exception as e:
            Logger.createLog(LogLevels.ERROR, __file__, 'Error while deserializing: ' + str(e))
            return None
