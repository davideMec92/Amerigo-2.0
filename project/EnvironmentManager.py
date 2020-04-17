# -*- coding: utf-8 -*-

from threading import Thread

import time

class EnvironmentManager( Thread ):

    #Stati Thread
    STOPPED = 0
    RUNNING = 1

    status = STOPPED

    #Coda RouteManager
    route_manager_queue = None

    lock = None

    def __init__(self, route_manager_queue, lock):

        self.route_manager_queue = route_manager_queue
        self.lock = lock

        Thread.__init__(self)
        self.status = self.RUNNING
        self.name = self.__class__.__name__
        self.start()

    def run(self):
        while self.status != self.STOPPED:
            time.sleep(0.05)

            try:

                if self.route_manager_queue.full() is not True:
                    print('Start route manager check..')
                    self.route_manager_queue.put('START')

            except Exception, e:
                print('Exception: ' + str(e))
                self.stop()

    def stop(self):
        self.status = self.STOPPED
        print('Stopping EnvironmentManager..')
