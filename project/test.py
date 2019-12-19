from compass import Compass
from motors import Motors
from proximity import Proximity
import time

motors = Motors()
"""compass = Compass()

degrees = compass.getDegress()
print("Start Degrees: " + str( degrees ))

time.sleep(2)

rotation_degress = 180
tolerance = 5
goal = degrees - rotation_degress + tolerance

motors.rotation("COUNTERCLOCKWISE")
#motors.rotation("CLOCKWISE")

while True:
    degrees = compass.getDegress()
    #print("Degrees: " + str( degrees ))

    if degrees <= goal:
        motors.stop()
        motors.shutdown()
        print("Obiettivo raggiunto")
        degrees = compass.getDegress()
        print("Final Degrees: " + str( degrees ))
        break"""

proximity = Proximity()

print( "LEFT DIST: " + str( proximity.getDistance('FRONT') ) )
#print( "LEFT DIST: " + str( proximity.getDistance() ) )

motors.backward()
time.sleep(2)
motors.stop()
motors.forward()

front_distance = None

while True:

    distance = proximity.getDistance('FRONT').get('FRONT')
    print("Distance (FRONT): " + str( distance ))

    if distance <= 10:
        motors.stop()
        print("Obiettivo raggiunto")
        distance = proximity.getDistance('FRONT').get('FRONT')
        front_distance = distance
        #proximity.shutdown()
        #motors.shutdown()
        print("Final Distance: " + str( distance ))
        break

motors.rotation("COUNTERCLOCKWISE")

front_distance = front_distance + 20

while True:

    distance = proximity.getDistance('RIGHT').get('RIGHT')
    print("Distance (RIGHT): " + str( distance ))

    if distance <= front_distance:
        motors.stop()
        print("Obiettivo raggiunto")
        distance = proximity.getDistance('RIGHT').get('RIGHT')
        front_distance = distance
        #proximity.shutdown()
        motors.shutdown()
        print("Final Distance: " + str( distance ))
        break
