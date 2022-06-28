from logging.handlers import RotatingFileHandler
import logging
import time


def create_logger():
    log_formatter = logging.Formatter(
        '%(levelname)s %(lineno)4s => %(message)s ')

    logFile = './application.log'

    log_handler = RotatingFileHandler(
        logFile, mode='a', maxBytes=2 * 1024 * 1024, backupCount=1, encoding=None, delay=0)
    log_handler.setFormatter(log_formatter)
    log_handler.setLevel(logging.INFO)

    app_log = logging.getLogger('root')
    app_log.setLevel(logging.INFO)

    app_log.addHandler(log_handler)
    app_log.info("")
    app_log.info("============== Start of Execution at {}  =============".format(time.asctime()))
    return app_log


app_log = create_logger()


def function_logger(func):

    def log(*args, **kwargs):

        app_log.info("Starting function {} at {}".format(func.__name__, time.asctime()))
        return func(*args, **kwargs)
    return log
