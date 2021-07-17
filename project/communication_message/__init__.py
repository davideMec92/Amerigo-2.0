from cryptography.fernet import Fernet
from aenum import Enum
from schema import Schema, And, Use, Optional, SchemaError
import json, ast


class CommunicationMessageTypes(Enum):
    LOGIN = 0
    PEERS_LIST = 1
    INFO = 2
    HASHGRAPH = 3,
    BLOCK = 4,
    POSITIONS_DEGREES = 5,
    TRANSACTION_GET = 6,
    POSITIONS_DEGREES_GET = 7,
    POSITIONS_DEGREES_GET_RESPONSE = 8,

class CommunicationMessage:

    ENCRYPTION_KEY = 'Jli5assvwZKQBWxm0n3DYPqT27wWrpqcjWyOcXNUSAQ='

    INFO_MESSAGE_CONF_SCHEMA = Schema({
        'type': str,
        'message': str
    })

    LOGIN_CONF_SCHEMA = Schema({
        'type': str,
        'authToken': str,
        'deviceId':str
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

    #TODO UNDERSTAND HOW TO MANAGE START POINT DEVICE ID
    TRANSACTION_GET_SCHEMA = Schema({
        'type': str,
        'authToken': str,
        'lastGoalDeviceId': str
    })

    POSITIONS_DEGREES_GET_SCHEMA = Schema({
        'type': str,
        'authToken': str
    })

    CommunicationMessageTypesSchemaAssoc = {
        CommunicationMessageTypes.LOGIN.name:LOGIN_CONF_SCHEMA,
        CommunicationMessageTypes.PEERS_LIST.name:PEERS_LIST_SCHEMA,
        CommunicationMessageTypes.INFO.name:INFO_MESSAGE_CONF_SCHEMA,
        CommunicationMessageTypes.BLOCK.name:BLOCK_SCHEMA,
        CommunicationMessageTypes.POSITIONS_DEGREES.name:POSITIONS_DEGREES_SCHEMA,
        CommunicationMessageTypes.TRANSACTION_GET.name:TRANSACTION_GET_SCHEMA,
        CommunicationMessageTypes.POSITIONS_DEGREES_GET.name:POSITIONS_DEGREES_GET_SCHEMA,
        CommunicationMessageTypes.POSITIONS_DEGREES_GET_RESPONSE.name:POSITIONS_DEGREES_GET_RESPONSE_SCHEMA,
    }

    type = None
    message = None
    out_time = None
    in_time = None
    fernet_crypt = None

    def __init__(self):
        self.fernet_crypt = Fernet(self.ENCRYPTION_KEY)

    def getMessage(self, message, decrypt = True):
        if message is None:
            raise Exception('Message cannot be null')

        if type(message) is str:
            message = str.encode(message)

        #Message decrypt
        if decrypt is True:
            message = self.fernet_crypt.decrypt(message)

        if isinstance(message, dict) is False:
            message = json.loads(message)

        #Message validation
        if self.check(self.CommunicationMessageTypesSchemaAssoc[message['type']],message) is False:
            raise Exception('Login data validation failed')

        return message

    def setMessage(self, message, encrypt = True):
        if message is None:
            raise Exception('Message cannot be null')

        if isinstance(message, dict) is False:
            message = json.loads(message)

        #Message validation
        self.check(self.CommunicationMessageTypesSchemaAssoc[message['type']],message)

        message = json.dumps(message)

        if type(message) is str:
            message = str.encode(message)

        return self.fernet_crypt.encrypt(message) if encrypt is True else message

    @staticmethod
    def check(conf_schema, conf):
        try:
            conf = ast.literal_eval(json.dumps(conf))
            conf_schema.validate(conf)
            return True
        except SchemaError as e:
            print(('Schema validation error:' + str(e)))
            return False
