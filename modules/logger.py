import logging
import logging.handlers
import json

def createLogger():
    with open("json_config/config.json") as config_file:
        config_dirs = json.load(config_file)

    logger = logging.getLogger('Media_Mover')
    logger.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler()
    syslog_handler = logging.handlers.SysLogHandler(address=(config_dirs['logger_ip'], config_dirs['logger_port']))
    syslog_handler.setLevel(logging.INFO)

    logger_formatter = logging.Formatter("%(name)s: %(levelname)s - %(message)s")
    stream_handler.setFormatter(logger_formatter)
    syslog_handler.setFormatter(logger_formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(syslog_handler)

    return logger