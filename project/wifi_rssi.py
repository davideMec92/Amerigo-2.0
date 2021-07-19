import rssi
import time

interface = 'wlan0'
rssi_scanner = rssi.RSSI_Scan(interface)

ssids = ['Cacca', 'BruceNet']

# sudo argument automatixally gets set for 'false', if the 'true' is not set manually.
# python file will have to be run with sudo privileges.
while True:
    ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)
    time.sleep(0.3)
    print(ap_info)

