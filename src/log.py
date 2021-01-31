from logging import DEBUG, INFO, ERROR
import logging
import sys

class Log:
    def __init__(self, Name, Format="%(asctime)s | %(levelname)s | %(message)s ", level=INFO):
        #Logger configuration
        self.console_formater=logging.Formatter(Format)
        self.console_logger=logging.StreamHandler(sys.stdout)
        self.console_logger.setFormatter(self.console_formater)
        #Complete logging config.
        self.logger=logging.getLogger(name=Name)
        self.logger.setLevel(level)
        self.logger.addHandler(self.console_logger)

    def info(self,message):
        self.logger.info(message)

    def warning(self,message):
        self.logger.warning(message)
    
    def error(self,message):
        self.logger.error(message)

    def critical(self,message):
        self.logger.critical(message)
