"""
Logging utilities for the AutoGen Planner application.

This module defines logging utilities for the application.
"""

import logging
import sys
from ..config.settings import settings

def setup_logging():
    """
    Set up logging for the application.
    
    Returns:
        The configured logger.
    """
    # Create a logger
    logger = logging.getLogger("autogen_planner")
    logger.setLevel(logging.DEBUG if settings.debug else logging.INFO)
    
    # Create a console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG if settings.debug else logging.INFO)
    
    # Create a formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)
    
    # Add the handler to the logger
    logger.addHandler(console_handler)
    
    return logger

# Create a global logger instance
logger = setup_logging() 