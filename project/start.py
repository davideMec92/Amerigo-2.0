
from EnvironmentManager import EnvironmentManager
from ProximityManager import ProximityManager
from RouteManager import RouteManager
from configurator import Configurator
from motors import Motors

from multiprocessing import Queue

try:
    print('Getting configuration..')
    configurator = Configurator()

    print('Setting GPIO..')
    configurator.setGpio()

    print('Starting and configuring Motors..')
    motors = Motors( configurator )

    proximity_manager_queue = Queue( maxsize = 1 )
    route_manager_queue = Queue( maxsize = 1 )

    environment_manager = EnvironmentManager( proximity_manager_queue, route_manager_queue )
    #print('Join environment_manager..')
    #environment_manager.join()
    proximity_manager = ProximityManager( configurator, motors, proximity_manager_queue )
    #print('Join proximity_manager..')
    #proximity_manager.join()
    route_manager = RouteManager( motors, route_manager_queue, proximity_manager )
    #print('Join route_manager..')
    #route_manager.join()
    raw_input("Press Enter to stop...")
except KeyboardInterrupt, SystemExit:
    print("Threads STOP")
finally:

    if environment_manager is not None:
        print('Stopping EnvironmentManager..')
        environment_manager.stop()

    if proximity_manager is not None:
        print('Stopping ProximityManager..')
        proximity_manager.stop()

    if route_manager is not None:
        print('Stopping RouteManager..')
        route_manager.stop()

    if configurator is not None:
        print('Cleaning up GPIO..')
        configurator.gpioCleanup()
