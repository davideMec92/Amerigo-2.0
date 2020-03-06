import pigpio
import time

class Proximity:

    triggers = None
    echoes = None
    sensor = None
    gpio = None

    triggers_mode = {}
    echoes_mode = {}

    ping = None
    high = None
    time = None
    triggered = None
    inited = None
    callback = None

    def __init__(self, configurator):

        if configurator is None:
            raise Exception('Proximity error: configurator element cannot be None')
            return

        if configurator.getGpio() is None:
            raise Exception('Proximity error: gpio element cannot be None')
            return

        self.gpio = configurator.getGpio()
        self.triggers = configurator.getConf().get('Proximity').get('Triggers')
        self.echoes = configurator.getConf().get('Proximity').get('Echoes')

        print('Proximity triggers initializing..')

        self.ping = False
        self.high = None
        self.time = None
        self.triggered = False

        #Settagio pin triggers
        for trigger in self.triggers:
            self.triggers_mode[trigger] = self.gpio.get_mode(self.triggers.get(trigger))
            self.gpio.set_mode(self.triggers.get(trigger), pigpio.OUTPUT)
            self.callback = self.gpio.callback(self.triggers.get(trigger), pigpio.EITHER_EDGE, self.callback_function)

        #Settagio pin echoes
        for echo in self.echoes:
            self.echoes_mode[echo] = self.gpio.get_mode(self.echoes.get(echo))
            self.gpio.set_mode(self.echoes.get(echo), pigpio.INPUT)
            self.callback = self.gpio.callback(self.echoes.get(echo), pigpio.EITHER_EDGE, self.callback_function)

        self.inited = True

    def callback_function(self, gpio, level, tick):

        if gpio == self.triggers.get('LEFT') or gpio == self.triggers.get('FRONT') or gpio == self.triggers.get('RIGHT'):

            if level == 0: # trigger sent

                self.triggered = True
                self.high = None
        else:

            if self.triggered:

                if level == 1:
                    self.high = tick
                else:
                    if self.high is not None:
                        self.time = tick - self.high
                        self.high = None
                        self.ping = True

    def read(self, trigger):

        if self.inited:
            self.ping = False
            self.gpio.gpio_trigger(trigger)
            start = time.time()

            while not self.ping:
                if (time.time()-start) > 5.0:
                    return 20000
                time.sleep(0.001)
            return self.time
        else:
            return None

    def cancel(self):

        if self.inited:
            self.inited = False
            self.callback.cancel()

            #Settagio pin triggers
            for trigger in self.triggers:
                self.gpio.set_mode(self.triggers.get(trigger), self.triggers_mode.get(trigger))

            #Settagio pin echoes
            for echo in self.echoes:
                self.gpio.set_mode(self.echoes.get(echo), self.echoes_mode.get(echo))

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

                TimeElapsed = self.read(triggers[i])

                distance = float( (TimeElapsed / 1000000.0 * 34030) / 2 )

                if sensor_orientation is not None:
                    data[sensor_orientation] = distance
                else:
                    if i == 0:
                        data['LEFT'] = distance
                    elif i == 1:
                        data['FRONT'] = distance
                    elif i == 2:
                        data['RIGHT'] = distance

        except Exception, e:
            print('Proximity exception: ' + str(e))
            return None

        return data
