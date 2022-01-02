from collections import defaultdict
from typing import Dict

from project.hashgraph.TableVote import TableVote
from project.hashgraph.helpers.Hash import Hash


class VotesTable:
    table: Dict[str, TableVote] = defaultdict(set)

    def setVote(self, x: str, y: str, vote: bool):
        vote = TableVote(x, y, vote)
        self.table[Hash.stringToHash(x+y)] = vote

    def getVote(self, x: str, y: str) -> bool:
        tableVote = self.table.get(Hash.stringToHash(x+y))
        return tableVote.vote if tableVote is not None else None
