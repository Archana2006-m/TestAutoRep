import logging
from logging.config import fileConfig
import os

# Get the path to the logging configuration file
config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logging_config.ini')

# Load the logging configuration
fileConfig(config_path)

# Create a shared logger
shared_logger = logging.getLogger("shared_logger")