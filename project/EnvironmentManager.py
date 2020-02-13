
from bluetooth_discoverer import BluetoothDiscoverer

from threading import Thread
import time

class EnvironmentManager( Thread ):

    bluetooth_server_rssi_streght = None
    bluetooth_discoverer = None
    stopT = False

    def __init__(self):
        Thread.__init__(self)
        self.deamon = True
        self.start()
        self.bluetooth_discoverer = BluetoothDiscoverer()

    def run(self):
        while self.stopT is False:
            time.sleep(0.7)
            print('RUN')
            self.bluetooth_discoverer.startInquiring(self)

    def setBluetoothServerRssiStrength(self, value):
        print('SET BLUETOOTH SERVER RSSI STRENGTH TO: ' + str( value ))
        self.bluetooth_server_rssi_streght = value

    def stop(self):
        self.stopT = True


try:
    environmentManager = EnvironmentManager()
except KeyboardInterrupt:
    print("Thread STOP")
    environmentManager.stop()
