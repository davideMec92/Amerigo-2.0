# -*- coding: utf-8 -*-

#from compass import Compass
from motors import Motors
from proximity import Proximity
from configurator import Configurator
#from bluetooth_discoverer import BluetoothDiscoverer
import time
import sys

configurator = None

try :

    configurator = Configurator()
    configurator.setGpio()

    time.sleep(1)

    """motors = Motors( configurator )
    print('Motors forward..')
    motors.forward()
    time.sleep(2)
    print('Motors stop..')
    motors.stop()"""

    proximity = Proximity( configurator )
    print('FINAL DESTINATIOOOONNNNNN DISTANCE: ' + str( proximity.getDistance() ))
    proximity.cancel()
    sys.exit()
    degrees_goal = 305
    compass_tolerance = 5

    compass = Compass()

    degrees = compass.getDegress()
    print("Start Degrees: " + str( degrees ))

    motors.forward()
    print("Motors forward started")

    while True:

        degrees = compass.getDegress()
        motor_left_actual_power = motors.getMotorLeftActualPower()
        motor_right_actual_power = motors.getMotorRightActualPower()

        print("Degrees: " + str( degrees ))
        print("Motor left actual power: " + str( motor_left_actual_power ))
        print("Motor right actual power: " + str( motor_right_actual_power ))

        #Caso in cui si è a sinistra dell'obiettivo
        if degrees + compass_tolerance < degrees_goal:
            print("Goal on the right")
            motor_right_actual_power = motor_right_actual_power - 1

            if motor_right_actual_power >= 0:
                motors.updateMotorPower( 'RIGHT', motor_right_actual_power )
            else:
                print( "STOPPING MOTORS.." )
                motors.stop()
                break
        elif degrees - compass_tolerance > degrees_goal:
            print("Goal on the left")
            motor_left_actual_power = motor_left_actual_power - 1

            if motor_left_actual_power >= 0:
                motors.updateMotorPower( 'LEFT', motor_left_actual_power )
            else:
                print( "STOPPING MOTORS.." )
                motors.stop()
                break
        else: #Caso in cui obiettivo in posizione frontale

            print("Goal on the front")
            motors.forward( True )


    """proximity = Proximity( configurator.getGpio(), configurator.getConf() )

    bluetooth_discoverer = BluetoothDiscoverer()
    bluetooth_discoverer.startInquiring()
    print( 'RESULT: ' + str( bluetooth_discoverer.getRssiStrength() ) )"""

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

    print('Finally')
    if configurator is not None:
        configurator.gpioCleanup() # this ensures a clean exit
"""except:
    # this catches ALL other exceptions including errors.
    # You won't get any error messages for debugging
    # so only use it once your code is working
    print "Other error or exception occurred!"""
