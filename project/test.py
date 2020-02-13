#from compass import Compass
#from motors import Motors
#from proximity import Proximity
#from configurator import Configurator
from bluetooth_discoverer import BluetoothDiscoverer
import time

configurator = None

try :

    """configurator = Configurator()
    configurator.setGpio()
    time.sleep(2)

    motors = Motors( configurator.getGpio() )
    proximity = Proximity( configurator.getGpio(), configurator.getConf() )"""

    bluetooth_discoverer = BluetoothDiscoverer()
    bluetooth_discoverer.startInquiring()
    print( 'RESULT: ' + str( bluetooth_discoverer.getRssiStrength() ) )

    """print( "LEFT DIST: " + str( proximity.getDistance('FRONT') ) )

    while True:
        #time.sleep(0.05)
        print( "LEFT DIST: " + str( proximity.getDistance() ) )"""

    """motors = Motors()
    compass = Compass()

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
            break

    proximity = Proximity()

    print( "LEFT DIST: " + str( proximity.getDistance('FRONT') ) )
    #print( "LEFT DIST: " + str( proximity.getDistance() ) )"""

    """motors.forward()

    front_distance = None

    while True:

        distance = proximity.getDistance('FRONT').get('FRONT')
        print("Distance (FRONT): " + str( distance ))

        if distance == 'OUT_OF_RANGE':
            continue

        if distance <= 10:
            motors.stop()
            print("Obiettivo raggiunto")
            distance = proximity.getDistance('FRONT').get('FRONT')
            front_distance = distance
            #proximity.shutdown()
            motors.stop()
            print("Final Distance: " + str( distance ))
            break

    motors.rotation("COUNTERCLOCKWISE")

    front_distance = front_distance + 20

    while True:

        distance = proximity.getDistance('RIGHT').get('RIGHT')
        print("Distance (RIGHT): " + str( distance ))

        if distance == 'OUT_OF_RANGE':
            continue

        if distance <= front_distance:
            motors.stop()
            print("Obiettivo raggiunto")
            distance = proximity.getDistance('RIGHT').get('RIGHT')
            front_distance = distance
            #proximity.shutdown()
            motors.stop()
            print("Final Distance: " + str( distance ))
            break"""

except KeyboardInterrupt:
    # here you put any code you want to run before the program
    # exits when you press CTRL+C
    print("KeyboardInterrupt")
finally:

    if configurator is not None:
        configurator.gpioCleanup() # this ensures a clean exit
"""except:
    # this catches ALL other exceptions including errors.
    # You won't get any error messages for debugging
    # so only use it once your code is working
    print "Other error or exception occurred!"""
