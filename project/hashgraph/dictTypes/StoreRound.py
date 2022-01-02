from __future__ import annotations
from typing import TYPE_CHECKING
from typing import TypedDict

if TYPE_CHECKING:
    from project.hashgraph.Round import Round


class StoreRound(TypedDict):
    roundCreated: int
    round: Round
