import logging


logger = logging.getLogger('audit')


def log_event(event):
    logger.info(event)
