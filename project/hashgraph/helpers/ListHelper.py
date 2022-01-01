from typing import List


class ListHelper:

    @staticmethod
    def getListDiff(a: List[str], b: List[str]):
        return [x for x in b if x not in a]
