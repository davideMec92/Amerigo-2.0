from typing import TypedDict

from project.hashgraph.models.Event import Event


class StoreEvent(TypedDict):
    deviceID: str
    event: Event
