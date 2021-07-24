# -*- coding: utf-8 -*-

from compass import Compass
from threading import Thread
from map_file_manager import MapFileManager
from transaction_manager import TransactionManager
from position_degrees import PositionDegrees
from wifi_rssi_manager import WifiRssiManager
from custom_exceptions import *

import time
import random


class RouteManager(Thread):
    # Stati Thread
    STOPPED = 0
    RUNNING = 1

    status = STOPPED

    # Reference oggetto classo Motors
    motors_object = None

    # Reference classe oggetto Compass
    compass_object = None

    # Direzione obiettivo
    goal_direction_degrees = None

    # Tolleranza magnetometro
    compass_tolerance = 5

    # Step decrementale potenza motori
    motors_deceleration_step = 15

    normal_mode_status = 'ENABLED'
    waiting_for_active_transaction = 'WAITING_FOR_NEW_TRANSACTION'
    bug_mode_status = 'DISABLED'

    directions = {0: 'LEFT', 1: 'RIGHT'}

    u_turn = False

    u_turn_forward_steps = 0

    before_turn_steps = 0

    max_before_turn_steps = 2

    main_locked_direction = None

    max_bug_mode_critical_exceptions = 3

    bug_mode_critical_exceptions_count = 0

    bug_mode_last_move = None

    map_file_manager = None

    positionsDegreesManager = None

    transactionManager = None

    activeTransaction = None

    actualPositionDeviceId = None

    wifiRssiManager = None

    def getGoalDirectionDegrees(self):
        return self.goal_direction_degrees

    def getCompassTolerance(self):
        return self.compass_tolerance

    def setGoalDirectionDegrees(self, value):
        self.goal_direction_degrees = value

    def setCompassTolerance(self, value):
        self.compass_tolerance = value

    def __init__(self, motors_object, proximity_manager_object, wifiRssiManager, positionsDegreesManager, startingSsidPosition):

        # Check oggetto classe Motors
        if motors_object is None:
            raise Exception('Motors object cannot be null')
            return

        # Check istanza classe ProximityManager
        if proximity_manager_object is None:
            raise Exception('ProximityManager object cannot be null')
            return

        # Check istanza classe PositionsDegreesManager
        if positionsDegreesManager is None:
            raise Exception('PositionsDegreesManager object cannot be null')
            return

        # Check istanza classe PositionsDegreesManager
        if startingSsidPosition is None:
            raise Exception('startingSsidPosition value cannot be null')
            return

        # Check istanza classe WifiRssiManager
        if wifiRssiManager is None:
            raise Exception('WifiRssiManager object cannot be null')
            return

        # Reference istanza oggetto classe Motors
        self.motors_object = motors_object

        # Reference istanza oggetto classe PositionsDegreesManager
        self.positionsDegreesManager = positionsDegreesManager

        # Reference istanza oggetto classe ProximityManager
        self.proximity_manager_object = proximity_manager_object

        # Reference istanza oggetto classe WifiManager
        self.wifiRssiManager = wifiRssiManager

        #Inizializzazione classe TransactionManager
        self.transactionManager = TransactionManager()

        #Inzializzazione della posizione attuale con quella di partenza al device più vicino
        self.actualPositionDeviceId = startingSsidPosition

        #Check for a new transaction
        self.getNextActiveTransaction()

        print('GOAL DIRECTION: ' + str(self.goal_direction_degrees))

        # Reference istanza oggetto classe Compass
        print('Starting Compass..')
        self.compass_object = Compass()

        Thread.__init__(self)
        self.status = self.RUNNING
        self.name = self.__class__.__name__
        self.start()

    def getNextActiveTransaction(self):
        print('Asking server for the next active transaction..')
        while self.goal_direction_degrees is None:

            #Asking server for a new transaction and check if last transaction is done
            if self.activeTransaction is None or self.actualPositionDeviceId == self.activeTransaction['goalPeerDeviceId']:
                time.sleep(0.5)
                self.activeTransaction = self.transactionManager.getTransaction(None if self.activeTransaction is None else self.activeTransaction['key'])

            #Check if a new transaction is returned from server
            if self.activeTransaction is not None:
                self.goal_direction_degrees = PositionDegrees.getDeviceToDegrees(self.actualPositionDeviceId, self.activeTransaction['goalPeerDeviceId'])

            #Ask to server for new version of positions Degrees
            if self.goal_direction_degrees is None:
                time.sleep(0.5)
                self.positionsDegreesManager.getPositionsDegrees()


    def run(self):

        while self.status != self.STOPPED:
            wifiRssiCheck = self.wifiRssiManager.checkIfSsidIsNearToMe(self.activeTransaction['goalPeerDeviceId'])

            print('wifiRssiCheck: ' + str(wifiRssiCheck))

            if self.activeTransaction is not None and wifiRssiCheck is True:
                print('Near to ' + str(self.activeTransaction['goalPeerDeviceId']) + 'stopping..')
                self.motors_object.stop()
                self.goal_direction_degrees = None
                self.normal_mode_status = 'DISABLED'
                self.bug_mode_status = 'DISABLED'
                self.actualPositionDeviceId = self.activeTransaction['goalPeerDeviceId']

            time.sleep(0.03)

            if self.normal_mode_status == 'ENABLED':
                print('Starting normalMode..')
                self.normalMode()
            elif self.bug_mode_status == 'ENABLED':
                print('Starting bugMode..')
                self.bugMode(self.goal_direction_degrees)

    def normalMode(self):

        try:

            # Caso di stop del thread
            if self.status == self.STOPPED or self.normal_mode_status == 'DISABLED':
                print('$$$$$ NORMAL MODE: Normal Mode disabled, resuming to normal mode.. $$$$$')
                return

            self.proximity_manager_object.retrieveProximityData()

            if self.proximity_manager_object.getAvailability().get('FRONT') is False:
                print('$$$$$ NORMAL MODE: Enabling bugMode.. $$$$$')
                self.normal_mode_status = 'DISABLED'
                self.bug_mode_status = 'ENABLED'

                if self.map_file_manager is None:
                    print('Initialing MapFileManager..')
                    self.map_file_manager = MapFileManager()

                self.motors_object.restoreMotorActualPowerToDefault()
                return

            # Check stato motori a FORWARD
            if self.motors_object.getMotorsStatus() == self.motors_object.STOPPED:
                self.motors_object.forward()

            degrees = self.compass_object.getDegress()
            motor_left_actual_power = self.motors_object.getMotorLeftActualPower()
            motor_right_actual_power = self.motors_object.getMotorRightActualPower()

            # print("Degrees: " + str( degrees ))
            print(("$$$$$ NORMAL MODE: Motor left actual power: " + str(motor_left_actual_power) + ' $$$$$'))
            print(("$$$$$ NORMAL MODE: Motor right actual power: " + str(motor_right_actual_power) + ' $$$$$'))

            # Caso in cui si è a sinistra dell'obiettivo
            if degrees + self.compass_tolerance < self.goal_direction_degrees:
                print("$$$$$ NORMAL MODE: Goal on the right $$$$$")

                if motor_right_actual_power - self.motors_deceleration_step >= 140:
                    motor_right_actual_power = motor_right_actual_power - self.motors_deceleration_step
                    self.motors_object.updateMotorPower('RIGHT', motor_right_actual_power)

            elif degrees - self.compass_tolerance > self.goal_direction_degrees:
                print("$$$$$ NORMAL MODE: Goal on the left $$$$$")

                if motor_left_actual_power - self.motors_deceleration_step >= 140:
                    motor_left_actual_power = motor_left_actual_power - self.motors_deceleration_step
                    self.motors_object.updateMotorPower('LEFT', motor_left_actual_power)

            else:  # Caso in cui obiettivo in posizione frontale
                print("$$$$$ NORMAL MODE: Goal on the front $$$$$")
                self.motors_object.forward(True)

        except proximityMeasurementErrorException as e:
            print(('$$$$$ NORMAL MODE: proximityMeasurementErrorException: ' + str(e) + ' $$$$$'))
        except proximityGetDistanceException as e:
            print(('$$$$$ NORMAL MODE: proximityGetDistanceException: ' + str(e) + ' $$$$$'))
        except Exception as e:
            print(('$$$$$ NORMAL MODE: Exception: ' + str(e) + ' $$$$$'))
        finally:
            return

    def bugMode(self, goal_degrees, parent_degrees=goal_direction_degrees, locked_direction=None):

        try:

            # Check limite massimo eccezioni raggiunto
            if self.bug_mode_critical_exceptions_count >= self.max_bug_mode_critical_exceptions:
                print('##### BUG MODE: Critical Exceptions limit raised, return #####')
                return

            # Caso di stop del thread
            if self.status == self.STOPPED or self.bug_mode_status == 'DISABLED':
                print('##### BUG MODE: Bug Mode disabled, resuming to normal mode.. #####')
                return

            time.sleep(0.4)
            self.motors_object.stop()

            self.proximity_manager_object.retrieveProximityData()

            if self.map_file_manager is not None:
                data = self.proximity_manager_object.getStringifyMeasurements() + ', ' + str(self.bug_mode_last_move)
                print(('Writing DATA: ' + str(data)))
                self.map_file_manager.append(data)

            # print('goal_degrees: ' + str(goal_degrees))
            # print('parent_degrees: ' + str(parent_degrees))
            print(('##### BUG MODE: Locked direction: ' + str(locked_direction) + ' #####'))

            if locked_direction is not None:
                if self.bug_mode_status == 'DISABLED':
                    self.bug_mode_status = 'ACTIVE'
            else:
                if self.bug_mode_status == 'ACTIVE':
                    self.bug_mode_status = 'DISABLED'

            # print('before_turn_steps: ' + str(self.before_turn_steps))

            if locked_direction is not None:

                # Caso in cui è presente un ostacolo laterale appena iniziato
                if self.proximity_manager_object.getAvailability().get(
                        locked_direction) is False and self.before_turn_steps != self.max_before_turn_steps:
                    self.before_turn_steps = self.max_before_turn_steps
                    # print('before_turn_steps: ' + str(self.before_turn_steps))
                elif self.proximity_manager_object.getAvailability().get(
                        locked_direction) is True and self.before_turn_steps == 0:

                    print('##### BUG MODE: locked direction now free #####')

                    if locked_direction == 'RIGHT':
                        self.motors_object.rotation('CLOCKWISE', False, True)
                        # TEST
                        self.bug_mode_last_move = 'C'
                    elif locked_direction == 'LEFT':
                        self.motors_object.rotation('COUNTERCLOCKWISE', False, True)
                        # TEST
                        self.bug_mode_last_move = 'CC'

                    # In questo caso ricordare di dare un minimo di tolleranza alla bussola dato che parent_degrees è determinato dai gradi bussola (+-5°)
                    if abs(self.goal_direction_degrees - parent_degrees) > self.compass_tolerance:
                        self.before_turn_steps = self.max_before_turn_steps
                        return self.bugMode(parent_degrees, self.goal_direction_degrees, self.main_locked_direction)

                    if self.main_locked_direction is not None:
                        self.main_locked_direction = None

                    return self.bugMode(parent_degrees)

            print(('##### BUG MODE: FRONT availability: ' + str(
                self.proximity_manager_object.getAvailability().get('FRONT')) + ' #####'))
            print(('##### BUG MODE: LEFT availability: ' + str(
                self.proximity_manager_object.getAvailability().get('LEFT')) + ' #####'))
            print(('##### BUG MODE: RIGHT availability: ' + str(
                self.proximity_manager_object.getAvailability().get('RIGHT')) + ' #####'))
            # print('locked_direction (' + str(locked_direction) + ') availability: ' + str(self.proximity_manager_object.getAvailability().get(locked_direction)))
            # print('self u_turn: ' + str( self.u_turn ))
            # print('self u_turn_forward_steps: ' + str( self.u_turn_forward_steps ))

            # Riabilitazione normalMode
            if self.u_turn is False and self.before_turn_steps == 0 and self.proximity_manager_object.getAvailability().get(
                    'FRONT') is True and self.proximity_manager_object.getAvailability().get(
                    'LEFT') is True and self.proximity_manager_object.getAvailability().get('RIGHT') is True:
                print('##### BUG MODE: Enabling normalMode.. #####')
                self.normal_mode_status = 'ENABLED'
                self.bug_mode_status = 'DISABLED'

                if self.map_file_manager is not None:
                    self.map_file_manager.close()

                self.bug_mode_last_move = None

                return

            # Check direzione front libera
            if self.proximity_manager_object.getAvailability().get('FRONT') is True:

                # Aggiunto and self.u_turn True valutare
                if self.before_turn_steps > 0 or (self.u_turn is False and (
                        locked_direction is None or self.proximity_manager_object.getAvailability().get(
                        locked_direction) is False)) or (
                        self.u_turn is True and self.proximity_manager_object.getAvailability().get(
                        'RIGHT') is False and self.proximity_manager_object.getAvailability().get('LEFT') is False):

                    self.motors_object.forward(True)

                    # TEST
                    self.bug_mode_last_move = 'F'

                    if self.before_turn_steps > 0:
                        self.before_turn_steps = self.before_turn_steps - 1

                    print('##### BUG MODE: Dritto #####')

                    return self.bugMode(goal_degrees, parent_degrees, locked_direction)

            # print('before_turn_steps reset')
            self.before_turn_steps = self.max_before_turn_steps

            # Check caso in cui sinistra è occupata
            if self.proximity_manager_object.getAvailability().get('LEFT') is False:

                # Vicolo cieco
                if self.proximity_manager_object.getAvailability().get('RIGHT') is False:
                    print('##### BUG MODE: u_turn #####')

                    # 2 rotazioni da 90° l'una
                    self.motors_object.rotation('CLOCKWISE', False, True)
                    self.motors_object.rotation('CLOCKWISE', False, True)
                    # TEST
                    self.bug_mode_last_move = '2C'

                    # Set flag u_turn a True
                    self.u_turn = True

                    return self.bugMode(self.compass_object.getDegress(), self.goal_direction_degrees)

                else:  # Solo destra libera

                    # Check direzione libera dopo u_turn
                    if self.u_turn is True and self.u_turn_forward_steps == 0:
                        print(('u_turn steps: ' + str(self.before_turn_steps)))
                        self.before_turn_steps = self.max_before_turn_steps - 1
                        self.u_turn_forward_steps = 1
                        return self.bugMode(goal_degrees, parent_degrees)

                    # Rotazione verso destra di 90°
                    self.motors_object.rotation('CLOCKWISE', False, True)
                    # TEST
                    self.bug_mode_last_move = 'C'

                    # TODO VEDERE SE ELIMINARE
                    if self.u_turn is True:

                        # print('BUG MODE: coming from u_turn RIGHT availability true')

                        # Steps per evitare controllo dx disponibile a TRUE appena girato
                        self.u_turn_forward_steps = 0

                        self.before_turn_steps = self.max_before_turn_steps

                        # Reset variabili u_turn
                        self.u_turn = False

                        return self.bugMode(self.compass_object.getDegress(), self.goal_direction_degrees, 'RIGHT')

                    else:

                        # print('BUG MODE: RIGHT availability true, normal turn')

                        # Caso di prima svolta, quando si incontra un ostacolo sul percorso verso il goal
                        if abs(goal_degrees - parent_degrees) <= self.compass_tolerance:
                            self.main_locked_direction = 'LEFT'

                        # print('BUG MODE: Recursive first call')
                        return self.bugMode(self.compass_object.getDegress(), goal_degrees, 'LEFT')

            elif self.proximity_manager_object.getAvailability().get('RIGHT') is False:  # Solo sinistra libera

                # Check direzione libera dopo u_turn
                if self.u_turn is True and self.u_turn_forward_steps == 0:
                    # print('u_turn steps: ' + str(self.before_turn_steps))
                    self.before_turn_steps = self.max_before_turn_steps - 1
                    self.u_turn_forward_steps = 1
                    return self.bugMode(goal_degrees, parent_degrees)

                # Rotazione verso sinistra di 90°
                self.motors_object.rotation('COUNTERCLOCKWISE', False, True)
                # TEST
                self.bug_mode_last_move = 'CC'

                # TODO VEDERE SE ELIMINARE
                if self.u_turn is True:

                    # print('BUG MODE: coming from u_turn LEFT availability true')

                    # Steps per evitare controllo dx disponibile a TRUE appena girato
                    self.u_turn_forward_steps = 0

                    self.before_turn_steps = self.max_before_turn_steps

                    # Reset variabili u_turn
                    self.u_turn = False

                    return self.bugMode(self.compass_object.getDegress(), self.goal_direction_degrees, 'LEFT')

                else:

                    # print('BUG MODE: LEFT availability true, normal turn')

                    # Caso di prima svolta, quando si incontra un ostacolo sul percorso verso il goal
                    if abs(goal_degrees - parent_degrees) <= self.compass_tolerance:
                        self.main_locked_direction = 'RIGHT'

                    return self.bugMode(self.compass_object.getDegress(), goal_degrees, 'RIGHT')

            else:

                # Check direzione libera dopo u_turn
                if self.u_turn is True and self.u_turn_forward_steps == 0:
                    # print('u_turn steps: ' + str(self.before_turn_steps))
                    self.before_turn_steps = self.max_before_turn_steps - 1
                    self.u_turn_forward_steps = 1
                    return self.bugMode(goal_degrees, parent_degrees)

                random_dir = self.getRandomDirection()

                print(('##### BUG MODE: random_dir: ' + str(random_dir) + ' #####'))

                if random_dir == 'LEFT':

                    # Rotazione verso sinistra di 90°
                    self.motors_object.rotation('COUNTERCLOCKWISE', False, True)
                    # TEST
                    self.bug_mode_last_move = 'CC'

                elif random_dir == 'RIGHT':

                    # Rotazione verso destra di 90°
                    self.motors_object.rotation('CLOCKWISE', False, True)
                    # TEST
                    self.bug_mode_last_move = 'C'

                if self.u_turn is True:

                    # print('BUG MODE: coming from u_turn LEFT and RIGHT availability true')

                    # Steps per evitare controllo dx disponibile a TRUE appena girato
                    self.u_turn_forward_steps = 0

                    self.before_turn_steps = self.max_before_turn_steps

                    # Reset variabili u_turn
                    self.u_turn = False

                    return self.bugMode(self.compass_object.getDegress(), self.goal_direction_degrees, random_dir)

                else:

                    # print('BUG MODE: LEFT and RIGHT availability true, normal turn')

                    opposite_dir = 'LEFT'

                    if random_dir == 'LEFT':
                        opposite_dir = 'RIGHT'

                        # Caso di prima svolta, quando si incontra un ostacolo sul percorso verso il goal
                        if abs(goal_degrees - parent_degrees) <= self.compass_tolerance:
                            self.main_locked_direction = opposite_dir

                    # print('BUG MODE: Recursive call 2')
                    return self.bugMode(self.compass_object.getDegress(), goal_degrees, opposite_dir)

        except proximityMeasurementErrorException as e:
            print(('##### BUG MODE: BugMode exception: ' + str(e) + ' #####'))
            print('##### BUG MODE: Recall bugMode Method #####')
            self.bugMode(goal_degrees, parent_degrees, locked_direction)
        except compassGetRotationDegreeCostsException as e:
            print(('##### BUG MODE: compassGetRotationDegreeCostsException: ' + str(e) + ' #####'))
            print('##### BUG MODE: Recall bugMode Method #####')
            self.bug_mode_critical_exceptions_count = self.bug_mode_critical_exceptions_count + 1
            self.bugMode(goal_degrees, parent_degrees, locked_direction)
        except proximityGetDistanceException as e:
            print(('##### BUG MODE: proximityGetDistanceException: ' + str(e) + ' #####'))
            print('##### BUG MODE: Recall bugMode Method #####')
            self.bug_mode_critical_exceptions_count = self.bug_mode_critical_exceptions_count + 1
            self.bugMode(goal_degrees, parent_degrees, locked_direction)
        except Exception as e:
            print(('##### BUG MODE: Generic Exception: ' + str(e) + ', return #####'))
            self.bug_mode_critical_exceptions_count = self.bug_mode_critical_exceptions_count + 1
            self.bugMode(goal_degrees, parent_degrees, locked_direction)

    def rotationToDegrees(self, degress):

        if self.status == self.STOPPED:
            return

        print('Starting rotation to degrees..')

        # Ottenimento posizione attuale
        temp_degrees = self.compass_object.getDegress()

        # Ottenimento costi rotazioni oraria e antioraria
        rotation_degree_costs = self.compass_object.getRotationDegreeCosts(temp_degrees, degress)

        if rotation_degree_costs.get('clockwise_cost') < rotation_degree_costs.get('counterclockwise_cost'):
            self.motors_object.rotation('CLOCKWISE')
        else:
            self.motors_object.rotation('COUNTERCLOCKWISE')

        while True and self.status == self.RUNNING:

            temp_degrees = self.compass_object.getDegress()

            if abs(degress - temp_degrees) <= self.compass_tolerance + 5:
                print('Stopping rotation')
                self.motors_object.stop()
                temp_degrees = self.compass_object.getDegress()
                break

    def getRandomDirection(self):
        return self.directions.get(random.randint(0, 1))

    def stop(self):

        print('Stopping RouteManager..')

        self.status = self.STOPPED
        self.bug_mode_status = 'DISABLED'

        if self.motors_object is not None and self.motors_object.getMotorsStatus() != self.motors_object.STOPPED:
            print('Stopping motors..')
            self.motors_object.stop()

        if self.map_file_manager is not None:
            self.map_file_manager.close()
