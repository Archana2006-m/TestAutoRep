import logging


def configure_logging():
    logging.basicConfig(level=logging.INFO)
configure_logging()
# Export the configured logger
logger = logging.getLogger(__name__)

class Config:
    BASE_URL = "https://www.google.com"
    SEARCH_TERM = "Cars in London"
    GUMTREE_DOMAIN = "gumtree.com"
    TIMEOUT = 20


