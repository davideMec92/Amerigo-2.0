import logging
import os
from datetime import datetime
from enum import Enum
from path import Path

logFilesDir = Path.dirname(Path(__file__)) + '/Log/'
logging.basicConfig(filename=logFilesDir + datetime.now().strftime("%Y_%m_%d") + '.log', level=logging.DEBUG)

class LogLevels(Enum):
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4


class Logger:
    @staticmethod
    def createLog(logLevel: LogLevels, filename: str, message: str):
        if logLevel is None:
            raise Exception('"logLevel" cannot be None')

        if filename is None:
            raise Exception('"filename" cannot be None')

        if message is None:
            raise Exception('"message" cannot be None')

        message: str = '['+datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'], "' + os.path.basename(filename) + '", ' + message

        if logLevel == LogLevels.DEBUG:
            logging.debug(message)
        elif logLevel == LogLevels.INFO:
            logging.info(message)
        elif logLevel == LogLevels.WARNING:
            logging.warning(message)
        elif logLevel == LogLevels.ERROR:
            logging.error(message)
        elif logLevel == LogLevels.CRITICAL:
            logging.critical(message)
        else:
            raise Exception('The log level passed in not define')
