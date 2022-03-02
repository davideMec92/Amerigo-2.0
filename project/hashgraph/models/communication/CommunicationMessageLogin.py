import os
from typing import Optional

from dotenv import load_dotenv

from project.hashgraph.enums.CommunicationMessageTypes import CommunicationMessageTypes
from project.hashgraph.models.communication.CommunicationMessage import CommunicationMessage

load_dotenv()


class CommunicationMessageLogin(CommunicationMessage):
    def __init__(self, deviceId: Optional[str] = None):
        super().__init__()
        self.type = CommunicationMessageTypes.LOGIN
        self.deviceId = deviceId
        self.authToken = os.getenv('SERVER_AUTH_TOKEN')

    def toJson(self) -> str:
        if self.deviceId is None:
            raise Exception('Property "deviceId" cannot be null')
        return super().toJson()

    def toPrettyJson(self) -> str:
        if self.deviceId is None:
            raise Exception('Property "deviceId" cannot be null')
        return super().toPrettyJson()



