# -*- coding: utf-8 -*-

from threading import Thread
from proximity import Proximity

import threading
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

    #Variabili distanze stop rotazione
    front_stop_distance = None
    left_stop_distance = None
    right_stop_distance = None

    #Tolleranza misurazione in fase di rotazione
    proximity_rotation_tollerance = 2

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

    def getFrontStopDistance(self):
        return self.front_stop_distance

    def getLeftStopDistance(self):
        return self.left_stop_distance

    def getRightStopDistance(self):
        return self.right_stop_distance

    def setFrontAvailability(self, value):
        self.front_availability = value

    def setLeftAvailability(self, value):
        self.left_availability = value

    def setRightAvailability(self, value):
        self.right_availability = value

    def setFrontStopDistance(self, value):
        self.front_stop_distance = value

    def setLeftStopDistance(self, value):
        self.left_stop_distance = value

    def setRightStopDistance(self, value):
        self.right_stop_distance = value

    def __init__(self, configurator, motors_object, environment_manager_object):

        print( 'Initializing ProximityManager..' )

        self.lock = threading.Lock()

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
        self.proximity = Proximity( configurator )
        print( 'Initializing proximity sensors..' )

        Thread.__init__(self)
        self.deamon = True
        self.status = self.RUNNING
        self.start()

    def run(self):
        while self.status != self.STOPPED:

            time.sleep(0.09)

            try:

                if self.lock.locked() == True:
                    print('Main lock already acquire, continue..')
                    continue

                print('Main acquire lock')
                self.lock.acquire()

                print('Getting measurements for all directions..')
                self.measurements = self.proximity.getDistance()

                if self.left_stop_distance is not None or self.right_stop_distance is not None or self.front_stop_distance is not None:
                    print('Continue..')
                    continue

                print('front_stop_distance: ' + str( self.front_stop_distance ))
                print('left_stop_distance: ' + str( self.left_stop_distance ))
                print('right_stop_distance: ' + str( self.right_stop_distance ))


                print('measurements: ' + str( self.measurements ))

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

            except Exception, e:
                print('ProximityManager exception: ' + str(e))
                raise Exception('ProximityManager execption')
            finally:
                print('Main release lock')
                self.lock.release()

    def proximityRotation(self, from_dir, to_dir):

        print('proximityRotation start..')

        if self.lock.locked() == True:
            print('Lock attivo su un altro processo, rilascio e proseguo')
            self.lock.release()

        if from_dir is None:
            raise Exception('Parameter "from_dir" cannot be None')

        if to_dir is None:
            raise Exception('Parameter "to_dir" cannot be None')

        #Check caso in cui roboto non sia fermo
        if self.motors_object.getMotorsStatus() != self.motors_object.STOPPED:
            print('Stopping motors..')
            self.motors_object.stop()

        #Check parametro distanza "from_dir"
        if self.measurements.get(from_dir) is None:
            return
            #raise Exception('None value distance for ' + str(from_dir) + ' direction, cannot use it as reference')

        #Check presenza effettiva ostacolo
        if self.measurements.get(from_dir) > self.critical_distance:
            raise Exception('No obastacle found in ' + str(from_dir) + ' direction to use as reference')

        if from_dir == 'FRONT':

            if to_dir == 'LEFT':
                #Settaggio distanza di riferimento per stop rotazione
                self.left_stop_distance = self.measurements.get(from_dir)
                #Rotazione senso orario
                self.motors_object.rotation('CLOCKWISE')
            elif to_dir == 'RIGHT':
                #Settaggio distanza di riferimento per stop rotazione
                self.right_stop_distance = self.measurements.get(from_dir)
                #Rotazione senso antiorario
                self.motors_object.rotation('COUNTERCLOCKWISE')

        elif from_dir == 'LEFT':

            if to_dir == 'FRONT':
                #Settaggio distanza di riferimento per stop rotazione
                self.front_stop_distance = self.measurements.get(from_dir)
                #Rotazione senso antiorario
                self.motors_object.rotation('COUNTERCLOCKWISE')
            elif to_dir == 'RIGHT':
                #Settaggio distanza di riferimento per stop rotazione
                self.right_stop_distance = self.measurements.get(from_dir)
                #Rotazione senso antiorario
                self.motors_object.rotation('COUNTERCLOCKWISE')

        elif from_dir == 'RIGHT':

            if to_dir == 'FRONT':
                #Settaggio distanza di riferimento per stop rotazione
                self.front_stop_distance = self.measurements.get(from_dir)
                #Rotazione senso orario
                self.motors_object.rotation('CLOCKWISE')
            elif to_dir == 'LEFT':
                #Settaggio distanza di riferimento per stop rotazione
                self.left_stop_distance = self.measurements.get(from_dir)
                #Rotazione senso orario
                self.motors_object.rotation('CLOCKWISE')

        #try:

        self.lock.acquire()

        while True:

            self.measurements = self.proximity.getDistance()

            if self.measurements is None:
                print('None measurements')
                break

            print('Loop measurements: ' + str( self.measurements ))

            print('Loop front_stop_distance: ' + str( self.front_stop_distance ))
            print('Loop left_stop_distance: ' + str( self.left_stop_distance ))
            print('Loop right_stop_distance: ' + str( self.right_stop_distance ))

            if self.front_stop_distance is not None and (self.measurements.get('FRONT') - self.proximity_rotation_tollerance ) <= self.front_stop_distance <= (self.measurements.get('FRONT') + self.proximity_rotation_tollerance ):
                print('Stopping rotation..')
                self.motors_object.stop()
                self.front_stop_distance = None
                break
            elif self.left_stop_distance is not None and (self.measurements.get('LEFT') - self.proximity_rotation_tollerance ) <= self.left_stop_distance <= (self.measurements.get('LEFT') + self.proximity_rotation_tollerance ):
                print('Stopping rotation..')
                self.motors_object.stop()
                self.left_stop_distance = None
                break;
            elif self.right_stop_distance is not None and (self.measurements.get('RIGHT') - self.proximity_rotation_tollerance ) <= self.right_stop_distance <= (self.measurements.get('RIGHT') + self.proximity_rotation_tollerance ):
                print('Stopping rotation..')
                self.motors_object.stop()
                self.right_stop_distance = None
                break;

        self.lock.release()
        """except Exception, e:
            print('ProximityManager proximityRotation exception: ' + str(e))
            raise Exception('ProximityManager execption')"""



    def stop(self):
        self.status = self.STOPPED

        if self.lock.locked() == True:
            self.lock.release()

        print('Stopping ProximityManager..')
