import RPi.GPIO as gpio

class Motors:

    RIGHT_MOTOR_FORWARDS = 12
    RIGHT_MOTOR_BACKWARDS = 16

    LEFT_MOTOR_FORWARDS = 20
    LEFT_MOTOR_BACKWARDS = 21

    motor_right_gpio_forwards = None
    motor_right_gpio_backwards = None
    motor_left_gpio_forwards = None
    motor_left_gpio_backwards = None

    def __init__(self):

        #Settaggio GPIO mediante dicitura BCM (numeri GPIO e non pin board)
        gpio.setmode(gpio.BCM)

        #Settaggio iniziale gpio, con stato LOW

        #MOTORE DESTRO
        gpio.setup(self.RIGHT_MOTOR_FORWARDS, gpio.OUT, initial = gpio.LOW) #IN1
        gpio.setup(self.RIGHT_MOTOR_BACKWARDS, gpio.OUT, initial = gpio.LOW) #IN2

        #MOTORE SINISTRO
        gpio.setup(self.LEFT_MOTOR_FORWARDS, gpio.OUT, initial = gpio.LOW) #IN3
        gpio.setup(self.LEFT_MOTOR_BACKWARDS, gpio.OUT, initial = gpio.LOW) #IN4

        #INZIALIZZAZIONE MOTORI
        self.motor_right_gpio_forwards = gpio.PWM(self.RIGHT_MOTOR_FORWARDS, 100)
        self.motor_right_gpio_backwards = gpio.PWM(self.RIGHT_MOTOR_BACKWARDS, 100)

        self.motor_left_gpio_forwards = gpio.PWM(self.LEFT_MOTOR_FORWARDS, 100)
        self.motor_left_gpio_backwards = gpio.PWM(self.LEFT_MOTOR_BACKWARDS, 100)

    def stop(self):

        self.motor_right_gpio_forwards.ChangeDutyCycle(0)
        self.motor_right_gpio_backwards.ChangeDutyCycle(0)
        self.motor_left_gpio_forwards.ChangeDutyCycle(0)
        self.motor_left_gpio_backwards.ChangeDutyCycle(0)

        self.motor_right_gpio_forwards.stop(0)
        self.motor_right_gpio_backwards.stop(0)
        self.motor_left_gpio_forwards.stop(0)
        self.motor_left_gpio_backwards.stop(0)

    def rotation(self, type):

        if type == "COUNTERCLOCKWISE":
            self.motor_right_gpio_forwards.start(45)
            self.motor_left_gpio_backwards.start(45)
        elif type == "CLOCKWISE":
            self.motor_left_gpio_forwards.start(45)
            self.motor_right_gpio_backwards.start(45)

    def shutdown(self):
        gpio.cleanup()
