import logging


# logging_config
def setup_logging():
    logging.basicConfig(filename='scraper.log',
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')