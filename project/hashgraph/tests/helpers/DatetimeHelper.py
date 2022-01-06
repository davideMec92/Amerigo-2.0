import time


class DatetimeHelper:

    @staticmethod
    def getNowTimestamp() -> int:
        return int(time.time())