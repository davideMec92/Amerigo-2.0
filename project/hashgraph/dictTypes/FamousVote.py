from typing import TypedDict

from project.hashgraph.Event import Event


class FamousVote(TypedDict):
    event: Event
    isFamous: bool
