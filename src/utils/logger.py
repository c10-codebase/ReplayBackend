from enum import IntEnum
import logging
import sys


class LogType(IntEnum):
    CRITICAL: int =0
    FATAL: int = 1
    ERROR: int = 2
    WARNING: int = 3
    WARN:int = 4
    INFO: int = 5
    DEBUG:int = 6
    EXCEPTION: int = 7
    

class Logger:
    
    @staticmethod
    def log(type:LogType, *args, **kwargs):
        arguments = [str(item) for item in args]
        message = ",".join(arguments) if arguments else ""
        message = (message + ", ".join(f"{key}={str(value)}" for key,value in kwargs.items())) if kwargs else message
        
        logSwitch = {
            LogType.DEBUG: logging.debug,
            LogType.INFO: logging.info,
            LogType.CRITICAL: logging.critical,
            LogType.FATAL: logging.fatal,
            LogType.ERROR: logging.error,
            LogType.WARNING: logging.warning,
            LogType.WARN: logging.warn,
            LogType.EXCEPTION: logging.exception
        }
        
        _log = logSwitch.get(type, logging.info)
        _log(message)