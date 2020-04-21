# -*- coding: utf-8 -*-

from proximity import Proximity
from custom_exceptions import *

import time

class ProximityManager:

    #Oggetto classe Proximity
    proximity = None

    #Variabili direzionali
    front_availability = None
    left_availability = None
    right_availability = None

    #Reference all'istanza della classe Motors
    motors_object = None

    #Dizionario misurazioni
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

    def getAvailability(self):
        directions_availability = { 'LEFT' : self.left_availability, 'FRONT' : self.front_availability, 'RIGHT' : self.right_availability }
        return directions_availability

    def __init__(self, configurator, motors_object):

        print( 'Initializing ProximityManager..' )

        #Check configurazione
        if configurator is None:
            raise Exception('No configuration received')
            return

        #Check istanza classe Motors
        if motors_object is None:
            raise Exception('Motors object cannot be null')
            return

        #Reference istanza oggetto classe Motors
        self.motors_object = motors_object

        #Inizializzazione oggetto classe Proximity
        self.proximity = Proximity( configurator )
        print( 'Initializing proximity sensors..' )

    def retrieveProximityData(self):

        print('Getting measurements for all directions..')
        self.measurements = self.proximity.getDistance()

        print('Measurements: ' + str(self.measurements))

        #Check caso di errore
        if self.measurements is None:

            print('Error while getting measurements')
            raise proximityMeasurementErrorException('Error while getting proximity measurements')
            self.front_availability = False
            self.left_availability = False
            self.right_availability = False

        else:

            if self.measurements.get('FRONT') is None:

                self.front_availability = False

                #Check caso in cui la direzione motori sia FORWARD e direzione FRONT bloccata
                if self.motors_object.getMotorsStatus() == self.motors_object.FORWARD:

                    print('Stopping front measurement None')
                    self.motors_object.stop()

                raise proximityMeasurementErrorException('FRONT measure None')

            elif self.measurements.get('FRONT') > self.critical_distance:
                self.front_availability = True
            elif self.measurements.get('FRONT') <= self.critical_distance:

                self.front_availability = False

                #Check caso in cui la direzione motori sia FORWARD e direzione FRONT bloccata
                if self.motors_object.getMotorsStatus() == self.motors_object.FORWARD:

                    print('ProximityManager stopping motors..')
                    self.motors_object.stop()

                    #print('ninetyDegreesRotation..')
                    #self.motors_object.rotation('CLOCKWISE', False, True)

            if self.measurements.get('LEFT') is None:
                self.left_availability = False
                raise proximityMeasurementErrorException('LEFT measure None')
            elif self.measurements.get('LEFT') > self.critical_distance:
                self.left_availability = True
            elif self.measurements.get('LEFT') <= self.critical_distance:

                self.left_availability = False

                #Check caso in cui il robot sia in movimento e abbia raggiunto la distanza critica
                if self.motors_object.getMotorsStatus() != self.motors_object.STOPPED:

                    print('ProximityManager stopping motors..')
                    self.motors_object.stop()


            if self.measurements.get('RIGHT') is None:
                self.right_availability = False
                raise proximityMeasurementErrorException('RIGHT measure None')
            elif self.measurements.get('RIGHT') > self.critical_distance:
                self.right_availability = True
            elif self.measurements.get('RIGHT') <= self.critical_distance:

                self.right_availability = False

                #Check caso in cui il robot sia in movimento e abbia raggiunto la distanza critica
                if self.motors_object.getMotorsStatus() != self.motors_object.STOPPED:

                    print('ProximityManager stopping motors..')
                    self.motors_object.stop()

    def proximityRotation(self, from_dir, to_dir):

        print('proximityRotation start..')

        if from_dir is None:
            raise Exception('Parameter "from_dir" cannot be None')

        if to_dir is None:
            raise Exception('Parameter "to_dir" cannot be None')

        #TODO checl from_dir == FRONT, LEFT, RIGHT
        #TODO checl to_dir == FRONT, LEFT, RIGHT
        #TODO check che from_dir e to_dir non siano uguali

        #Check caso in cui robot non sia fermo
        if self.motors_object.getMotorsStatus() != self.motors_object.STOPPED:
            print('Stopping motors 2..')
            self.motors_object.stop()

        #Check parametro distanza "from_dir"
        if self.measurements.get(from_dir) is None:
            print('Distance from obastacle not found')
            return
            #raise Exception('None value distance for ' + str(from_dir) + ' direction, cannot use it as reference')

        #Check presenza effettiva ostacolo
        if self.measurements.get(from_dir) > self.critical_distance:
            raise Exception('No obastacle found in ' + str(from_dir) + ' direction to use as reference')

        if from_dir == 'FRONT':

            if to_dir == 'LEFT':
                #Rotazione senso orario
                self.motors_object.rotation('CLOCKWISE')
            elif to_dir == 'RIGHT':
                #Rotazione senso antiorario
                self.motors_object.rotation('COUNTERCLOCKWISE')

        elif from_dir == 'LEFT':

            if to_dir == 'FRONT':
                #Rotazione senso antiorario
                self.motors_object.rotation('COUNTERCLOCKWISE')
            elif to_dir == 'RIGHT':
                #Rotazione senso antiorario
                self.motors_object.rotation('COUNTERCLOCKWISE')

        elif from_dir == 'RIGHT':

            if to_dir == 'FRONT':
                #Rotazione senso orario
                self.motors_object.rotation('CLOCKWISE')
            elif to_dir == 'LEFT':
                #Rotazione senso orario
                self.motors_object.rotation('CLOCKWISE')

        time.sleep(0.4)
        print('Motors stop..')
        self.motors_object.stop()

    def stop(self):

        print('Stopping ProximityManager..')

        self.motors_object.stop()

        if self.proximity is not None:
            self.proximity.cancel()
