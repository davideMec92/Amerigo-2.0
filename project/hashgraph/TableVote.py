class TableVote:
    x: str
    y: str
    vote: bool

    def __init__(self, x: str, y: str, vote: bool):
        self.x = x
        self.y = y
        self.vote = vote
