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

    lock = None

    def getGoalDirectionDegrees(self):
        return self.goal_direction_degrees

    def getCompassTolerance(self):
        return self.compass_tolerance

    def setGoalDirectionDegrees(self,value):
        self.goal_direction_degrees = value

    def setCompassTolerance(self,value):
        self.compass_tolerance = value

    def __init__(self, motors_object, queue, proximity_manager_object, lock):

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

        self.lock = lock

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

                print('RouteManager Acquire lock..')
                self.lock.acquire()

                """if self.normal_mode_status == 'ENABLED':
                    print('Starting normalMode..')
                    self.normalMode()"""
                if self.bug_mode_status == 'ENABLED':
                    print('Starting bugMode..')
                    self.bugMode( self.goal_direction_degrees )

            except Exception, e:
                print('RouteManager exception: ' + str(e))
                raise Exception('RouteManager execption: ' + str(e))
            finally:
                print('ROUTE MANAGER Queue get')
                data = self.queue.get()
                print('RouteManager Release lock..')
                self.lock.release()

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

        print('Refreshing proximity data..')
        self.proximity_manager_object.refreshData()

        print('goal_degrees: ' + str(goal_degrees))
        print('parent_degrees: ' + str(parent_degrees))
        print('locked_direction: ' + str(locked_direction))

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

            print('BUG MODE: locked direction now free')

            self.rotationToDegrees( parent_degrees )

            #In questo caso ricordare di dare un minimo di tolleranza alla bussola dato che parent_degrees è determinato dai gradi bussola (+-5°)
            if abs(self.goal_direction_degrees - parent_degrees) > self.compass_tolerance:
                print('STO CAZZO')
            	return self.bugMode(parent_degrees, self.goal_direction_degrees, self.main_locked_direction)

            if self.main_locked_direction is not None:
            	self.main_locked_direction = None

            print('ERROR 1')
            return self.bugMode(parent_degrees)

        if abs( self.compass_object.getDegress() - goal_degrees ) > self.compass_tolerance:

            print('BUG MODE: Rotation to goal degrees: ' + str(goal_degrees))
            self.rotationToDegrees( goal_degrees )


        print('FRONT availability: ' + str(self.proximity_manager_object.getAvailability().get('FRONT')))
        print('LEFT availability: ' + str(self.proximity_manager_object.getAvailability().get('LEFT')))
        print('RIGHT availability: ' + str(self.proximity_manager_object.getAvailability().get('RIGHT')))
        print('locked_direction (' + str(locked_direction) + ') availability: ' + str(self.proximity_manager_object.getAvailability().get(locked_direction)))
        print('self u_turn: ' + str( self.u_turn ))

        if self.u_turn_forward_steps > 0 or (self.proximity_manager_object.getAvailability().get('FRONT') is True and ( locked_direction is None or self.proximity_manager_object.getAvailability().get(locked_direction) is False) ) or (self.u_turn is True and self.proximity_manager_object.getAvailability().get('RIGHT') is False and self.proximity_manager_object.getAvailability().get('LEFT') is False):

            self.motors_object.forward(True)

            if self.u_turn_forward_steps > 0:
            	self.u_turn_forward_steps = self.u_turn_forward_steps - 1

            print('BUG MODE: Dritto')

            return self.bugMode( goal_degrees, parent_degrees, locked_direction )

        else:

            print('BUG MODE: Else marco di merda!')

            #Check caso in cui sinistra è occupata
            if self.proximity_manager_object.getAvailability().get('LEFT') is False:
                print('BUG MODE: LEFT availability false')

                #Vicolo cieco
                if self.proximity_manager_object.getAvailability().get('RIGHT') is False:
                    print('BUG MODE: u_turn')

                    #2 rotazioni da 90° l'una
                    self.motors_object.rotation('CLOCKWISE', False, True)
                    self.motors_object.rotation('CLOCKWISE', False, True)

                    #Set flag u_turn a True
                    self.u_turn = True

                    return self.bugMode( self.compass_object.getDegress(), self.goal_direction_degrees )

                else: #Solo destra libera

                    print('BUG MODE: RIGHT availability true')

                    #Rotazione verso destra di 90°
                    self.motors_object.rotation('CLOCKWISE', False, True)

                    if self.u_turn is True:

                        print('BUG MODE: coming from u_turn RIGHT availability true')

                    	#Steps per evitare controllo dx disponibile a TRUE appena girato
                    	self.u_turn_forward_steps = 1

                    	#Reset variabili u_turn
                    	self.u_turn = False

                    	return self.bugMode( self.compass_object.getDegress(), self.goal_direction_degrees, 'RIGHT' )

                    else:

                        print('BUG MODE: RIGHT availability true, normal turn')

                    	#Caso di prima svolta, quando si incontra un ostacolo sul percorso verso il goal
                    	if abs(goal_degrees - parent_degrees) <= self.compass_tolerance:
                    		self.main_locked_direction = 'LEFT'

                        print('BUG MODE: Recursive first call')
                    	return self.bugMode( self.compass_object.getDegress(), goal_degrees, 'LEFT' )

            elif self.proximity_manager_object.getAvailability().get('RIGHT') is False: #Solo sinistra libera
                print('BUG MODE: RIGHT availability false')

    			#Rotazione verso sinistra di 90°
                self.motors_object.rotation('COUNTERCLOCKWISE', False, True)

                if self.u_turn is True:

                    print('BUG MODE: coming from u_turn LEFT availability true')

                    #Steps per evitare controllo dx disponibile a TRUE appena girato
                    self.u_turn_forward_steps = 1

                    #Reset variabili u_turn
                    self.u_turn = False

                    return self.bugMode( self.compass_object.getDegress(), self.goal_direction_degrees, 'LEFT' )

                else:

                    print('BUG MODE: LEFT availability true, normal turn')

                	#Caso di prima svolta, quando si incontra un ostacolo sul percorso verso il goal
                    if abs(goal_degrees - parent_degrees) <= self.compass_tolerance:
                        self.main_locked_direction = 'RIGHT'

                	return self.bugMode( self.compass_object.getDegress(), goal_degrees, 'RIGHT' )

            else:
                print('BUG MODE: LEFT and RIGHT availability true')

                random_dir = self.getRandomDirection()

                print('random_dir: ' + str( random_dir ))

                if random_dir == 'LEFT':

                	#Rotazione verso sinistra di 90°
                    self.motors_object.rotation('COUNTERCLOCKWISE', False, True)

                elif random_dir == 'RIGHT':

                	#Rotazione verso destra di 90°
                    self.motors_object.rotation('CLOCKWISE', False, True)

                if self.u_turn is True:

                    print('BUG MODE: coming from u_turn LEFT and RIGHT availability true')

                    #Steps per evitare controllo dx disponibile a TRUE appena girato
                    self.u_turn_forward_steps = 1

                    #Reset variabili u_turn
                    self.u_turn = False

                    return self.bugMode( self.compass_object.getDegress(), self.goal_direction_degrees, random_dir )

                else:

                    print('BUG MODE: LEFT and RIGHT availability true, normal turn')

                    opposite_dir = 'LEFT'

                    if random_dir == 'LEFT':
                        opposite_dir = 'RIGHT'

                	#Caso di prima svolta, quando si incontra un ostacolo sul percorso verso il goal
                	if abs(goal_degrees - parent_degrees) <= self.compass_tolerance:
                		self.main_locked_direction = opposite_dir

                    print('BUG MODE: Recursive call 2')
                    #TODO ESEGUIRE ROTAZIONE PRIMA RICORSIONE
                    return self.bugMode( self.compass_object.getDegress(), goal_degrees, opposite_dir )

    def rotationToDegrees(self, degress):

        """print('RouteManager Acquire lock..')
        self.lock.acquire()"""

        print('Starting rotation to degrees..')

        #Ottenimento posizione attuale
        temp_degrees = self.compass_object.getDegress()

        rotation_degree_costs = self.compass_object.getRotationDegreeCosts( temp_degrees, degress )

        print('rotation_degree_costs: ' + str( rotation_degree_costs ))

        if rotation_degree_costs.get('clockwise_cost') < rotation_degree_costs.get('counterclockwise_cost'):
            print('Sono nel range')
            self.motors_object.rotation('CLOCKWISE')
        else:
            print('Non sono nel range')
            self.motors_object.rotation('COUNTERCLOCKWISE')

        print('Now dregrees: ' + str(temp_degrees))
        #self.motors_object.updateMotorPower('LEFT', 150)
        #self.motors_object.updateMotorPower('RIGHT', 150)

        while True:

            if self.status == self.STOPPED:
                break

            temp_degrees = self.compass_object.getDegress()

            print('Degrees: ' + str(temp_degrees))

            if abs( degress - temp_degrees ) <= self.compass_tolerance + 5:
                print('Stopping rotation')
                self.motors_object.stop()
                temp_degrees = self.compass_object.getDegress()
                print('Degrees: ' + str(temp_degrees))
                break

        self.motors_object.updateMotorPower('LEFT', 200)
        self.motors_object.updateMotorPower('RIGHT', 200)

        """print('RouteManager Release lock..')
        self.lock.release()"""

    def getRandomDirection(self):
        return self.directions.get( random.randint(0, 1) )

    def stop(self):

        print('Stopping RouteManager..')

        self.status = self.STOPPED
        self.bug_mode_status = 'DISABLED'

        if self.motors_object is not None and self.motors_object.getMotorsStatus() != self.motors_object.STOPPED:
            print('Stopping motors..')
            self.motors_object.stop()
