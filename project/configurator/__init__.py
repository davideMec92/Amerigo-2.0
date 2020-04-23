# -*- coding: utf-8 -*-

import pigpio as gpio
import json
from collections import namedtuple
from custom_exceptions import *

class Configurator:

    gpio = None
    conf = None
    configFilename = "conf.json"

    def __init__(self):
        self.conf = self.loadConf()

    def getRightMotorForwardsPin(self):
        return int(self.conf.get('Motors').get('RIGHT_MOTOR_FORWARDS'))

    def getLeftMotorForwardsPin(self):
        return int(self.conf.get('Motors').get('LEFT_MOTOR_FORWARDS'))

    def getRightMotorBackwardsPin(self):
        return int(self.conf.get('Motors').get('RIGHT_MOTOR_BACKWARDS'))

    def getLeftMotorBackwardsPin(self):
        return int(self.conf.get('Motors').get('LEFT_MOTOR_BACKWARDS'))

    def fileGetContents(self, filename):
        with open(filename) as f:
            return f.read()

    def loadConf(self):

        try:
            data = self.fileGetContents(self.configFilename)
            jsonData = None
            jsonData = json.loads(data)
            return jsonData
        except Exception, e:
            raise configuratorLoadConfException('^^^^^ Configurator Exception: ' + str(e) + ' ^^^^^')

    def getConf(self):
        return self.conf

    def getGpio(self):
        return self.gpio

    def setGpio(self):

        #Inizializzazione pigpio
        self.gpio = gpio.pi()

        self.gpio.exceptions = True

        if not self.gpio.connected:
            raise configuratorGpioInitializationException('^^^^^ Configurator Exception: cannot extabilish pigpio deamon connection ^^^^^')
            return

        #Settaggio iniziale gpio (Range valori PWM 0-255)

        #MOTORE DESTRO
        if self.gpio.set_PWM_dutycycle(self.conf.get('Motors').get('RIGHT_MOTOR_FORWARDS'),0) != 0:
            raise configuratorGpioInitializationException('Configurator error:  cannot initialize RIGHT_MOTOR_FORWARDS gpio')
            return

        if self.gpio.set_PWM_dutycycle(self.conf.get('Motors').get('RIGHT_MOTOR_BACKWARDS'),0) != 0:
            raise configuratorGpioInitializationException('Configurator error:  cannot initialize RIGHT_MOTOR_BACKWARDS gpio')
            return

        if self.gpio.set_PWM_dutycycle(self.conf.get('Motors').get('LEFT_MOTOR_FORWARDS'),0) != 0:
            raise configuratorGpioInitializationException('Configurator error:  cannot initialize LEFT_MOTOR_FORWARDS gpio')
            return

        if self.gpio.set_PWM_dutycycle(self.conf.get('Motors').get('LEFT_MOTOR_BACKWARDS'),0) != 0:
            raise configuratorGpioInitializationException('Configurator error:  cannot initialize LEFT_MOTOR_BACKWARDS gpio')
            return

    def gpioCleanup(self):
        self.gpio.stop()
