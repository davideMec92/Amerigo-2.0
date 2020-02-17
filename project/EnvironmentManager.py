# -*- coding: utf-8 -*-

#from bluetooth_discoverer import BluetoothDiscoverer

from threading import Thread

from configurator import Configurator
from ProximityManager import ProximityManager
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

    #Variabili direzionali
    front_availability = True
    left_availability = True
    right_availability = True

    #Classe configurazione
    configurator = None

    #Manager sensori prossimità
    proximity_manager = None

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

    def getFrontAvailability(self):
        return self.front_availability

    def getLeftAvailability(self):
        return self.left_availability

    def getRightAvailability(self):
        return self.right_availability

    def setFrontAvailability(self, value):
        self.front_availability = value

    def setLeftAvailability(self, value):
        self.left_availability = value

    def setRightAvailability(self, value):
        self.right_availability = value

    def __init__(self):

        print('Getting configuration..')
        self.configurator = Configurator()
        print('Setting GPIO..')
        self.configurator.setGpio()

        print('Starting Proximity Manager..')
        self.proximity_manager = ProximityManager( self.configurator, self )

        print('Starting adn configuring Motors..')
        self.motors = Motors( self.configurator.getGpio() )
        self.motor_left_actual_power = self.motors.getMotorLeftActualPower()
        self.motor_right_actual_power = self.motors.getMotorRightActualPower()

        print('Starting Compass..')
        self.compass = Compass()

        Thread.__init__(self)
        self.deamon = True
        self.status = self.RUNNING
        self.start()
        #self.bluetooth_discoverer = BluetoothDiscoverer()

    def run(self):
        while self.status != self.STOPPED:
            time.sleep(0.1)

            try:
                #Check direzione stabilita
                if self.goal_direction_degrees is not None:

                    print('FRONT AVAILABILIT: ' + str( self.front_availability ))
                    print('LEFT AVAILABILIT: ' + str( self.left_availability ))
                    print('RIGHT AVAILABILIT: ' + str( self.right_availability ))

                    #Check direzione frontale libera
                    if self.front_availability is True:

                        print('self.motors.STOPPED: ' + str(self.motors.STOPPED))

                        #Check caso in cui robot sia fermo
                        if self.motors.getMotorsStatus() == self.motors.STOPPED:
                            print('Starting motors forward')
                            self.motors.forward()

                    elif self.front_availability is False and self.motors.getMotorsStatus() == self.motors.FORWARD: #Check caso in cui direzione frontale non disponibile e robot avanza
                        self.motors.stop()
                        self.stop()
            except Exception:
                print('Exception')
                self.motors.stop()
                self.stop()

            #self.bluetooth_discoverer.startInquiring(self)

    """def setBluetoothServerRssiStrength(self, value):
        print('SET BLUETOOTH SERVER RSSI STRENGTH TO: ' + str( value ))
        self.bluetooth_server_rssi_streght = value"""

    def stop(self):
        self.status = self.STOPPED

        if self.proximity_manager is not None:
            self.proximity_manager.stop()

        if self.configurator is not None:
            self.configurator.gpioCleanup()
