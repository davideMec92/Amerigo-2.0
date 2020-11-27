from cryptography.fernet import Fernet
from aenum import Enum
from schema import Schema, And, Use, Optional, SchemaError
import json, ast


class CommunicationMessageTypes(Enum):
    LOGIN = 0
    PEER_ACCESS = 1

class CommunicationMessage:

    ENCRYPTION_KEY = 'Jli5assvwZKQBWxm0n3DYPqT27wWrpqcjWyOcXNUSAQ='

    LOGIN_CONF_SCHEMA = Schema({
        'type': str,
        'authToken': str,
        'macAddress':str
    })

    PEER_ACCESS_SCHEMA = Schema({
        'type': str,
        'secretToken': str,
        'peers': [
            {
                "status": str,
                "updatedTime": str,
                "bluetooth_mac": str,
                "ip_address": str,
                "id": str
            }
        ]
    })

    type = None
    message = None
    out_time = None
    in_time = None
    fernet_crypt = None

    def __init__(self):
        self.fernet_crypt = Fernet(self.ENCRYPTION_KEY)

    def getMessage(self, message, decrypt = True):
        if(message is None):
            raise Exception('Message cannot be null')
        return self.fernet_crypt.decrypt(message) if decrypt is True else message

    def setMessage(self, message, encrypt = True):
        if(message is None):
            raise Exception('Message cannot be null')
        return self.fernet_crypt.encrypt(message) if encrypt is True else message

    @staticmethod
    def check(conf_schema, conf):
        try:
            conf = ast.literal_eval(json.dumps(conf))
            conf_schema.validate(conf)
            return True
        except SchemaError, e:
            print str(e)
            return False
