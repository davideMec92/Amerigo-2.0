import unittest

from project.hashgraph.helpers.FifoQueue import FifoQueue
from project.hashgraph.models.Peer import Peer


class FifoQueueTest(unittest.TestCase):
    peer1 = Peer()
    peer1.deviceId = 'Peer 1'
    peer2 = Peer()
    peer2.deviceId = 'Peer 2'
    peer3 = Peer()
    peer3.deviceId = 'Peer 3'

    def testIsEmptyOK(self):
        baseFifoQueue = FifoQueue[Peer]()
        self.assertTrue(baseFifoQueue.size() == 0 and baseFifoQueue.isEmpty() is True)

    def testPutItemOK(self):
        baseFifoQueue = FifoQueue[Peer]()
        baseFifoQueue.push(self.peer1)
        self.assertTrue(baseFifoQueue.size() == 1 and baseFifoQueue.isEmpty() is False)

    def testGetItemOK(self):
        fifoQueue = FifoQueue[Peer]()
        fifoQueue.push(self.peer1)
        fifoQueue.pop()
        self.assertTrue(fifoQueue.size() == 0 and fifoQueue.isEmpty() is True)

    def testPeekItemOK(self):
        baseFifoQueue = FifoQueue[Peer]()
        baseFifoQueue.push(self.peer1)
        baseFifoQueue.peek()
        self.assertTrue(baseFifoQueue.size() == 1 and baseFifoQueue.isEmpty() is False)

    def testFifoOK(self):
        baseFifoQueue = FifoQueue[Peer]()
        baseFifoQueue.push(self.peer1)
        baseFifoQueue.push(self.peer2)
        baseFifoQueue.push(self.peer3)
        baseFifoQueue.peek()
        self.assertTrue(baseFifoQueue.peek().deviceId == 'Peer 1')
        baseFifoQueue.pop()
        self.assertTrue(baseFifoQueue.peek().deviceId == 'Peer 2')
        baseFifoQueue.pop()
        self.assertTrue(baseFifoQueue.peek().deviceId == 'Peer 3')


if __name__ == '__main__':
    unittest.main()
