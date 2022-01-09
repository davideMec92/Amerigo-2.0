from project.hashgraph.enums.CommunicationMessageTypes import CommunicationMessageTypes  # type: ignore
from project.hashgraph.interfaces.JsonPrintable import JsonPrintable


class CommunicationMessage(JsonPrintable):
    type: CommunicationMessageTypes = None

