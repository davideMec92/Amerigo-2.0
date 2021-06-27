from ProximityManager import ProximityManager
from RouteManager import RouteManager
from configurator import Configurator
from motors import Motors
from MapAnalyzer import MapAnalyzer
from custom_exceptions import *
import sys

try:

    draw_map = False

    if len(sys.argv) > 1 and sys.argv[1].lower() == 'map':
        draw_map = True

    print('Getting configuration..')
    configurator = Configurator()

    print('Setting GPIO..')
    configurator.setGpio()

    print('Starting and configuring Motors..')
    motors = Motors( configurator )

    proximity_manager = ProximityManager( configurator, motors )

    route_manager = RouteManager( motors, proximity_manager )

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
