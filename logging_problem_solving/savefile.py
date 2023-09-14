import logging

# Create logger
logger = logging.getLogger(__name__)

# Create handlers and set levels
f_handler = logging.FileHandler('sf.log')
f_handler.setLevel(logging.DEBUG)

s_handler = logging.StreamHandler()
s_handler.setLevel(logging.DEBUG)

# Create formatter and add to handlers
f_format = logging.Formatter('%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)

s_format = logging.Formatter('%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(message)s')
s_handler.setFormatter(s_format)

# Add handlers to logger
logger.addHandler(f_handler)
logger.addHandler(s_handler)

# Application started
logger.debug("Demo started")
logger.info("Application started")
logger.warning("Please write documentation")
logger.error("Invalid arguments")
logger.critical("End of application")
