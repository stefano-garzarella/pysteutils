import logging
import inspect
import datetime

class SteLogger:
    """
    Simple application logger (on file)

    Example:

    from pysteutils.stelogger import SteLogger

    # log file = AppName.log
    logger = SteLogger('AppName')
    logger.debug('test dbg msg')

    """
    logger = None

    def __init__(self, appname = 'stelogger'):
        """
        Constructor

        :type   appname: String
        :param  appname: application name (log stored in <appname>.log)
        """
        self.logger = logging.getLogger(appname)
        self.logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        fh = logging.FileHandler(appname + '.log')
        fh.setLevel(logging.DEBUG)
        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # add the handlers to the logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def error(self, msg = ''):
        """
        Log error message with filename, line, funcname

        :type   msg: String
        :param  msg: message to print
        """
        # get the previous frame in the stack
        func = inspect.currentframe().f_back.f_code
        self.logger.error("%s:%i %s(): %s" % (
                func.co_filename,
                func.co_firstlineno,
                func.co_name,
                msg,
        ))

    def debug(self, msg = ''):
        """
        Log debug message with filename, line, funcname

        :type   msg: String
        :param  msg: message to print
        """
        # get the previous frame in the stack
        func = inspect.currentframe().f_back.f_code
        self.logger.debug("%s:%i %s(): %s" % (
                func.co_filename,
                func.co_firstlineno,
                func.co_name,
                msg,
        ))

    def print(self, msg = ''):
        """
        Print message with time

        :type   msg: String
        :param  msg: message to print
        """
        now = str(datetime.datetime.now())
        print(now + ' - ' + msg)
        self.logger.info((msg))
