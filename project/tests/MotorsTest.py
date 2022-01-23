import time
import unittest

from project.configurator import Configurator
from project.enums.motors.RotationTypes import RotationTypes
from project.motors import Motors


class MotorsTest(unittest.TestCase):

    configurator: Configurator = None
    motors: Motors = None

    @classmethod
    def setUpClass(cls) -> None:
        print('Getting configuration..')
        cls.configurator = Configurator()

        print('Setting GPIO..')
        cls.configurator.setGpio()

        print('Starting and configuring Motors..')
        cls.motors = Motors(cls.configurator)

    @classmethod
    def tearDownClass(cls) -> None:
        if cls.configurator is not None:
            print('Cleaning up GPIO..')
            cls.configurator.gpioCleanup()

    def testForward(self):
        print('Starting motors forward..')
        self.motors.forward()
        time.sleep(2)
        print('Stopping motors forward..')
        self.motors.stop()
        self.assertEqual(True, True)  # add assertion here

    def testBackward(self):
        print('Starting motors backward..')
        self.motors.backward()
        time.sleep(2)
        print('Stopping motors backward..')
        self.motors.stop()
        self.assertEqual(True, True)  # add assertion here

    def testClockwiseRotation(self):
        print('Starting clockwise rotation..')
        self.motors.rotation(RotationTypes.CLOCKWISE)
        time.sleep(2)
        print('Stopping clockwise rotation..')
        self.motors.stop()
        self.assertEqual(True, True)  # add assertion here

    def testCounterClockwiseRotation(self):
        print('Starting counterclockwise rotation..')
        self.motors.rotation(RotationTypes.COUNTERCLOCKWISE)
        time.sleep(2)
        print('Stopping counterclockwise rotation..')
        self.motors.stop()
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
