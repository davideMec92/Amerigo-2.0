import time

from project.hashgraph.helpers.Hash import Hash


class Transaction:

    key: str
    goalPeerDeviceId: str
    creationTime: float

    def __init__(self, goalPeerDeviceId: str):
        self.goalPeerDeviceId = goalPeerDeviceId

    def setKey(self):
        self.key = Hash.stringToHash(self.goalPeerDeviceId + str(self.creationTime))

    def setCreationTimeAtNow(self):
        self.creationTime = time.time()
