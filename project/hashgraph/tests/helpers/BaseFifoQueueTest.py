import unittest
from typing import List

from project.hashgraph.helpers.BaseFifoQueue import BaseFifoQueue
from project.hashgraph.models.Peer import Peer


class BaseFifoQueueTest(unittest.TestCase):
    peer1 = Peer()
    peer1.deviceId = 'Peer 1'
    peer2 = Peer()
    peer2.deviceId = 'Peer 2'
    peer3 = Peer()
    peer3.deviceId = 'Peer 3'

    def testIsEmptyOK(self):
        baseFifoQueue = BaseFifoQueue[Peer]()
        self.assertTrue(baseFifoQueue.size() == 0 and baseFifoQueue.isEmpty() is True)

    def testPutItemOK(self):
        baseFifoQueue = BaseFifoQueue[Peer]()
        baseFifoQueue.put(self.peer1)
        self.assertTrue(baseFifoQueue.size() == 1 and baseFifoQueue.isEmpty() is False)

    def testGetItemOK(self):
        baseFifoQueue = BaseFifoQueue[Peer]()
        baseFifoQueue.put(self.peer1)
        baseFifoQueue.get()
        self.assertTrue(baseFifoQueue.size() == 0 and baseFifoQueue.isEmpty() is True)

    def testPeekItemOK(self):
        baseFifoQueue = BaseFifoQueue[Peer]()
        baseFifoQueue.put(self.peer1)
        baseFifoQueue.peek()
        self.assertTrue(baseFifoQueue.size() == 1 and baseFifoQueue.isEmpty() is False)

    def testFifoOK(self):
        baseFifoQueue = BaseFifoQueue[Peer]()
        baseFifoQueue.put(self.peer1)
        baseFifoQueue.put(self.peer2)
        baseFifoQueue.put(self.peer3)
        baseFifoQueue.peek()
        self.assertTrue(baseFifoQueue.peek().deviceId == 'Peer 1')
        baseFifoQueue.get()
        self.assertTrue(baseFifoQueue.peek().deviceId == 'Peer 2')
        baseFifoQueue.get()
        self.assertTrue(baseFifoQueue.peek().deviceId == 'Peer 3')


if __name__ == '__main__':
    unittest.main()
