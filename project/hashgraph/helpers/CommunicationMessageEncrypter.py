import os

from project.Logger.Logger import LogLevels, Logger  # type: ignore
from project.hashgraph.enums.CommunicationMessageTypes import CommunicationMessageTypes  # type: ignore
from project.hashgraph.models.communication.CommunicationMessage import CommunicationMessage  # type: ignore
from cryptography.fernet import Fernet
from dotenv import load_dotenv

from project.hashgraph.validators.communicationMessage.CommunicationMessageSchemaValidator import CommunicationMessageSchemaValidator # type: ignore

load_dotenv()


class CommunicationMessageEncrypter:
    fernet_crypt = Fernet(os.getenv('ENCRYPTION_KEY'))

    @staticmethod
    def encrypt(communicationMessage: CommunicationMessage) -> str | None:
        if communicationMessage is None:
            raise Exception('Message parameter cannot be empty')

        messageToJson: str = communicationMessage.toJson()

        try:

            if communicationMessage.type != CommunicationMessageTypes.BLOCK and communicationMessage.type != CommunicationMessageTypes.HASHGRAPH:
                if CommunicationMessageSchemaValidator.validate(messageToJson) is False:
                    raise Exception('Message submitted is not valid')

            if type(messageToJson) is str:
                messageToJson = str.encode(messageToJson)

            encryptedMessage = CommunicationMessageEncrypter.fernet_crypt.encrypt(messageToJson).decode('utf-8')
            Logger.createLog(LogLevels.DEBUG, __file__, 'Generated encrypted message: ' + str(encryptedMessage))
            return encryptedMessage
        except Exception as e:
            Logger.createLog(LogLevels.ERROR, __file__, 'Communication encryption error: ' + str(e))
            return None
