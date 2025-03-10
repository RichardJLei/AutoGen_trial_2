"""
Tests for the chat component.
"""

import pytest
from unittest.mock import patch, MagicMock
import gradio as gr
from src.gradio_app.components.chat import ChatInterface
from src.gradio_app.api_client import APIClient

def test_chat_interface_initialization():
    """
    Test that the chat interface can be initialized.
    """
    api_client = MagicMock(spec=APIClient)
    chat_interface = ChatInterface(api_client=api_client)
    assert chat_interface is not None
    assert chat_interface.api_client is api_client
    assert chat_interface.chat_history == []

def test_create_interface():
    """
    Test that the chat interface can create a Gradio interface.
    """
    api_client = MagicMock(spec=APIClient)
    chat_interface = ChatInterface(api_client=api_client)
    
    with patch('gradio.Blocks') as mock_blocks, \
         patch('gradio.Markdown') as mock_markdown, \
         patch('gradio.Chatbot') as mock_chatbot, \
         patch('gradio.Textbox') as mock_textbox, \
         patch('gradio.Button') as mock_button, \
         patch('gradio.Row') as mock_row, \
         patch('gradio.Column') as mock_column:
        
        # Create the interface
        result = chat_interface.create_interface()
        
        # Check that the Gradio components were created
        mock_blocks.assert_called_once()
        assert mock_markdown.call_count >= 2
        mock_chatbot.assert_called_once()
        mock_textbox.assert_called_once()
        mock_button.assert_called_once()
        assert mock_row.call_count >= 1
        assert mock_column.call_count >= 2 