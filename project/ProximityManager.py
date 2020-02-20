# -*- coding: utf-8 -*-

from threading import Thread
from proximity import Proximity

import time

class ProximityManager( Thread ):

    #Stati Thread
    STOPPED = 0
    RUNNING = 1

    status = STOPPED

    #Oggetto classe Proximity
    proximity = None

    #Variabili direzionali
    front_availability = None
    left_availability = None
    right_availability = None

    #Reference all'istanza della classe EnvironmentManager
    environment_manager_object = None

    #Reference all'istanza della classe Motors
    motors_object = None

    measurements = {}

    #Distanze ostacoli
    out_of_range_distance = float(150) #1,5m
    critical_distance = float(20) #20 cm

    def getMeasurements(self):
        return self.measurements

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

    def __init__(self, configurator, motors_object, environment_manager_object):

        print( 'Initializing ProximityManager..' )

        #Check configurazione
        if configurator is None:
            raise Exception('No configuration received')
            return

        #Check istanza classe Motors
        if motors_object is None:
            raise Exception('Motors object cannot be null')
            return

        #Check istanza classe EnvironmentManager
        if environment_manager_object is None:
            raise Exception('EnvironmentManager object cannot be null')
            return

        #Reference istanza oggetto classe EnvironmentManager
        self.environment_manager_object = environment_manager_object

        #Reference istanza oggetto classe Motors
        self.motors_object = motors_object

        #Inizializzazione oggetto classe Proximity
        self.proximity = Proximity( configurator.getGpio(), configurator.getConf() )
        print( 'Initializing proximity sensors..' )

        Thread.__init__(self)
        self.deamon = True
        self.status = self.RUNNING
        self.start()

    def run(self):
        while self.status != self.STOPPED:
            time.sleep(0.5)

            try:
                print('Getting measurements for all directions..')
                self.measurements = self.proximity.getDistance()

                #Check caso di errore
                if self.measurements is None:

                    print('Error while getting measurements')
                    self.front_availability = False
                    self.left_availability = False
                    self.right_availability = False

                else:

                    if self.measurements.get('FRONT') is None:
                        self.front_availability = False
                    elif self.measurements.get('FRONT') > self.critical_distance:
                        self.front_availability = True
                    elif self.measurements.get('FRONT') <= self.critical_distance:

                        self.front_availability = False

                        #Check caso in cui la direzione motori sia FORWARD e direzione FRONT bloccata
                        if self.motors_object.getMotorsStatus() == self.motors_object.FORWARD:

                            print('Stopping motors..')
                            self.motors_object.stop()

                    if self.measurements.get('LEFT') is None:
                        self.left_availability = False
                    elif self.measurements.get('LEFT') > self.critical_distance:
                        self.left_availability = True
                    elif self.measurements.get('LEFT') <= self.critical_distance:
                        self.left_availability = False

                    if self.measurements.get('RIGHT') is None:
                        self.right_availability = False
                    elif self.measurements.get('RIGHT') > self.critical_distance:
                        self.right_availability = True
                    elif self.measurements.get('RIGHT') <= self.critical_distance:
                        self.right_availability = False

            except Exception:
                print('ProximityManager exception')
                raise Exception('ProximityManager execption')

    def stop(self):
        self.status = self.STOPPED
        print('Stopping ProximityManager..')
