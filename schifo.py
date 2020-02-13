import bluetooth
import select
import time

class MyDiscoverer(bluetooth.DeviceDiscoverer):

    bluetooth_server_mac = 'B4:86:55:59:A2:E9'
    rssi = None

    def pre_inquiry(self):
        self.done = False

    def device_discovered(self, address, device_class, rssi, name):
        print ("%s - %s - %s" % (address, name, rssi))

    def inquiry_complete(self):
        self.done = True
        return self.rssi

    def _inquiry_complete (self):
        """
        Called when an inquiry started by find_devices has completed.
        """
        self.is_inquiring = False
        self.sock.close ()
        self.sock = None
        self.inquiry_complete()

    def _device_discovered (self, address, device_class,
            psrm, pspm, clockoff, rssi, name):

        if address is not None and rssi is not None and address == self.bluetooth_server_mac:
            print('1 RSSI: ' + str( rssi ))

            if self.rssi != rssi:
                self.rssi = rssi

            self._inquiry_complete()

    def getRssiStrength(self):
        return self.rssi

    def getIsInquiring(self):
        return self.is_inquiring

d = MyDiscoverer()

try:
    while True:

        time.sleep(0.7)

        if d.getIsInquiring() == False:
            d.find_devices(False, 1, True,1)
            d.process_inquiry()
            print('2 RSSI: ' + str(d.getRssiStrength()))

except KeyboardInterrupt:
    print("INQUIRY STOP")
    d.inquiry_complete()

"""print('RESULT: ' + str(result))

readfiles = [ d, ]

while True:
    rfds = select.select( readfiles, [], [] )[0]

    if d in rfds:
        d.process_inquiry()
        #d.process_event()

    if d.done: break"""
