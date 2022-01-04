import os

from cryptography.fernet import Fernet
from dotenv import load_dotenv

from project.Logger.Logger import Logger, LogLevels

load_dotenv()

class CommunicationMessageDecrypter:
    fernet_crypt = Fernet(os.getenv('ENCRYPTION_KEY'))

    @staticmethod
    def decrypt(message: str) -> str | None:

        if message is None:
            raise Exception('Message parameter cannot be empty')

        try:
            if type(message) is str:
                message = str.encode(message)
            return CommunicationMessageDecrypter.fernet_crypt.decrypt(message).decode('utf-8')
        except Exception as e:
            Logger.createLog(LogLevels.ERROR, __file__, 'Communication encryption error: ' + str(e))
            return None
