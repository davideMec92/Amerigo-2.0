from enum import Enum


class PeerStatus(Enum):
    CONNECTED = 0
    WARNING = 1
    DISCONNECTED = 2
