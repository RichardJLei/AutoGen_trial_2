"""
Tests for the Gemini client.
"""

import pytest
from unittest.mock import patch, MagicMock
from src.autogen_planner.services.ai.gemini import GeminiClient

def test_gemini_client_initialization():
    """
    Test that the Gemini client can be initialized.
    """
    with patch('google.generativeai.configure'), \
         patch('google.generativeai.GenerativeModel'):
        client = GeminiClient()
        assert client is not None
        assert client.model is not None

def test_generate_text_success():
    """
    Test that the Gemini client can generate text successfully.
    """
    # Mock the GenerativeModel
    mock_model = MagicMock()
    mock_response = MagicMock()
    mock_response.text = "Generated text"
    mock_model.generate_content.return_value = mock_response
    
    with patch('google.generativeai.configure'), \
         patch('google.generativeai.GenerativeModel', return_value=mock_model):
        client = GeminiClient()
        result = client.generate_text("Test prompt")
        
        # Check that the result is correct
        assert result == "Generated text"
        
        # Check that the model was called with the correct prompt
        mock_model.generate_content.assert_called_once_with("Test prompt")

def test_generate_text_error():
    """
    Test that the Gemini client handles errors gracefully.
    """
    # Mock the GenerativeModel to raise an exception
    mock_model = MagicMock()
    mock_model.generate_content.side_effect = Exception("Test error")
    
    with patch('google.generativeai.configure'), \
         patch('google.generativeai.GenerativeModel', return_value=mock_model):
        client = GeminiClient()
        result = client.generate_text("Test prompt")
        
        # Check that the result is the error message
        assert "I'm sorry" in result
        assert "try again later" in result 