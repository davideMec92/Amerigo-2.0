from motors import Motors
from compass import Compass
from configurator import Configurator
import time

print('Getting configuration..')
configurator = Configurator()

print('Setting GPIO..')
configurator.setGpio()

print('Starting and configuring Motors..')
motors = Motors(configurator)

# Reference istanza oggetto classe Compass
print('Starting Compass..')
compass = Compass()

stopRotationDegrees = 315

motors.rotation('COUNTERCLOCKWISE')

while True:
    degrees = compass.getDegress()
    print('Degrees: ' + str(degrees))

    if stopRotationDegrees - 5 <= degrees <= stopRotationDegrees + 5:
        print('Found stopRotationDegrees: ' + str(degrees))
        motors.stop()
        break

