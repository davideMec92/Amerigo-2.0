
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
    proximity_manager = ProximityManager( configurator, motors, proximity_manager_queue )
    route_manager = RouteManager( motors, route_manager_queue )
    raw_input("Press Enter to stop...")
    environment_manager.stop()
    proximity_manager.stop()
    route_manager.stop()
    configurator.gpioCleanup()
except KeyboardInterrupt, SystemExit:
    print("Thread STOP")
    environment_manager.stop()
    proximity_manager.stop()
    route_manager.stop()
    configurator.gpioCleanup()
