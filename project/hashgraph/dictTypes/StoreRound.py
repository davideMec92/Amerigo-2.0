from typing import TypedDict

from project.hashgraph.Round import Round


class StoreRound(TypedDict):
    roundCreated: int
    round: Round
