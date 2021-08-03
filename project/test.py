from ProximityManager import ProximityManager
from configurator import Configurator
from motors import Motors
import time

print('Getting configuration..')
configurator = Configurator()

print('Setting GPIO..')
configurator.setGpio()

print('Starting and configuring Motors..')
motors = Motors(configurator)

# Reference istanza oggetto classe ProximityManager
print('Starting ProximityManager..')
proximity_manager = ProximityManager(configurator, motors)

while True:
    print('Measurements: ' + str(proximity_manager.retrieveProximityData()))

