import unittest

from project.ProximityManager import ProximityManager
from project.configurator import Configurator
from project.motors import Motors


class ProximityTest(unittest.TestCase):

    configurator: Configurator | None = None
    motors: Motors | None = None
    proximity_manager: ProximityManager | None = None

    @classmethod
    def setUpClass(cls) -> None:
        print('Getting configuration..')
        cls.configurator = Configurator()

        print('Setting GPIO..')
        cls.configurator.setGpio()

        print('Starting and configuring Motors..')
        cls.motors = Motors(cls.configurator)

        print('Starting ProximityManager..')
        cls.proximity_manager = ProximityManager(cls.configurator, cls.motors)

    @classmethod
    def tearDownClass(cls) -> None:
        if cls.proximity_manager is not None:
            print('Stopping ProximityManager..')
            cls.proximity_manager.stop()

        if cls.configurator is not None:
            print('Cleaning up GPIO..')
            cls.configurator.gpioCleanup()

    def testRetrieveProximityData(self):
        print('Reading proximity data from sensors...')
        self.proximity_manager.retrieveProximityData()
        proximityData = self.proximity_manager.measurements
        print('DATA: ' + str(proximityData))
        self.assertFalse(not proximityData)
        self.assertTrue(proximityData['LEFT'] is not None and str(proximityData['LEFT']).replace('.','').isdecimal())
        self.assertTrue(proximityData['FRONT'] is not None and str(proximityData['FRONT']).replace('.','').isdecimal())
        self.assertTrue(proximityData['RIGHT'] is not None and str(proximityData['RIGHT']).replace('.','').isdecimal())


if __name__ == '__main__':
    unittest.main()
