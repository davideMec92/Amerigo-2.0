# -*- coding: utf-8 -*-

from compass import Compass
from threading import Thread

import time
import random

class RouteManager( Thread ):

    #Stati Thread
    STOPPED = 0
    RUNNING = 1

    status = STOPPED

    #Reference oggetto classo Motors
    motors_object = None

    #Reference classe oggetto Compass
    compass_object = None

    #Direzione obiettivo
    goal_direction_degrees = 300

    #Tolleranza magnetometro
    compass_tolerance = 5

    #Step decrementale potenza motori
    motors_deceleration_step = 5

    normal_mode_status = 'ENABLED'
    bug_mode_status = 'ENABLED'

    queue = None

    directions = {0 : 'LEFT', 1 : 'RIGHT'}

    u_turn = False

    u_turn_forward_steps = 0

    main_locked_direction = None

    def getGoalDirectionDegrees(self):
        return self.goal_direction_degrees

    def getCompassTolerance(self):
        return self.compass_tolerance

    def setGoalDirectionDegrees(self,value):
        self.goal_direction_degrees = value

    def setCompassTolerance(self,value):
        self.compass_tolerance = value

    def __init__(self, motors_object, queue, proximity_manager_object):

        #Check oggetto classe Motors
        if motors_object is None:
            raise Exception('Motors object cannot be null')
            return

        #Check istanza classe ProximityManager
        if proximity_manager_object is None:
            raise Exception('ProximityManager object cannot be null')
            return

        #Reference istanza oggetto classe Motors
        self.motors_object = motors_object

        #Reference istanza oggetto classe ProximityManager
        self.proximity_manager_object = proximity_manager_object

        #Reference istanza oggetto classe Compass
        print('Starting Compass..')
        self.compass_object = Compass()

        self.queue = queue

        Thread.__init__(self)
        self.status = self.RUNNING
        self.name = self.__class__.__name__
        #self.motors_object.forward()
        self.start()

    def run(self):

        while self.status != self.STOPPED:

            if self.queue.full() is not True:
                print('RouteManager Return')
                time.sleep(0.05)
                continue

            try:

                """if self.normal_mode_status == 'ENABLED':
                    print('Starting normalMode..')
                    self.normalMode()"""
                if self.bug_mode_status == 'ENABLED':
                    print('Starting bugMode..')
                    self.bugMode( self.goal_direction_degrees )

            except Exception, e:
                print('RouteManager exception')
                raise Exception('RouteManager execption: ' + str(e))
            finally:
                print('Queue get')
                data = self.queue.get()


    def normalMode( self ):

        if self.normal_mode_status == 'DISABLED':
            return

        #Check stato motori a FORWARD
        if self.motors_object.getMotorsStatus() == self.motors_object.FORWARD:

            degrees = self.compass_object.getDegress()
            motor_left_actual_power = self.motors_object.getMotorLeftActualPower()
            motor_right_actual_power = self.motors_object.getMotorRightActualPower()

            print("Degrees: " + str( degrees ))
            print("Motor left actual power: " + str( motor_left_actual_power ))
            print("Motor right actual power: " + str( motor_right_actual_power ))

            #Caso in cui si è a sinistra dell'obiettivo
            if degrees + self.compass_tolerance < self.goal_direction_degrees:
                print("Goal on the right")

                if motor_right_actual_power >= 0:
                    motor_right_actual_power = motor_right_actual_power - self.motors_deceleration_step
                    self.motors_object.updateMotorPower( 'RIGHT', motor_right_actual_power )

            elif degrees - self.compass_tolerance > self.goal_direction_degrees:
                print("Goal on the left")

                if motor_left_actual_power >= 0:
                    motor_left_actual_power = motor_left_actual_power - self.motors_deceleration_step
                    self.motors_object.updateMotorPower( 'LEFT', motor_left_actual_power )

            else: #Caso in cui obiettivo in posizione frontale
                print("Goal on the front")
                self.motors_object.forward( True )

    def bugMode( self, goal_degrees, parent_degrees = goal_direction_degrees, locked_direction = None ):

        print('parent_degrees: ' + str(parent_degrees))

    	if locked_direction is not None:
    		if self.bug_mode_status == 'DISABLED':
    			self.bug_mode_status = 'ACTIVE'
    	else:
    		if self.bug_mode_status == 'ACTIVE':
    			self.bug_mode_status = 'DISABLED'

        #Caso di stop del thread
        if self.status == self.STOPPED or self.bug_mode_status == 'DISABLED':
            print('Bug Mode disabled, resuming to normal mode..')
            return

        #Valutare variabile istanza di uscita, quando programma interrotto
        #if self.goal_reached() == True:
        	#return True

    	if locked_direction is not None and self.proximity_manager_object.getAvailability().get( locked_direction ) is True:

            self.rotationToDegrees( parent_degrees )

            #In questo caso ricordare di dare un minimo di tolleranza alla bussola dato che parent_degrees è determinato dai gradi bussola (+-5°)
            if abs(self.goal_direction_degrees - parent_degrees) > self.compass_tolerance:
            	return self.bugMode(parent_degrees, self.goal_direction_degrees, self.main_locked_direction)

            if self.main_locked_direction is not None:
            	self.main_locked_direction = None

            print('ERROR 1')
            return self.bugMode(parent_degrees)

        if abs( self.compass_object.getDegress() - goal_degrees ) > self.compass_tolerance:
        	self.rotationToDegrees( goal_degrees )

        if (
                self.u_turn_forward_steps > 0 or
                (self.proximity_manager_object.getAvailability().get('FRONT') is True and self.proximity_manager_object.getAvailability().get(locked_direction) is False) or
                (self.u_turn is True and self.proximity_manager_object.getAvailability().get('RIGHT') is False and self.proximity_manager_object.getAvailability().get('LEFT') is False)

            ):

        	self.motors_object.forward(True)

        	if self.u_turn_forward_steps > 0:
        		self.u_turn_forward_steps = self.u_turn_forward_steps - 1

        	return self.bugMode( goal_degrees, parent_degrees, locked_direction )

    	else:

            if self.proximity_manager_object.getAvailability().get('LEFT') is False:

                #Vicolo cieco
                if self.proximity_manager_object.getAvailability().get('RIGHT') is False:

                    #2 rotazioni da 90° l'una
                    self.motors_object.rotation('CLOCKWISE', False, True)
                    self.motors_object.rotation('CLOCKWISE', False, True)

                    #Set flag u_turn a True
                    self.u_turn = True

                    return self.bugMode( self.compass_object.getDegress(), self.goal_direction_degrees )

                else: #Solo destra libera

                    #Rotazione verso destra di 90°
                    self.motors_object.rotation('CLOCKWISE', False, True)

                    if self.u_turn is True:

                    	#Steps per evitare controllo dx disponibile a TRUE appena girato
                    	self.u_turn_forward_steps = 1

                    	#Reset variabili u_turn
                    	self.u_turn = False

                    	return self.bugMode( self.compass_object.getDegress(), self.goal_direction_degrees, 'RIGHT' )

                    else:

                    	#Caso di prima svolta, quando si incontra un ostacolo sul percorso verso il goal
                    	if abs(goal_degrees - parent_degrees) <= self.compass_tolerance:
                    		self.main_locked_direction = 'LEFT'

                    	return self.bugMode( self.compass_object.getDegress(), goal_degrees, 'LEFT' )

            elif self.proximity_manager_object.getAvailability().get('RIGHT') is False: #Solo sinistra libera

    			#Rotazione verso sinistra di 90°
                self.motors_object.rotation('COUNTERCLOCKWISE', False, True)

                if self.u_turn is True:

    				#Steps per evitare controllo dx disponibile a TRUE appena girato
    				self.u_turn_forward_steps = 1

    				#Reset variabili u_turn
    				self.u_turn = False

    				return self.bugMode( self.compass_object.getDegress(), self.goal_direction_degrees, 'LEFT' )

                else:

                	#Caso di prima svolta, quando si incontra un ostacolo sul percorso verso il goal
                    if abs(goal_degrees - parent_degrees) <= self.compass_tolerance:
                        self.main_locked_direction = 'RIGHT'

                	return self.bugMode( self.compass_object.getDegress(), goal_degrees, 'RIGHT' )

            else:

                random_dir = self.getRandomDirection()

                print('random_dir: ' + str( random_dir ))

                if random_dir == 'LEFT':

                	#Rotazione verso sinistra di 90°
                    self.motors_object.rotation('COUNTERCLOCKWISE', False, True)

                elif random_dir == 'RIGHT':

                	#Rotazione verso destra di 90°
                    self.motors_object.rotation('CLOCKWISE', False, True)

                if self.u_turn is True:

                    #Steps per evitare controllo dx disponibile a TRUE appena girato
                    self.u_turn_forward_steps = 1

                    #Reset variabili u_turn
                    self.u_turn = False

                    return self.bugMode( self.compass_object.getDegress(), self.goal_direction_degrees, random_dir )

                else:

                    opposite_dir = 'LEFT'

                    if random_dir == 'LEFT':
                        opposite_dir = 'RIGHT'

                	#Caso di prima svolta, quando si incontra un ostacolo sul percorso verso il goal
                	if abs(goal_degrees - parent_degrees) <= self.compass_tolerance:
                		self.main_locked_direction = opposite_dir

                	return self.bugMode( self.compass_object.getDegress(), goal_degrees, opposite_dir )

    def rotationToDegrees(self, degress):

        print('Starting rotation to degrees..')

        self.motors_object.rotation('CLOCKWISE')

        while True:

            if self.status == self.STOPPED:
                break

            temp_degrees = self.compass_object.getDegress()

            print('Degrees: ' + str(temp_degrees))

            if abs( degress - temp_degrees ) <= self.compass_tolerance:
                print('Stopping rotation')
                self.motors_object.stop()
                break

    def getRandomDirection(self):
        return self.directions.get( random.randint(0, 1) )

    def stop(self):

        print('Stopping RouteManager..')

        self.status = self.STOPPED
        self.bug_mode_status = 'DISABLED'

        if self.motors_object is not None and self.motors_object.getMotorsStatus() != self.motors_object.STOPPED:
            print('Stopping motors..')
            self.motors_object.stop()
