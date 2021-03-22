import bluetooth

#sudo btmgmt find | awk '$3 == "B4:86:55:59:A2:E9" {print $7}' linux command to get rssi without connection

"""
Distance tests - approximates

-19 =  close (5cm)

-69 = across the room (1.5m)

-74 = in another room (8m)

-87 = outside (10m)

"""

class BluetoothManager(bluetooth.DeviceDiscoverer):

    def pre_inquiry(self):
        self.done = False

    def device_discovered(self, address, device_class, rssi, name):
        print("%s - %s" % (address, name))

        # get some information out of the device class and display it.
        # voodoo magic specified at:
        #
        # https://www.bluetooth.org/foundry/assignnumb/document/baseband
        major_classes = ("Miscellaneous",
                         "Computer",
                         "Phone",
                         "LAN/Network Access point",
                         "Audio/Video",
                         "Peripheral",
                         "Imaging")
        major_class = (device_class >> 8) & 0xf
        if major_class < 7:
            print("  %s" % major_classes[major_class])
        else:
            print("  Uncategorized")

        print("  services:")
        service_classes = ((16, "positioning"),
                           (17, "networking"),
                           (18, "rendering"),
                           (19, "capturing"),
                           (20, "object transfer"),
                           (21, "audio"),
                           (22, "telephony"),
                           (23, "information"))

        for bitpos, classname in service_classes:
            if device_class & (1 << (bitpos - 1)):
                print("    %s" % classname)
        print("  RSSI: " + str(rssi))

    def inquiry_complete(self):
        self.done = True

    #@staticmethod
    """def getNearbyDevices():
        print("Performing inquiry...")

        nearby_devices = bluetooth.discover_devices(duration=1, lookup_names=True, flush_cache=True, lookup_class=False)

        print("Found {} devices".format(len(nearby_devices)))

        for addr, name in nearby_devices:
            try:
                print("   {} - {}".format(addr, name))
            except UnicodeEncodeError:
                print("   {} - {}".format(addr, name.encode("utf-8", "replace")))"""

