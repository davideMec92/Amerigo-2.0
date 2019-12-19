import py_qmc5883l
import time

sensor = py_qmc5883l.QMC5883L()
#sensor.declination = 3.15
#sensor.calibration = [[1.001924343474609, -0.007879196754770956, -1807.778072637528], [-0.007879196754770959, 1.0322612580963557, 617.6182936841687], [0.0, 0.0, 1.0]]
#sensor.set_calibration(c)
#sensor_calibration = sensor.get_calibration()
#print( "sensor_calibration: " + str( sensor_calibration ) )

while True:
    m = sensor.get_bearing()
    print(m)
    time.sleep(0.25)
