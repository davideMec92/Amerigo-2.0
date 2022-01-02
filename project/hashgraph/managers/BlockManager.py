from project.hashgraph.helpers.BaseFifoQueue import BaseFifoQueue
from project.hashgraph.models.Block import Block


class BlockManager:
    __instance = None
    isSendEnabled: bool = True


    def __init__(self):
        self.toCommitBlocks = BaseFifoQueue[Block]()

