import time


class Transaction:

    key: str
    goalPeerDeviceId: str
    creationTime: float

    def __init__(self, goalPeerDeviceId: str):
        self.goalPeerDeviceId = goalPeerDeviceId

    def setCreationTimeAtNow(self):
        self.creationTime = time.time()
