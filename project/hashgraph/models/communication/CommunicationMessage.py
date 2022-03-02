from __future__ import annotations
from project.hashgraph.enums.CommunicationMessageTypes import CommunicationMessageTypes  # type: ignore
from project.hashgraph.helpers.CommunicationMessageEncrypter import CommunicationMessageEncrypter
from project.hashgraph.interfaces.JsonPrintable import JsonPrintable


class CommunicationMessage(JsonPrintable):
    type: CommunicationMessageTypes = None

    def encrypt(self) -> str:
        return CommunicationMessageEncrypter.encrypt(self)

    def createFromDict(self, entries: dict) -> CommunicationMessage:
        self.__dict__.update(entries)
        return self
