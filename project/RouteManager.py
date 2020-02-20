# -*- coding: utf-8 -*-

from threading import Thread

import time

class RouteManager( Thread ):

    #Stati Thread
    STOPPED = 0
    RUNNING = 1

    status = STOPPED

    motors_object = None
    environment_manager_object = None
    compass_object = None

    #Variabili direzionali

    #Direzione obiettivo
    goal_direction_degrees = 125

    #Tolleranza magnetometro
    compass_tolerance = 5

    def getGoalDirectionDegrees(self):
        return self.goal_direction_degrees

    def getCompassTolerance(self):
        return self.compass_tolerance

    def setGoalDirectionDegrees(self,value):
        self.goal_direction_degrees = value

    def setCompassTolerance(self,value):
        self.compass_tolerance = value

    def __init__(self, motors_object, compass_object, environment_manager_object):

        #Check oggetto classe Motors
        if motors_object is None:
            raise Exception('Motors object cannot be null')
            return

        #Check oggetto classe Compass
        if compass_object is None:
            raise Exception('Compass object cannot be null')
            return

        #Check oggetto classe EnvironmentManager
        if environment_manager_object is None:
            raise Exception('EnvironmentManager object cannot be null')
            return

        #Reference istanza oggetto classe Motors
        self.motors_object = motors_object

        #Reference istanza oggetto classe Compass
        self.compass_object = compass_object

        #Reference istanza oggetto classe EnvironmentManager
        self.environment_manager_object = environment_manager_object

        self.motors_object.forward()

        Thread.__init__(self)
        self.deamon = True
        self.status = self.RUNNING
        self.start()

    def run(self):
        while self.status != self.STOPPED:
            time.sleep(0.05)

            try:

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
                        motor_right_actual_power = motor_right_actual_power - 1

                        if motor_right_actual_power >= 0:
                            self.motors_object.updateMotorPower( 'RIGHT', motor_right_actual_power )
                        else:
                            print( "STOPPING MOTORS.." )
                            self.motors_object.stop()
                            break
                    elif degrees - self.compass_tolerance > self.goal_direction_degrees:
                        print("Goal on the left")
                        motor_left_actual_power = motor_left_actual_power - 1

                        if motor_left_actual_power >= 0:
                            self.motors_object.updateMotorPower( 'LEFT', motor_left_actual_power )
                        else:
                            print( "STOPPING MOTORS.." )
                            self.motors_object.stop()
                            break
                    else: #Caso in cui obiettivo in posizione frontale
                        print("Goal on the front")
                        self.motors_object.forward( True )
            except Exception, e:
                print('RouteManager exception')
                raise Exception('RouteManager execption: ' + str(e))


    def stop(self):
        self.status = self.STOPPED
        print('Stopping RouteManager..')
