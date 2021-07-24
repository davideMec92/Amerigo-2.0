from wifi_rssi_manager import WifiRssiManager
import time

wifiRssiManager = WifiRssiManager()
wifiRssiManager.setSsids(['2e97ca47-9741-44eb-9099-f5682b', 'e5551ca3-a3a3-4288-870d-ddab6d'])
wifiRssiManager.start()

while True:
    print('LEVEL: ' + str(wifiRssiManager.checkIfSsidIsNearToMe('2e97ca47-9741-44eb-9099-f5682b')))
