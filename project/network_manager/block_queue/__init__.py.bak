from threading import Thread
from queue import Queue
from block import Block

class BlockQueue(Thread):
    queue = Queue()
    isWorkerRunning = False

    def __init__(self):
        # Call the Thread class's init function
        Thread.__init__(self)
        self.isWorkerRunning = True

    def run(self):
        print('Starting Block queue..')
        while self.isWorkerRunning is True:
            block = Block(self.queue.get())
            block.save()
            print ('New block saved! (Round created: ' + str(block.roundCreated) + ')')
            self.queue.task_done()

    def putBlock(self, blockData):
        self.queue.put(blockData)

    def stop(self):
        self.isWorkerRunning = False
