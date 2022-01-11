from project.hashgraph.interfaces.JsonPrintable import JsonPrintable


class PositionDegrees(JsonPrintable):

    def __init__(self, deviceId: str, degrees: int):
        self.deviceId = deviceId
        self.degrees = degrees