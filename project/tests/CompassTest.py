import unittest

from project.compass import Compass


class CompassTest(unittest.TestCase):

    compass: Compass | None = None

    def testCompass(self):
        print('Starting Compass..')
        self.compass = Compass()
        measuredDegrees = str(self.compass.getDegress())
        print('Degrees: ' + measuredDegrees)
        self.assertTrue(measuredDegrees.replace('.','').isdigit())


if __name__ == '__main__':
    unittest.main()
