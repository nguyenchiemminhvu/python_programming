import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s: %(levelname)s: %(filename)s:%(lineno)s: %(message)s',
    encoding='utf-8',
)
logging.info("Default logging configuration has been set up.")