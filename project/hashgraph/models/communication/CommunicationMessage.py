import json

from project.hashgraph.enums.CommunicationMessageTypes import CommunicationMessageTypes  # type: ignore


class CommunicationMessage:
    type: CommunicationMessageTypes = None

    def toJson(self) -> str:
        return json.dumps(self, default=vars)
