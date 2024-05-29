import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler
handler = logging.FileHandler('./test_automation.log')
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)