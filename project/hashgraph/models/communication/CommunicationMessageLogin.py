import os

from dotenv import load_dotenv

from project.hashgraph.enums.CommunicationMessageTypes import CommunicationMessageTypes
from project.hashgraph.models.communication.CommunicationMessage import CommunicationMessage

load_dotenv()


class CommunicationMessageLogin(CommunicationMessage):
    def __init__(self, deviceId: str):
        super().__init__()
        self.type = CommunicationMessageTypes.LOGIN
        self.deviceId = deviceId
        self.authToken = os.getenv('SERVER_AUTH_TOKEN')
