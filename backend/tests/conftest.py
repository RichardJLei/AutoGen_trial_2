"""
Pytest fixtures for the AutoGen Planner backend tests.
"""

import pytest
from fastapi.testclient import TestClient
from src.autogen_planner.main import app

@pytest.fixture
def client():
    """
    Create a test client for the FastAPI application.
    
    Returns:
        TestClient: The test client.
    """
    return TestClient(app) 