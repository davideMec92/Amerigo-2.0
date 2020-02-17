
from EnvironmentManager import EnvironmentManager

try:
    environmentManager = EnvironmentManager()
except KeyboardInterrupt, SystemExit:
    print("Thread STOP")
    environmentManager.stop()
