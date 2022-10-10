from enum import Enum


class TransactionStatus(str, Enum):
    READY = 'READY'
    RUNNING = 'RUNNING'
    COMPLETED = 'COMPLETED'
