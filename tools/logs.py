import logging

def critical(msg):
    logger = logging.getLogger('common')
    logger.critical(msg)

def error(msg):
    logger = logging.getLogger('common')
    logger.error(msg)

def warning(msg):
    logger = logging.getLogger('common')
    logger.warning(msg)

def info(msg):
    logger = logging.getLogger('common')
    logger.info(msg)

def debug(msg):
    logger = logging.getLogger('common')
    logger.debug(msg)
