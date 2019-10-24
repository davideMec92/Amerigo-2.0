import RPi.GPIO as gpio
import time

#Settaggio impostazione GPIO
def init():
#Settaggio GPIO mediante dicitura BCM (numeri GPIO e non pin board)
 gpio.setmode(gpio.BCM)

#Settaggio iniziale gpio, con stato LOW

#MOTORE SINISTRO
 gpio.setup(12, gpio.OUT, initial = gpio.LOW) #IN1
 gpio.setup(16, gpio.OUT, initial = gpio.LOW) #IN2

#MOTORE DESTRO
 gpio.setup(20, gpio.OUT, initial = gpio.LOW) #IN3
 gpio.setup(21, gpio.OUT, initial = gpio.LOW) #IN4

def forward(sec):
 init()
 gpio.output(12, True)
 gpio.output(16, False)
 gpio.output(20, True) 
 gpio.output(21, False)
 time.sleep(sec)
 gpio.cleanup()

def reverse(sec):
 init()
 gpio.output(12, False)
 gpio.output(16, True)
# gpio.output(20, False) 
# gpio.output(21, True)
 time.sleep(sec)
 gpio.cleanup()

print "forward"
forward(4)
print "reverse"
reverse(2)
