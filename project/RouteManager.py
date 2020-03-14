# -*- coding: utf-8 -*-

from compass import Compass
from threading import Thread

import time

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

    queue = None

    def getGoalDirectionDegrees(self):
        return self.goal_direction_degrees

    def getCompassTolerance(self):
        return self.compass_tolerance

    def setGoalDirectionDegrees(self,value):
        self.goal_direction_degrees = value

    def setCompassTolerance(self,value):
        self.compass_tolerance = value

    def __init__(self, motors_object, queue):

        #Check oggetto classe Motors
        if motors_object is None:
            raise Exception('Motors object cannot be null')
            return

        #Reference istanza oggetto classe Motors
        self.motors_object = motors_object

        #Reference istanza oggetto classe Compass
        print('Starting Compass..')
        self.compass_object = Compass()

        self.queue = queue

        Thread.__init__(self)
        self.deamon = True
        self.status = self.RUNNING
        self.motors_object.forward()
        self.start()

    def run(self):

        while self.status != self.STOPPED:

            if self.queue.full() is not True:
                print('RouteManager Return')
                time.sleep(0.05)
                continue

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

                    print('Queue get')
                    data = self.queue.get()

            except Exception, e:
                print('RouteManager exception')
                raise Exception('RouteManager execption: ' + str(e))


    def stop(self):

        print('Stopping RouteManager..')

        self.status = self.STOPPED

        if self.motors_object is not None and self.motors_object.getMotorsStatus() != self.motors_object.STOPPED:
            print('Stopping motors..')
            self.motors_object.stop()
