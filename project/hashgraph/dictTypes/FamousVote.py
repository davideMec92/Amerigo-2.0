from __future__ import annotations
from typing import TypedDict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from project.hashgraph.Event import Event


class FamousVote(TypedDict):
    event: Event
    isFamous: bool
