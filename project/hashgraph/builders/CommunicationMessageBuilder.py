import json
from typing import Dict

from project.Logger.Logger import LogLevels, Logger
from project.hashgraph.enums.CommunicationMessageTypes import CommunicationMessageTypes
from project.hashgraph.helpers.models.Deserializers.communication.CommunicationMessageHashgraphDeserializer import \
    CommunicationMessageHashgraphDeserializer
from project.hashgraph.models.communication.CommunicationMessage import CommunicationMessage
from project.hashgraph.models.communication.CommunicationMessageACK import CommunicationMessageACK
from project.hashgraph.models.communication.CommunicationMessageNACK import CommunicationMessageNACK
from project.hashgraph.models.communication.CommunicationMessagePeersList import CommunicationMessagePeersList


class CommunicationMessageBuilder:

    @staticmethod
    def build(communicationMessage: str) -> CommunicationMessage:

        try:
            communicationMessageDict: Dict = json.loads(communicationMessage)

            if communicationMessageDict['type'] is None:
                raise Exception('Converted JSON string not contains "type" property')

            if communicationMessageDict['type'] == CommunicationMessageTypes.PEERS_LIST:
                return CommunicationMessagePeersList().createFromDict(communicationMessageDict)
            elif communicationMessageDict['type'] == CommunicationMessageTypes.HASHGRAPH:
                return CommunicationMessageHashgraphDeserializer.deserialize(communicationMessage)
            elif communicationMessageDict['type'] == CommunicationMessageTypes.ACK:
                return CommunicationMessageACK().createFromDict(communicationMessageDict)
            elif communicationMessageDict['type'] == CommunicationMessageTypes.NACK:
                return CommunicationMessageNACK().createFromDict(communicationMessageDict)
            else:
                return CommunicationMessage()

        except Exception as e:
            Logger.createLog(LogLevels.ERROR, __file__, 'Communication message build error: ' + str(e))
            return None
