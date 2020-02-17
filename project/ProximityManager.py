# -*- coding: utf-8 -*-

from threading import Thread
from proximity import Proximity

import time

class ProximityManager( Thread ):

    #Stati Thread
    STOPPED = 0
    RUNNING = 1

    status = STOPPED

    proximity = None
    environment_manager_object = None

    #Distanze ostacoli
    out_of_range_distance = float(150) #1,5m
    critical_distance = float(20) #20 cm

    def __init__(self, configurator, environment_manager_object):

        print( 'Initializing ProximityManager..' )

        #Check configurazione
        if configurator is None:
            raise Exception('No configuration received')
            return

        #Check configurazione
        if environment_manager_object is None:
            raise Exception('EnvironmentManager objetc cannot be null')
            return

        #Reference istanza oggetto classe EnvironmentManager
        self.environment_manager_object = environment_manager_object

        #Inizializzazione oggetto classe Proximity
        self.proximity = Proximity( configurator.getGpio(), configurator.getConf() )
        print( 'Initializing proximity sensors..' )

        Thread.__init__(self)
        self.deamon = True
        self.status = self.RUNNING
        self.start()

    def run(self):
        while self.status != self.STOPPED:
            time.sleep(0.1)

            print('Getting measures for all directions..')
            measures = self.proximity.getDistance()

            #Check caso di errore
            if measures is None:

                print('Error while getting measures')
                self.environment_manager_object.setFrontAvailability(False)
                self.environment_manager_object.setLeftAvailability(False)
                self.environment_manager_object.setRightAvailability(False)

            else:

                if measures.get('FRONT') is None:
                    self.environment_manager_object.setFrontAvailability(False)
                elif measures.get('FRONT') > self.critical_distance:
                    self.environment_manager_object.setFrontAvailability(True)
                elif measures.get('FRONT') <= self.critical_distance:
                    self.environment_manager_object.setFrontAvailability(False)

                if measures.get('LEFT') is None:
                    self.environment_manager_object.setLeftAvailability(False)
                elif measures.get('LEFT') > self.critical_distance:
                    self.environment_manager_object.setLeftAvailability(True)
                elif measures.get('LEFT') <= self.critical_distance:
                    self.environment_manager_object.setLeftAvailability(False)

                if measures.get('RIGHT') is None:
                    self.environment_manager_object.setRightAvailability(False)
                elif measures.get('RIGHT') > self.critical_distance:
                    self.environment_manager_object.setRightAvailability(True)
                elif measures.get('RIGHT') <= self.critical_distance:
                    self.environment_manager_object.setRightAvailability(False)


    def stop(self):
        self.status = self.STOPPED
