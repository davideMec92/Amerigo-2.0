import RPi.GPIO as gpio
import json
from collections import namedtuple

class Configurator:

    gpio = None
    conf = None
    configFilename = "conf.json"

    def __init__(self):
        self.conf = self.loadConf()

    def fileGetContents(self, filename):
        with open(filename) as f:
            return f.read()

    def loadConf(self):
        data = self.fileGetContents(self.configFilename)
        jsonData = None
        jsonData = json.loads(data)
        return jsonData

    def getConf(self):
        return self.conf

    def getGpio(self):
        return self.gpio

    def setGpio(self):

        self.gpio = gpio

        #Settaggio GPIO mediante dicitura BCM (numeri GPIO e non pin board)
        self.gpio.setmode(gpio.BCM)
        #self.gpioCleanup()

        #Settaggio iniziale gpio, con stato LOW

        #MOTORE DESTRO
        self.gpio.setup(self.conf.get('Motors').get('RIGHT_MOTOR_FORWARDS'), gpio.OUT, initial = gpio.LOW) #IN1
        self.gpio.setup(self.conf.get('Motors').get('RIGHT_MOTOR_BACKWARDS'), gpio.OUT, initial = gpio.LOW) #IN2

        #MOTORE SINISTRO
        self.gpio.setup(self.conf.get('Motors').get('LEFT_MOTOR_FORWARDS'), gpio.OUT, initial = gpio.LOW) #IN3
        self.gpio.setup(self.conf.get('Motors').get('LEFT_MOTOR_BACKWARDS'), gpio.OUT, initial = gpio.LOW) #IN4

        #SETTAGGIO PROXIMITY SENSORS
        for trigger in self.conf.get('Proximity').get('Triggers'):
          gpio.setup(self.conf.get('Proximity').get('Triggers')[ trigger ], gpio.OUT)

        for echo in self.conf.get('Proximity').get('Echoes'):
          gpio.setup(self.conf.get('Proximity').get('Echoes')[ echo ], gpio.IN)

        print("TEST")

    def gpioCleanup(self):
        self.gpio.cleanup()
