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
