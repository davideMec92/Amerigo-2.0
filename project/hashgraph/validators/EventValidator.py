from project.hashgraph.helpers.Hash import Hash
from project.hashgraph.models.EventBody import EventBody


class EventValidator:

    @staticmethod
    def validateEventBodyHash(bodySignature: str, eventBody: EventBody):
        if bodySignature != Hash.stringToHash(eventBody.toJson()):
            raise Exception('Invalid event body signature')
