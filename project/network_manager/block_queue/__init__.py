from threading import Thread
from queue import Queue
from block import Block
from transaction import Transaction

class BlockQueue(Thread):
    queue = Queue()
    isWorkerRunning = False

    def __init__(self):
        # Call the Thread class's init function
        Thread.__init__(self)
        self.isWorkerRunning = True

    def run(self):
        #TODO Add try catch in order to not stopping loop
        print('Starting Block queue..')
        while self.isWorkerRunning is True:
            block = Block(self.queue.get())
            block.save()
            
            print(('New block saved! (Round created: ' + str(block.roundCreated) + ')'))

            for event in block.events:
                #Check if transaction list is empty
                if not event["transactions"]:
                    continue

                transaction = Transaction(event["transactions"][0])
                transaction.save()

            self.queue.task_done()

    def putBlock(self, blockData):
        self.queue.put(blockData)

    def stop(self):
        self.isWorkerRunning = False
