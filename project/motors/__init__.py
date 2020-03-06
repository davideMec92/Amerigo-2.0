import time

class Motors:

    #Costanti stato motori
    STOPPED = 0
    FORWARD = 1
    BACKWARD = 2
    COUNTERCLOCKWISE_ROTATION = 3
    CLOCKWISE_ROTATION = 4

    motors_status = STOPPED
    motors_default_power = 35
    motor_left_actual_power = motors_default_power
    motor_right_actual_power = motors_default_power

    gpio = None
    configurator = None

    def __init__(self, configurator):

        if configurator is None:
            raise Exception('Motors error: configurator element cannot be None')
            return

        if configurator.getGpio() is None:
            raise Exception('Motors error: gpio element cannot be None')
            return

        self.configurator = configurator
        self.gpio = self.configurator.getGpio()

    def getMotorsStatus(self):
        return self.motors_status

    def getMotorsDefaultPower(self):
        return self.motors_default_power

    def getMotorLeftActualPower(self):
        return self.motor_left_actual_power

    def getMotorRightActualPower(self):
        return self.motor_right_actual_power

    def stop(self):

        self.gpio.set_PWM_dutycycle(self.configurator.getRightMotorForwardsPin(), 0)
        self.gpio.set_PWM_dutycycle(self.configurator.getRightMotorBackwardsPin(), 0)
        self.gpio.set_PWM_dutycycle(self.configurator.getLeftMotorForwardsPin(), 0)
        self.gpio.set_PWM_dutycycle(self.configurator.getLeftMotorBackwardsPin(), 0)

        self.motors_status = self.STOPPED

    def rotation(self, type, restoreToDefaultPower = False):

        if type == "COUNTERCLOCKWISE":

            if restoreToDefaultPower is False:
                self.gpio.set_PWM_dutycycle(self.configurator.getRightMotorForwardsPin(), 100)
                self.gpio.set_PWM_dutycycle(self.configurator.getLeftMotorBackwardsPin(), 100)
                time.sleep(0.10)

            self.gpio.set_PWM_dutycycle(self.configurator.getRightMotorForwardsPin(), int(self.motors_default_power))
            self.gpio.set_PWM_dutycycle(self.configurator.getLeftMotorBackwardsPin(), int(self.motors_default_power))

            self.motor_right_actual_power = self.motors_default_power
            self.motor_left_actual_power = self.motors_default_power
            self.motors_status = self.COUNTERCLOCKWISE_ROTATION

        elif type == "CLOCKWISE":

            if restoreToDefaultPower is False:
                self.gpio.set_PWM_dutycycle(self.configurator.getLeftMotorForwardsPin(), 100)
                self.gpio.set_PWM_dutycycle(self.configurator.getRightMotorBackwardsPin(), 100)
                time.sleep(0.10)

            self.gpio.set_PWM_dutycycle(self.configurator.getLeftMotorForwardsPin(), int(self.motors_default_power))
            self.gpio.set_PWM_dutycycle(self.configurator.getRightMotorBackwardsPin(), int(self.motors_default_power))

            self.motor_right_actual_power = self.motors_default_power
            self.motor_left_actual_power = self.motors_default_power
            self.motors_status = self.CLOCKWISE_ROTATION

    def forward(self, restoreToDefaultPower = False):

            if restoreToDefaultPower is False:
                self.gpio.set_PWM_dutycycle(self.configurator.getRightMotorForwardsPin(), 200)
                self.gpio.set_PWM_dutycycle(self.configurator.getLeftMotorForwardsPin(), 200)
            else:
                self.gpio.set_PWM_dutycycle(self.configurator.getRightMotorForwardsPin(), int(self.motors_default_power))
                self.gpio.set_PWM_dutycycle(self.configurator.getLeftMotorForwardsPin(), int(self.motors_default_power))

                self.motor_right_actual_power = self.motors_default_power
                self.motor_left_actual_power = self.motors_default_power

            self.motors_status = self.FORWARD

    def backward(self, restoreToDefaultPower = False):

            if restoreToDefaultPower is False:
                self.gpio.set_PWM_dutycycle(self.configurator.getRightMotorBackwardsPin(), 100)
                self.gpio.set_PWM_dutycycle(self.configurator.getLeftMotorBackwardsPin(), 100)
            else:
                self.gpio.set_PWM_dutycycle(self.configurator.getRightMotorBackwardsPin(), int(self.motors_default_power))
                self.gpio.set_PWM_dutycycle(self.configurator.getLeftMotorBackwardsPin(), int(self.motors_default_power))

                self.motor_right_actual_power = self.motors_default_power
                self.motor_left_actual_power = self.motors_default_power

            self.motors_status = self.BACKWARD

    def updateMotorPower(self, type, value):

        if type is None:
            return

        if value is None:
            return

        if value > 255 or value < 0:
            return

        #Check stato motori diverso da STOPPED
        if self.motors_status != self.STOPPED:

            if type == 'LEFT':

                #Check caso in cui stato motori sia FORWARD
                if self.motors_status == self.FORWARD:
                    self.gpio.set_PWM_dutycycle(self.configurator.getLeftMotorForwardsPin(), int(value))
                elif self.motors_status == self.BACKWARD: #Check caso in cui stato motori sia BACKWARD
                    self.gpio.set_PWM_dutycycle(self.configurator.getLeftMotorBackwardsPin(), int(value))
                elif self.motors_status == self.CLOCKWISE_ROTATION: #Check caso in cui stato motori sia CLOCKWISE_ROTATION
                    self.gpio.set_PWM_dutycycle(self.configurator.getLeftMotorForwardsPin(), int(value))
                elif self.motors_status == self.COUNTERCLOCKWISE_ROTATION: #Check caso in cui stato motori sia COUNTERCLOCKWISE_ROTATION
                    self.gpio.set_PWM_dutycycle(self.configurator.getLeftMotorBackwardsPin(), int(value))

                self.motor_left_actual_power = int(value)

            elif type == 'RIGHT':

                #Check caso in cui stato motori sia FORWARD
                if self.motors_status == self.FORWARD:
                    self.gpio.set_PWM_dutycycle(self.configurator.getRightMotorForwardsPin(), int(value))
                elif self.motors_status == self.BACKWARD: #Check caso in cui stato motori sia BACKWARD
                    self.gpio.set_PWM_dutycycle(self.configurator.getRightMotorBackwardsPin(), int(value))
                elif self.motors_status == self.CLOCKWISE_ROTATION: #Check caso in cui stato motori sia CLOCKWISE_ROTATION
                    self.gpio.set_PWM_dutycycle(self.configurator.getRightMotorBackwardsPin(), int(value))
                elif self.motors_status == self.COUNTERCLOCKWISE_ROTATION: #Check caso in cui stato motori sia COUNTERCLOCKWISE_ROTATION
                    self.gpio.set_PWM_dutycycle(self.configurator.getRightMotorForwardsPin(), int(value))

                self.motor_right_actual_power = int(value)
