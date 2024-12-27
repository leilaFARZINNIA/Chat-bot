import logging

def setup_logging(logging_enabled, log_level):
    if logging_enabled:
        log_level = logging.INFO if log_level == 'INFO' else logging.WARNING
        logging.basicConfig(
            filename='app.log',
            level=log_level,
            # format='%(asctime)s - %(levelname)s - %(message)s'
            format='%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - Line: %(lineno)d - %(message)s'
        )
        logging.info('Logging is enabled.')
    else:
        logging.basicConfig(level=logging.CRITICAL)  # Disable logging
