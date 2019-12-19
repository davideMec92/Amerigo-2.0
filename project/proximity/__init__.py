import RPi.GPIO as gpio
import time

class Proximity:

    gpio.setmode(gpio.BCM)
    triggers = {"LEFT": 5, "FRONT": 6, "RIGHT": 13}
    echoes = {"LEFT": 17, "FRONT": 27, "RIGHT": 22}
    sensor = None

    def __init__(self):

        for trigger in self.triggers:
          gpio.setup(self.triggers[ trigger ], gpio.OUT)

        for echo in self.echoes:
          gpio.setup(self.echoes[ echo ], gpio.IN)

    def getDistance(self, sensor_orientation = None):

        triggers = []
        echoes = []
        data = {}

        try:

            if sensor_orientation is not None:

                if sensor_orientation == 'LEFT':
                    triggers.append(self.triggers['LEFT'])
                    echoes.append(self.echoes['LEFT'])
                elif sensor_orientation == 'FRONT':
                    triggers.append(self.triggers['FRONT'])
                    echoes.append(self.echoes['FRONT'])
                elif sensor_orientation == 'RIGHT':
                    triggers.append(self.triggers['RIGHT'])
                    echoes.append(self.echoes['RIGHT'])
            else:

                triggers.append(self.triggers['LEFT'])
                echoes.append(self.echoes['LEFT'])
                triggers.append(self.triggers['FRONT'])
                echoes.append(self.echoes['FRONT'])
                triggers.append(self.triggers['RIGHT'])
                echoes.append(self.echoes['RIGHT'])

            for i in range(len(triggers)):

                # set Trigger to HIGH
                gpio.output(triggers[i], True)

                # set Trigger after 0.01ms to LOW
                time.sleep(0.00001)
                gpio.output(triggers[i], False)

                StartTime = time.time()
                StopTime = time.time()

                # save StartTime
                while gpio.input(echoes[i]) == 0:
                    StartTime = time.time()

                # save time of arrival
                while gpio.input(echoes[i]) == 1:
                    StopTime = time.time()

                # time difference between start and arrival
                TimeElapsed = StopTime - StartTime
                # multiply with the sonic speed (34300 cm/s)
                # and divide by 2, because there and back
                distance = (TimeElapsed * 34300) / 2

                if sensor_orientation is not None:
                    data[sensor_orientation] = distance
                else:
                    if i == 0:
                        data['LEFT'] = distance
                    elif i == 1:
                        data['FRONT'] = distance
                    elif i == 2:
                        data['RIGHT'] = distance
        except:
            print("Errore durante Proximity")
            return None

        return data

    def shutdown(self):
        gpio.cleanup()
