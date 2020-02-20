
from EnvironmentManager import EnvironmentManager

try:
    environmentManager = EnvironmentManager()
    raw_input("Press Enter to stop...")
    environmentManager.stop()
except KeyboardInterrupt, SystemExit:
    print("Thread STOP")
    environmentManager.stop()
