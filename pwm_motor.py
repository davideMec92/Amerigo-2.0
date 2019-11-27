import RPi.GPIO as gpio
import time

#Settaggio GPIO mediante dicitura BCM (numeri GPIO e non pin board)
gpio.setmode(gpio.BCM)

#Settaggio iniziale gpio, con stato LOW

#MOTORE SINISTRO
gpio.setup(12, gpio.OUT, initial = gpio.LOW) #IN1
gpio.setup(16, gpio.OUT, initial = gpio.LOW) #IN2

#MOTORE DESTRO
gpio.setup(20, gpio.OUT, initial = gpio.LOW) #IN3
gpio.setup(21, gpio.OUT, initial = gpio.LOW) #IN4

#INZIALIZZAZIONE MOTORI
motor1GPIO_FORWARDS = gpio.PWM(12, 100)
motor1GPIO_BACKWARDS = gpio.PWM(16, 100)

motor2GPIO_FORWARDS = gpio.PWM(20, 100)
motor2GPIO_BACKWARDS = gpio.PWM(21, 100)


#START MOTORI AL 50%
motor1GPIO_FORWARDS.start(40)
motor2GPIO_BACKWARDS.start(45)

time.sleep(2.22)

#STOP MOTORI E INVERSIONE ROTAZIONE

motor2GPIO_BACKWARDS.ChangeDutyCycle(0)
motor1GPIO_FORWARDS.ChangeDutyCycle(0)

motor2GPIO_BACKWARDS.stop(0)
motor1GPIO_FORWARDS.stop(0)

"""motor2GPIO_FORWARDS.start(40)
motor1GPIO_BACKWARDS.start(45)

time.sleep(2)

#STOP MOTORI
motor1GPIO_BACKWARDS.ChangeDutyCycle(0)
motor1GPIO_BACKWARDS.stop(0)

motor2GPIO_FORWARDS.ChangeDutyCycle(0)
motor2GPIO_FORWARDS.stop(0)"""

print("STOP")
#MOTORE SINISTRO
#gpio.output(12, True)
#gpio.output(16, False)

#MOTORE DESTRO
#gpio.output(20, False)
#gpio.output(21, True)


gpio.cleanup()
