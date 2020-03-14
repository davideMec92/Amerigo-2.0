# -*- coding: utf-8 -*-

#from bluetooth_discoverer import BluetoothDiscoverer

from threading import Thread

class ThreadA( Thread ):

    status = 'STOPPED'

    queue = None

    def __init__(self, queue):

        self.queue = queue

        Thread.__init__(self)
        self.deamon = True
        self.start()
        self.status = 'STARTED'
        print('ThreadA started')

    def run(self):

        while self.status != 'STOPPED':

            data = self.queue.get()

            if data is not None:
                print('Ricevuti dati: ' + str(data))

            print('ThreadA run..')

        self.stop()

    def stop(self):

        self.status = 'STOPPED'
