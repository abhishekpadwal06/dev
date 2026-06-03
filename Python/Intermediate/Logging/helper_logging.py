import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='app.log', filemode='w', datefmt='%d/%m/%Y %H:%M:%S')

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler("app.log")
logger.addHandler(file_handler)

logger.debug("DEBUG message")
logger.info("INFO message")
logger.warning("WARNING message")
logger.error("ERROR message")
logger.critical("CRITICAL message")