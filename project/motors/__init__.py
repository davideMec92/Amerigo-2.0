import time

class Motors:

    RIGHT_MOTOR_FORWARDS = 12
    RIGHT_MOTOR_BACKWARDS = 16

    LEFT_MOTOR_FORWARDS = 20
    LEFT_MOTOR_BACKWARDS = 21

    motor_right_gpio_forwards = None
    motor_right_gpio_backwards = None
    motor_left_gpio_forwards = None
    motor_left_gpio_backwards = None

    #Costanti stato motori
    STOPPED = 0
    FORWARD = 1
    BACKWARD = 2
    COUNTERCLOCKWISE_ROTATION = 3
    CLOCKWISE_ROTATION = 4

    motors_status = STOPPED
    motors_default_power = 40
    motor_left_actual_power = motors_default_power
    motor_right_actual_power = motors_default_power

    gpio = None

    def __init__(self, gpio):

        self.gpio = gpio

        #Settaggio GPIO mediante dicitura BCM (numeri GPIO e non pin board)
        """gpio.setmode(gpio.BCM)

        #Settaggio iniziale gpio, con stato LOW

        #MOTORE DESTRO
        gpio.setup(self.RIGHT_MOTOR_FORWARDS, gpio.OUT, initial = gpio.LOW) #IN1
        gpio.setup(self.RIGHT_MOTOR_BACKWARDS, gpio.OUT, initial = gpio.LOW) #IN2

        #MOTORE SINISTRO
        gpio.setup(self.LEFT_MOTOR_FORWARDS, gpio.OUT, initial = gpio.LOW) #IN3
        gpio.setup(self.LEFT_MOTOR_BACKWARDS, gpio.OUT, initial = gpio.LOW) #IN4"""

        #INZIALIZZAZIONE MOTORI
        self.motor_right_gpio_forwards = self.gpio.PWM(self.RIGHT_MOTOR_FORWARDS, 100)
        self.motor_right_gpio_backwards = self.gpio.PWM(self.RIGHT_MOTOR_BACKWARDS, 100)

        self.motor_left_gpio_forwards = self.gpio.PWM(self.LEFT_MOTOR_FORWARDS, 100)
        self.motor_left_gpio_backwards = self.gpio.PWM(self.LEFT_MOTOR_BACKWARDS, 100)

    def getMotorsStatus(self):
        return self.motors_status

    def getMotorsDefaultPower(self):
        return self.motors_default_power

    def getMotorLeftActualPower(self):
        return self.motor_left_actual_power

    def getMotorRightActualPower(self):
        return self.motor_right_actual_power

    def stop(self):

        self.motor_right_gpio_forwards.ChangeDutyCycle(0)
        self.motor_right_gpio_backwards.ChangeDutyCycle(0)
        self.motor_left_gpio_forwards.ChangeDutyCycle(0)
        self.motor_left_gpio_backwards.ChangeDutyCycle(0)

        self.motor_right_gpio_forwards.stop(0)
        self.motor_right_gpio_backwards.stop(0)
        self.motor_left_gpio_forwards.stop(0)
        self.motor_left_gpio_backwards.stop(0)

        self.motors_status = self.STOPPED

    def rotation(self, type, restoreToDefaultPower = False):

        if type == "COUNTERCLOCKWISE":

            if restoreToDefaultPower is False:
                self.motor_right_gpio_forwards.start(50)
                self.motor_left_gpio_backwards.start(50)
                time.sleep(0.10)

            self.motor_right_gpio_forwards.ChangeDutyCycle(int(self.motors_default_power))
            self.motor_left_gpio_backwards.ChangeDutyCycle(int(self.motors_default_power))
            self.motor_right_actual_power = self.motors_default_power
            self.motor_left_actual_power = self.motors_default_power
            self.motors_status = self.COUNTERCLOCKWISE_ROTATION

        elif type == "CLOCKWISE":

            if restoreMotorPower is False:
                self.motor_left_gpio_forwards.start(50)
                self.motor_right_gpio_backwards.start(50)
                time.sleep(0.10)

            self.motor_left_gpio_forwards.ChangeDutyCycle(int(self.motors_default_power))
            self.motor_right_gpio_backwards.ChangeDutyCycle(int(self.motors_default_power))
            self.motor_right_actual_power = self.motors_default_power
            self.motor_left_actual_power = self.motors_default_power
            self.motors_status = self.CLOCKWISE_ROTATION

    def forward(self, restoreToDefaultPower = False):

            if restoreToDefaultPower is False:
                self.motor_right_gpio_forwards.start(100)
                self.motor_left_gpio_forwards.start(100)
            else:
                self.motor_right_gpio_forwards.ChangeDutyCycle(int(self.motors_default_power))
                self.motor_left_gpio_forwards.ChangeDutyCycle(int(self.motors_default_power))
                self.motor_right_actual_power = self.motors_default_power
                self.motor_left_actual_power = self.motors_default_power

            self.motors_status = self.FORWARD

    def backward(self, restoreToDefaultPower = False):

            if restoreToDefaultPower is False:
                self.motor_right_gpio_backwards.start(100)
                self.motor_left_gpio_backwards.start(100)
            else:
                self.motor_right_gpio_backwards.ChangeDutyCycle(int(self.motors_default_power))
                self.motor_left_gpio_backwards.ChangeDutyCycle(int(self.motors_default_power))
                self.motor_right_actual_power = self.motors_default_power
                self.motor_left_actual_power = self.motors_default_power

            self.motors_status = self.BACKWARD

    def updateMotorPower(self, type, value):

        if type is None:
            return

        if value is None:
            return

        if value > 100 or value < 0:
            return

        #Check stato motori diverso da STOPPED
        if self.motors_status != self.STOPPED:

            if type == 'LEFT':

                #Check caso in cui stato motori sia FORWARD
                if self.motors_status == self.FORWARD:
                    self.motor_left_gpio_forwards.ChangeDutyCycle(int(value))
                elif self.motors_status == self.BACKWARD: #Check caso in cui stato motori sia BACKWARD
                    self.motor_left_gpio_backwards.ChangeDutyCycle(int(value))
                elif self.motors_status == self.CLOCKWISE_ROTATION: #Check caso in cui stato motori sia CLOCKWISE_ROTATION
                    self.motor_left_gpio_forwards.ChangeDutyCycle(int(value))
                elif self.motors_status == self.COUNTERCLOCKWISE_ROTATION: #Check caso in cui stato motori sia COUNTERCLOCKWISE_ROTATION
                    self.motor_left_gpio_backwards.ChangeDutyCycle(int(value))

                self.motor_left_actual_power = int(value)

            elif type == 'RIGHT':

                #Check caso in cui stato motori sia FORWARD
                if self.motors_status == self.FORWARD:
                    self.motor_right_gpio_forwards.ChangeDutyCycle(int(value))
                elif self.motors_status == self.BACKWARD: #Check caso in cui stato motori sia BACKWARD
                    self.motor_right_gpio_backwards.ChangeDutyCycle(int(value))
                elif self.motors_status == self.CLOCKWISE_ROTATION: #Check caso in cui stato motori sia CLOCKWISE_ROTATION
                    self.motor_right_gpio_backwards.ChangeDutyCycle(int(value))
                elif self.motors_status == self.COUNTERCLOCKWISE_ROTATION: #Check caso in cui stato motori sia COUNTERCLOCKWISE_ROTATION
                    self.motor_right_gpio_forwards.ChangeDutyCycle(int(value))

                self.motor_right_actual_power = int(value)
