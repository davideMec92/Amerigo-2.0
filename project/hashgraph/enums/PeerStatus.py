from enum import Enum


class PeerStatus(str, Enum):
    CONNECTED = 'CONNECTED'
    WARNING = 'WARNING'
    DISCONNECTED = 'DISCONNECTED'
