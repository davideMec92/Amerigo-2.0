from typing import TypedDict

from project.hashgraph.Event import Event


class StoreEvent(TypedDict):
    deviceID: str
    event: Event
