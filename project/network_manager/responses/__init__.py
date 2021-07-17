from communication_message import CommunicationMessageTypes


class PositionsDegreesGetResponse:

    baseSchema = {
        'type': CommunicationMessageTypes.POSITIONS_DEGREES_GET_RESPONSE.name,
        'positionsDegrees': []
    }

    def build(self, responseData):
        print('responseData: ' + str(responseData))

        for positionDegrees in responseData:
            tempPositionDegrees = {
                'deviceId': positionDegrees['deviceId'],
                'positions': positionDegrees['positions']
            }

            self.baseSchema['positionsDegrees'].append(tempPositionDegrees)

        return self.baseSchema


