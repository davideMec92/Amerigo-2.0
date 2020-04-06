# -*- coding: utf-8 -*-

#from bluetooth_discoverer import BluetoothDiscoverer

from threading import Thread

import time

class EnvironmentManager( Thread ):

    #bluetooth_server_rssi_streght = None
    #bluetooth_discoverer = None

    #Stati Thread
    STOPPED = 0
    RUNNING = 1

    status = STOPPED

    #Coda ProximityManager
    proximity_manager_queue = None

    #Coda RouteManager
    route_manager_queue = None

    lock = None

    def __init__(self, proximity_manager_queue, route_manager_queue, lock):

        self.proximity_manager_queue = proximity_manager_queue
        self.route_manager_queue = route_manager_queue
        self.lock = lock

        Thread.__init__(self)
        self.status = self.RUNNING
        self.name = self.__class__.__name__
        self.start()
        #self.bluetooth_discoverer = BluetoothDiscoverer()

    def run(self):
        while self.status != self.STOPPED:
            time.sleep(0.05)

            try:

                if self.proximity_manager_queue.full() is not True:
                    print('Start proximity check..')
                    self.proximity_manager_queue.put('START')

                if self.route_manager_queue.full() is not True:
                    print('Start route manager check..')
                    self.route_manager_queue.put('START')

            except Exception, e:
                print('Exception: ' + str(e))
                self.stop()

            #self.bluetooth_discoverer.startInquiring(self)

    """def setBluetoothServerRssiStrength(self, value):
        print('SET BLUETOOTH SERVER RSSI STRENGTH TO: ' + str( value ))
        self.bluetooth_server_rssi_streght = value"""

    def stop(self):
        self.status = self.STOPPED
        print('Stopping EnvironmentManager..')

        """if self.proximity_manager is not None:
            self.proximity_manager.stop()

        if self.route_manager is not None:
            self.route_manager.stop()

        if self.configurator is not None:
            self.configurator.gpioCleanup()"""
