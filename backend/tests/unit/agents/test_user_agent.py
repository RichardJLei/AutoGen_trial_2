"""
Tests for the user agent.
"""

import pytest
from src.autogen_planner.agents.user_agent import UserAgent

def test_user_agent_initialization():
    """
    Test that the user agent can be initialized.
    """
    agent = UserAgent()
    assert agent is not None
    assert agent.agent is not None

def test_process_request():
    """
    Test that the user agent can process a request.
    """
    agent = UserAgent()
    query = "Test query"
    result = agent.process_request(query)
    assert result is not None
    assert isinstance(result, str)
    assert "Test query" in result 