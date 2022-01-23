import py_qmc5883l

from project.custom_exceptions import *

class Compass:

    sensor = None

    def __init__(self):
        self.sensor = py_qmc5883l.QMC5883L()

    def getDegress(self):

        degrees = None

        try:
            degrees = self.sensor.get_bearing()
        except Exception as e:
            print(("Compass measurement Exception: " + str(e)))
            return None

        return degrees

    def getRotationDegreeCosts(self, start, arrive):

        if start is None:
            raise compassGetRotationDegreeCostsException('Parameter "start" cannot be None')

        if arrive is None:
            raise compassGetRotationDegreeCostsException('Parameter "arrive" cannot be None')

        result = {}
        clockwise_cost = 0
        counterclockwise_cost = 0

        phi = abs(arrive - start) % 360

        sign = None

        if (start - arrive >= 0 and start - arrive <= 180) or (start - arrive <=-180 and start- arrive >= -360):
            sign = 'positive' #counterclockwise
        else:
            sign = 'negative' #clockwise

        if phi > 180:

            if sign == 'negative':
                clockwise_cost = 360 - phi
                counterclockwise_cost = 360 - clockwise_cost
            else:
                counterclockwise_cost = 360 - phi
                clockwise_cost = 360 - counterclockwise_cost

        else:

            if sign == 'positive':
                counterclockwise_cost = phi
                clockwise_cost = 360 - counterclockwise_cost
            else:
                clockwise_cost = phi
                counterclockwise_cost = 360 - clockwise_cost

        result = { 'clockwise_cost' : int( clockwise_cost ), 'counterclockwise_cost' : int( counterclockwise_cost ) }

        return result
