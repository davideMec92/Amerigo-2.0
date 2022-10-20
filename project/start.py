import os
import traceback

from dotenv import load_dotenv
from compass import Compass
from ProximityManager import ProximityManager
from RouteManager import RouteManager
from configurator import Configurator
from motors import Motors
from MapAnalyzer import MapAnalyzer
from custom_exceptions import *
from positions_degrees_manager import PositionsDegreesManager
from project.hashgraph.managers.services.BluetoothConnectionManager import BluetoothConnectionManager
from project.hashgraph.models.communication.CommunicationMessageLogin import CommunicationMessageLogin
from project.hashgraph.services.bluetooth.BluetoothSocketConnection import BluetoothSocketConnection
from wifi_rssi_manager import WifiRssiManager
import sys
import time

load_dotenv()

try:
    draw_map = False

    if len(sys.argv) > 1 and sys.argv[1].lower() == 'map':
        draw_map = True

    print('Getting configuration..')
    configurator = Configurator()

    print('Starting pigpio daemon..')
    os.system('sudo pigpiod')

    print('Setting GPIO..')
    configurator.setGpio()

    print('Starting and configuring Motors..')
    motors = Motors( configurator )

    print('Asking to server the positions degrees list..')
    positionsDegreesManager = PositionsDegreesManager()

    print('Starting Compass..')
    compass = Compass()

    startingSsidPosition = None

    wifiRssiManager = WifiRssiManager()

    while positionsDegreesManager.getPositionsDegreesFromServer() is False or startingSsidPosition is None:
        wifiRssiManager.setSsids(positionsDegreesManager.getPositionDegreesDevicesIds())
        startingSsidPosition = wifiRssiManager.getSsidNearToMe()
        time.sleep(2)
        # time.sleep(3)

    print('startingSsidPosition: ' + str(startingSsidPosition))
    print('Starting wifi manager rssi continuos scan..')
    wifiRssiManager.start()
    
    print('Positions degrees list found!')

    bluetoothConnectionManager: BluetoothConnectionManager = BluetoothConnectionManager.getInstance()

    # Create login communication message
    communicationMessageLogin: CommunicationMessageLogin = CommunicationMessageLogin()
    communicationMessageLogin.deviceId = os.getenv('DEVICE_ID')

    # Create socket to send login request to server
    bluetoothSocketConnection: BluetoothSocketConnection = bluetoothConnectionManager.newBluetoothSocketConnection(
        os.getenv('BluetoothServerUUID'), os.getenv('BluetoothServerBluetoothMAC'), True)

    # Send login request message to server
    bluetoothSocketConnection.sendNewMessage(communicationMessageLogin)

    proximity_manager = ProximityManager( configurator, motors )

    route_manager = RouteManager( compass, motors, proximity_manager, wifiRssiManager, positionsDegreesManager, startingSsidPosition)
    route_manager.start()

    input("Press Enter to stop...")

except KeyboardInterrupt as SystemExit:
    print("Threads STOP")
except configuratorLoadConfException as e:
    print(e)
except motorsInitializationException as e:
    print(e)
except proximityInitializationException as e:
    print(e)
except mapAnalyzerInitializationException as e:
    print(e)
except mapAnalyzerPlotBuildException as e:
    print(e)
except Exception as e:
    print(("start.py Exception: " + str(e)))
    traceback.print_exc()
finally:

    if proximity_manager is not None:
        print('Stopping ProximityManager..')
        proximity_manager.stop()

    if route_manager is not None:
        print('Stopping RouteManager..')
        route_manager.stop()

    if configurator is not None:
        print('Cleaning up GPIO..')
        configurator.gpioCleanup()

    if draw_map is True:
        print('Creating plots..')
        map_analyzer = MapAnalyzer()
        map_analyzer.plotMaps()
