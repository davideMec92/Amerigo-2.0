from project.hashgraph.helpers.Hash import Hash
from project.hashgraph.tests.helpers.DatetimeHelper import DatetimeHelper


class Transaction:

    def __init__(self, goalPeerDeviceId: str):
        self.key: str | None = None
        self.goalPeerDeviceId: str = goalPeerDeviceId
        self.creationTime: int | None = None

    def setKey(self):
        self.key = Hash.stringToHash(self.goalPeerDeviceId + str(self.creationTime))

    def setCreationTimeAtNow(self):
        self.creationTime = DatetimeHelper.getNowTimestamp()
