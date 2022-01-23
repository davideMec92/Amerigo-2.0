from threading import Thread
from dotenv import load_dotenv

class BaseSocketServerConnection(Thread):

    def __int__(self):
        self.isRunning = False
        self.connectionCallbacks:

        Thread.__init__(self)