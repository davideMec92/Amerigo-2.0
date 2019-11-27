from compass import Compass
from motors import Motors
import time

motors = Motors()
compass = Compass()

degrees = compass.getDegress()
print("Start Degrees: " + str( degrees ))

time.sleep(2)

rotation_degress = 80
goal = degrees + rotation_degress

motors.rotation("COUNTERCLOCKWISE")

while True:
    degrees = compass.getDegress()
    print("Degrees: " + str( degrees ))

    if degrees >= goal:
        motors.stop()
        motors.shutdown()
        print("Obiettivo raggiunto")
        break
