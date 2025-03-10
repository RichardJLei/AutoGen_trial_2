"""
Tests for the plan agent.
"""

import pytest
from unittest.mock import patch, MagicMock
from src.autogen_planner.agents.plan_agent import PlanAgent

def test_plan_agent_initialization():
    """
    Test that the plan agent can be initialized.
    """
    with patch('src.autogen_planner.services.ai.gemini.GeminiClient'):
        agent = PlanAgent()
        assert agent is not None
        assert agent.agent is not None
        assert agent.gemini_client is not None

def test_generate_plan():
    """
    Test that the plan agent can generate a plan.
    """
    # Mock the GeminiClient
    mock_gemini_client = MagicMock()
    mock_gemini_client.generate_text.return_value = "Test plan"
    
    with patch('src.autogen_planner.agents.plan_agent.GeminiClient', return_value=mock_gemini_client):
        agent = PlanAgent()
        user_message = "Test message"
        result = agent.generate_plan(user_message)
        
        # Check that the result is correct
        assert result == "Test plan"
        
        # Check that the GeminiClient was called with the correct prompt
        mock_gemini_client.generate_text.assert_called_once()
        prompt = mock_gemini_client.generate_text.call_args[0][0]
        assert "Test message" in prompt 