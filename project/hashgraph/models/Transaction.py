from project.hashgraph.helpers.Hash import Hash
from project.hashgraph.helpers.DatetimeHelper import DatetimeHelper


class Transaction:

    def __init__(self, goalPeerDeviceId: str):
        self.key: str = None
        self.goalPeerDeviceId: str = goalPeerDeviceId
        self.creationTime: int = 0

    def setKey(self):
        self.key = Hash.stringToHash(self.goalPeerDeviceId + str(self.creationTime))

    def setCreationTimeAtNow(self):
        self.creationTime = DatetimeHelper.getNowTimestamp()
