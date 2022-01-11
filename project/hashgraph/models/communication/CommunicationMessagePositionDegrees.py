from typing import List

from project.hashgraph.enums.CommunicationMessageTypes import CommunicationMessageTypes
from project.hashgraph.models.PositionDegrees import PositionDegrees
from project.hashgraph.models.communication.CommunicationMessage import CommunicationMessage


class CommunicationMessagePositionDegrees(CommunicationMessage):
    def __init__(self, deviceId: str):
        super().__init__()
        self.type = CommunicationMessageTypes.POSITIONS_DEGREES
        self.deviceId = deviceId
        self.positions: List[PositionDegrees] = []
