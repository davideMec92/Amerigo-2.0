#Libraries
import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

triggers = {"LEFT": 5, "FRONT": 6, "RIGHT": 13}
echos = {"LEFT": 17, "FRONT": 27, "RIGHT": 22}

print("Initializing sensors..")

for trigger in triggers:
  GPIO.setup(triggers[ trigger ], GPIO.OUT)

for echo in echos:
  GPIO.setup(echos[ echo ], GPIO.IN)

def distance( sensor_type ):

    if sensor_type is None:
        return

    trigger = None
    echo = None

    if sensor_type == 'LEFT':
        trigger = triggers['LEFT']
        echo = echos['LEFT']
    elif sensor_type == 'FRONT':
        trigger = triggers['FRONT']
        echo = echos['FRONT']
    elif sensor_type == 'RIGHT':
        trigger = triggers['RIGHT']
        echo = echos['RIGHT']

    print("Trigger: " + str( trigger ))
    print("Echo: " + str( echo ))

    # set Trigger to HIGH
    GPIO.output(trigger, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(trigger, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(echo) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(echo) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

try:
    while True:

        print( "Left distance: %.1f cm" % distance('LEFT') )
        print( "Front distance: %.1f cm" % distance('FRONT') )
        print( "Right distance: %.1f cm" % distance('RIGHT') )
        time.sleep(3)

    # Reset by pressing CTRL + C
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
