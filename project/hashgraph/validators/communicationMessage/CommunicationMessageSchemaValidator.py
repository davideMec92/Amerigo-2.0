import ast
import json
import os.path

from schema import Schema, Optional, SchemaError

from project.Logger.Logger import Logger, LogLevels
from project.hashgraph.enums.CommunicationMessageTypes import CommunicationMessageTypes


class CommunicationMessageSchemaValidator:
    INFO_MESSAGE_CONF_SCHEMA = Schema({
        'type': str,
        'message': str
    })

    LOGIN_CONF_SCHEMA = Schema({
        'type': str,
        'authToken': str,
        'deviceId': str
    })

    POSITIONS_DEGREES_SCHEMA = Schema({
        'type': str,
        'deviceId': str,
        'positions': [
            {
                "deviceId": str,
                "degrees": int,
            }
        ]
    })

    PEERS_LIST_SCHEMA = Schema({
        'type': str,
        'peers': [
            {
                "status": str,
                "updatedTime": str,
                "deviceId": str,
                "address": str
            }
        ]
    })

    BLOCK_SCHEMA = Schema({
        'type': str,
        'block': {
            'roundCreated': int,
            'events': [
                {
                    "consensusTimestamp": int,
                    "transactions": [
                        {
                            "key": str,
                            "goalPeerDeviceId": str,
                            "creationTime": int,
                        }
                    ],
                    "creatorAssociation": {
                        "peerDeviceId": str,
                        "key": str,
                        "eventCreatorIndex": int
                    }
                }
            ]
        }

    })

    POSITIONS_DEGREES_GET_RESPONSE_SCHEMA = Schema({
        'type': str,
        'positionsDegrees': [
            {
                'deviceId': str,
                'positions': [
                    {
                        "deviceId": str,
                        "degrees": int,
                    }
                ]
            },
        ]
    })

    TRANSACTION_GET_SCHEMA = Schema({
        'type': str,
        'authToken': str,
        Optional('lastTransactionKey'): str
    })

    TRANSACTION_GET_RESPONSE_SCHEMA = Schema({
        'type': str,
        Optional('key'): str,
        Optional('goalPeerDeviceId'): str,
    })

    POSITIONS_DEGREES_GET_SCHEMA = Schema({
        'type': str,
        'authToken': str
    })

    ACK_MESSAGE_SCHEMA = Schema({
        'type': str
    })

    NACK_MESSAGE_SCHEMA = Schema({
        'type': str
    })

    CommunicationMessageTypesSchemaAssoc = {
        CommunicationMessageTypes.LOGIN.name: LOGIN_CONF_SCHEMA,
        CommunicationMessageTypes.PEERS_LIST.name: PEERS_LIST_SCHEMA,
        CommunicationMessageTypes.INFO.name: INFO_MESSAGE_CONF_SCHEMA,
        CommunicationMessageTypes.BLOCK.name: BLOCK_SCHEMA,
        CommunicationMessageTypes.POSITIONS_DEGREES.name: POSITIONS_DEGREES_SCHEMA,
        CommunicationMessageTypes.TRANSACTION_GET.name: TRANSACTION_GET_SCHEMA,
        CommunicationMessageTypes.POSITIONS_DEGREES_GET.name: POSITIONS_DEGREES_GET_SCHEMA,
        CommunicationMessageTypes.POSITIONS_DEGREES_GET_RESPONSE.name: POSITIONS_DEGREES_GET_RESPONSE_SCHEMA,
        CommunicationMessageTypes.TRANSACTION_GET_RESPONSE.name: TRANSACTION_GET_RESPONSE_SCHEMA,
        CommunicationMessageTypes.ACK.name: ACK_MESSAGE_SCHEMA,
        CommunicationMessageTypes.NACK.name: NACK_MESSAGE_SCHEMA,
    }

    @staticmethod
    def validate(message: str) -> bool:
        try:
            if message is None:
                raise Exception('Message cannot be null')

            if isinstance(message, dict) is False:
                message = json.loads(message)

            if message['type'] not in CommunicationMessageSchemaValidator.CommunicationMessageTypesSchemaAssoc:
                raise Exception('Validation schema not found for type message: ' + str(message['type']))

            conf = ast.literal_eval(json.dumps(message))
            CommunicationMessageSchemaValidator.CommunicationMessageTypesSchemaAssoc[message['type']].validate(conf)
            Logger.createLog(LogLevels.DEBUG, __file__, 'Successfully validated message type: ' + str(message['type']))
            return True
        except SchemaError as e:
            Logger.createLog(LogLevels.ERROR, __file__, 'Schema validation error: ' + str(e))
            return False
