from cryptography.fernet import Fernet
from aenum import Enum
from schema import Schema, And, Use, Optional, SchemaError
import json, ast


class CommunicationMessageTypes(Enum):
    LOGIN = 0
    PEERS_LIST = 1
    INFO = 2

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

    PEERS_LIST_SCHEMA = Schema({
        'type': str,
        'peers': [
            {
                "status": str,
                "updatedTime": str,
                "deviceId": str,
                "ipAddress": str
            }
        ]
    })

    CommunicationMeesageTypesSchemaAssoc = {CommunicationMessageTypes.LOGIN.name:LOGIN_CONF_SCHEMA,CommunicationMessageTypes.PEERS_LIST.name:PEERS_LIST_SCHEMA,CommunicationMessageTypes.INFO.name:INFO_MESSAGE_CONF_SCHEMA}

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

        #Message decrypt
        if decrypt is True:
            message = self.fernet_crypt.decrypt(message)

        if isinstance(message, dict) is False:
            message = json.loads(message)

        #Message validation
        if self.check(self.CommunicationMeesageTypesSchemaAssoc[message['type']],message) is False:
            raise Exception('Login data validation failed')

        return message

    def setMessage(self, message, encrypt = True):
        if message is None:
            raise Exception('Message cannot be null')

        if isinstance(message, dict) is False:
            message = json.loads(message)

        #Message validation
        self.check(self.CommunicationMeesageTypesSchemaAssoc[message['type']],message)

        message = json.dumps(message)

        return self.fernet_crypt.encrypt(message) if encrypt is True else message

    @staticmethod
    def check(conf_schema, conf):
        try:
            conf = ast.literal_eval(json.dumps(conf))
            conf_schema.validate(conf)
            return True
        except SchemaError, e:
            print 'Schema validation error:' + str(e)
            return False
