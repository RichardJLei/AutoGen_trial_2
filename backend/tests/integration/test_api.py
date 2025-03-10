"""
Integration tests for the API.
"""

import pytest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from src.autogen_planner.main import app

client = TestClient(app)

def test_create_plan_endpoint():
    """
    Test the create plan endpoint.
    """
    # Mock the PlanAgent to return a fixed plan
    mock_plan_agent = MagicMock()
    mock_plan_agent.generate_plan.return_value = "Test plan"
    
    # Mock the UserAgent to return a fixed message
    mock_user_agent = MagicMock()
    mock_user_agent.process_request.return_value = "Test message"
    
    with patch('src.autogen_planner.api.routes.UserAgent', return_value=mock_user_agent), \
         patch('src.autogen_planner.api.routes.PlanAgent', return_value=mock_plan_agent):
        # Send a request to the endpoint
        response = client.post(
            "/api/v1/plan",
            json={"query": "Test query"}
        )
        
        # Check that the response is correct
        assert response.status_code == 200
        assert response.json() == {"plan": "Test plan"}
        
        # Check that the agents were called with the correct arguments
        mock_user_agent.process_request.assert_called_once_with("Test query")
        mock_plan_agent.generate_plan.assert_called_once_with("Test message")

def test_create_plan_endpoint_error():
    """
    Test that the create plan endpoint handles errors gracefully.
    """
    # Mock the UserAgent to raise an exception
    mock_user_agent = MagicMock()
    mock_user_agent.process_request.side_effect = Exception("Test error")
    
    with patch('src.autogen_planner.api.routes.UserAgent', return_value=mock_user_agent):
        # Send a request to the endpoint
        response = client.post(
            "/api/v1/plan",
            json={"query": "Test query"}
        )
        
        # Check that the response is an error
        assert response.status_code == 500
        assert "Test error" in response.json()["detail"] 