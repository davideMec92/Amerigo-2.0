# -*- coding: utf-8 -*-

#from bluetooth_discoverer import BluetoothDiscoverer

from threading import Thread

from configurator import Configurator
from ProximityManager import ProximityManager
from RouteManager import RouteManager
from compass import Compass
from motors import Motors

import time

class EnvironmentManager( Thread ):

    #bluetooth_server_rssi_streght = None
    #bluetooth_discoverer = None

    #Stati Thread
    STOPPED = 0
    RUNNING = 1

    status = STOPPED

    #Classe configurazione
    configurator = None

    #Manager sensori prossimità
    proximity_manager = None

    #Classe per la gestione dei parametri direzinali
    route_manager = None

    #Classe per la gestione motori
    motors = None
    motor_left_actual_power = None
    motor_right_actual_power = None

    #Classe gestione magnetometro
    compass = None

    #Direzione obiettivo
    goal_direction_degrees = 305

    #Tolleranza magnetometro
    compass_tolerance = 5

    def getEventLock(self):
        return self.event_lock

    def setEventLock(self,value):
        self.event_lock = value

    def __init__(self):

        print('Getting configuration..')
        self.configurator = Configurator()

        print('Setting GPIO..')
        self.configurator.setGpio()

        print('Starting and configuring Motors..')
        self.motors = Motors( self.configurator.getGpio() )
        self.motor_left_actual_power = self.motors.getMotorLeftActualPower()
        self.motor_right_actual_power = self.motors.getMotorRightActualPower()

        print('Starting Proximity Manager..')
        self.proximity_manager = ProximityManager( self.configurator, self.motors, self )

        print('Starting Compass..')
        self.compass = Compass()

        print('Starting RouteManager..')
        self.route_manager = RouteManager( self.motors, self.compass, self )

        Thread.__init__(self)
        self.deamon = True
        self.status = self.RUNNING
        self.start()
        #self.bluetooth_discoverer = BluetoothDiscoverer()

    def run(self):
        while self.status != self.STOPPED:
            time.sleep(0.5)

            try:

                if self.proximity_manager.getRightStopDistance() is None:
                    print('Starting rotation..')
                    self.proximity_manager.proximityRotation('LEFT', 'RIGHT')

                """print('FRONT AVAILABILIT: ' + str( self.proximity_manager.getFrontAvailability() ))
                print('LEFT AVAILABILIT: ' + str( self.proximity_manager.getLeftAvailability() ))
                print('RIGHT AVAILABILIT: ' + str( self.proximity_manager.getRightAvailability() ))"""

            except Exception, e:
                print('Exception: ' + str(e))
                self.motors.stop()
                self.stop()

            #self.bluetooth_discoverer.startInquiring(self)

    """def setBluetoothServerRssiStrength(self, value):
        print('SET BLUETOOTH SERVER RSSI STRENGTH TO: ' + str( value ))
        self.bluetooth_server_rssi_streght = value"""

    def stop(self):
        self.status = self.STOPPED
        print('Stopping EnvironmentManager..')

        if self.proximity_manager is not None:
            self.proximity_manager.stop()

        if self.route_manager is not None:
            self.route_manager.stop()

        if self.configurator is not None:
            self.configurator.gpioCleanup()
