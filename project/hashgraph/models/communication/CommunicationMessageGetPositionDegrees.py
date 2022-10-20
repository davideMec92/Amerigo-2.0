import os

from dotenv import load_dotenv
from project.hashgraph.enums.CommunicationMessageTypes import CommunicationMessageTypes
from project.hashgraph.models.communication.CommunicationMessage import CommunicationMessage

load_dotenv()

class CommunicationMessageGetPositionDegrees(CommunicationMessage):
    def __init__(self):
        super().__init__()
        self.type = CommunicationMessageTypes.POSITIONS_DEGREES_GET
        self.authToken = os.getenv('SERVER_AUTH_TOKEN')
