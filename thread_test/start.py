from thread_a import ThreadA
from thread_b import ThreadB

from multiprocessing import Queue
import time

a_queue = Queue()
b_queue = Queue()

print('ThreadA init..')
threadA = ThreadA( a_queue )
print('ThreadB init..')
threadB = ThreadB( b_queue )

a_queue.put('CIAO THREAD A..')
a_queue.put('CIAO THREAD B..')
print('Sleep..')
time.sleep(2)

a_queue.put('ARRIVEDERCI THREAD A..')
a_queue.put('ARRIVEDERCI THREAD B..')

raw_input("Press Enter to stop...")
print('ThreadA stop..')
threadA.stop()
print('ThreadB stop..')
threadB.stop()
