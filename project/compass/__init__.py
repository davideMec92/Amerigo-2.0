import py_qmc5883l

class Compass:

    sensor = None

    def __init__(self):
        self.sensor = py_qmc5883l.QMC5883L()

    def getDegress(self):

        degrees = None

        try:
            degrees = self.sensor.get_bearing()
        except:
            print("Errore durante nik")
            return None

        return degrees

    def getRotationDegreeCosts(self, start, arrive):

        if start is None:
            raise Exception('Parameter "start" cannot be None')

        if arrive is None:
            raise Exception('Parameter "arrive" cannot be None')

        result = {}
        clockwise_cost = 0
        counterclockwise_cost = 0

        phi = abs(arrive - start) % 360

        if phi > 180:
            clockwise_cost = 360 - phi
            counterclockwise_cost = 360 - clockwise_cost
        else:
            counterclockwise_cost = phi
            clockwise_cost = 360 - counterclockwise_cost
        
        result = { 'clockwise_cost' : int( clockwise_cost ), 'counterclockwise_cost' : int( counterclockwise_cost ) }

        return result
