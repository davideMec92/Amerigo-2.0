import bluetooth
import select
import time

class BluetoothDiscoverer(bluetooth.DeviceDiscoverer):

    bluetooth_server_mac = 'B4:86:55:59:A2:E9'
    rssi = None
    callbackClassObject = None

    def pre_inquiry(self):
        self.done = False

    def device_discovered(self, address, device_class, rssi, name):
        print ("%s - %s - %s" % (address, name, rssi))

    def inquiry_complete(self):
        self.done = True

        if self.callbackClassObject is not None:
            print('SENDING RSSI STRENGTH TO CALLBACK OBJECT CLASS')
            self.callbackClassObject.setBluetoothServerRssiStrength( self.rssi )

    def _inquiry_complete (self):
        self.is_inquiring = False
        self.sock.close ()
        self.sock = None
        self.inquiry_complete()

    def _device_discovered (self, address, device_class,
            psrm, pspm, clockoff, rssi, name):

        #Check se trovato device server bluetooth
        if address is not None and rssi is not None and address == self.bluetooth_server_mac:

            if self.rssi != rssi:
                self.rssi = rssi

            self._inquiry_complete()

    def getRssiStrength(self):
        return self.rssi

    def getIsInquiring(self):
        return self.is_inquiring

    def startInquiring(self, callbackClassObject):

        try:

            self.callbackClassObject = callbackClassObject

            if self.is_inquiring == False:
                self.find_devices(False, 1, True,1)
                self.process_inquiry()

        except Exception as e:
            print('exception'+str(e))
            self.inquiry_complete()
