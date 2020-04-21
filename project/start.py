
#from EnvironmentManager import EnvironmentManager
from ProximityManager import ProximityManager
from RouteManager import RouteManager
from configurator import Configurator
from motors import Motors

from multiprocessing import Queue
from threading import Lock

try:

    multi_threading_lock = Lock()

    print('Getting configuration..')
    configurator = Configurator()

    print('Setting GPIO..')
    configurator.setGpio()

    print('Starting and configuring Motors..')
    motors = Motors( configurator )

    route_manager_queue = Queue( maxsize = 1 )

    #environment_manager = EnvironmentManager( route_manager_queue, multi_threading_lock )
    #print('Join environment_manager..')
    #environment_manager.join()
    proximity_manager = ProximityManager( configurator, motors )
    route_manager = RouteManager( motors, route_manager_queue, proximity_manager, multi_threading_lock )
    #print('Join route_manager..')
    #route_manager.join()
    raw_input("Press Enter to stop...")
except KeyboardInterrupt, SystemExit:
    print("Threads STOP")
except Exception, e:
    print("start.py Exception: " + str(e))
finally:

    """if environment_manager is not None:
        print('Stopping EnvironmentManager..')
        environment_manager.stop()"""

    if proximity_manager is not None:
        print('Stopping ProximityManager..')
        proximity_manager.stop()

    if route_manager is not None:
        print('Stopping RouteManager..')
        route_manager.stop()

    if configurator is not None:
        print('Cleaning up GPIO..')
        configurator.gpioCleanup()
