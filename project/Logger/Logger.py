import logging
import os
from datetime import datetime
from enum import Enum

from path import Path

logFilesDir = Path.dirname(Path(__file__)) + '/Log/'
logging.basicConfig(filename=logFilesDir + datetime.now().strftime("%Y_%m_%d") + '.log', encoding='utf-8', level=logging.DEBUG)

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

        match logLevel:
            case LogLevels.DEBUG:
                logging.debug(message)
            case LogLevels.INFO:
                logging.info(message)
            case LogLevels.WARNING:
                logging.warning(message)
            case LogLevels.ERROR:
                logging.error(message)
            case LogLevels.CRITICAL:
                logging.critical(message)
            case _:
                raise Exception('The log level passed in not define')
