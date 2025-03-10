"""
Application settings for the AutoGen Planner application.

This module defines the application settings using Pydantic's BaseSettings.
"""

import os
from pydantic import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """
    Application settings.
    
    Attributes:
        app_name: The name of the application.
        api_prefix: The prefix for the API endpoints.
        debug: Whether to run in debug mode.
        gemini_api_key: The API key for the Gemini API.
    """
    app_name: str = "AutoGen Planner"
    api_prefix: str = "/api/v1"
    debug: bool = False
    gemini_api_key: Optional[str] = None
    
    class Config:
        """
        Configuration for the settings.
        """
        env_file = ".env"
        env_prefix = "AUTOGEN_"

# Create a global settings instance
settings = Settings()

# Override settings from environment variables
for key, value in os.environ.items():
    if key.startswith("AUTOGEN_"):
        setting_key = key[len("AUTOGEN_"):].lower()
        if hasattr(settings, setting_key):
            setattr(settings, setting_key, value) 