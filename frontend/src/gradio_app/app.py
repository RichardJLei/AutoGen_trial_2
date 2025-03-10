"""
Main Gradio application for the AutoGen Planner.

This module defines the main Gradio application for the frontend.
"""

import gradio as gr
import os
from dotenv import load_dotenv
from .components.chat import ChatInterface
from .api_client import APIClient

# Load environment variables from .env file
load_dotenv()

def create_app(api_url: str = None) -> gr.Blocks:
    """
    Create the Gradio application.
    
    Args:
        api_url: The URL for the backend API.
        
    Returns:
        The Gradio Blocks application.
    """
    # Use environment variable if api_url is not provided
    if api_url is None:
        api_url = os.environ.get("AUTOGEN_API_URL", "http://localhost:8000/api/v1")
    
    # Initialize the API client
    api_client = APIClient(base_url=api_url)
    
    # Initialize the chat interface
    chat_interface = ChatInterface(api_client=api_client)
    
    # Create the Gradio application
    with gr.Blocks(
        title="AutoGen Planner",
        theme=gr.themes.Soft(),
        css="""
        .gradio-container {
            max-width: 1200px;
            margin: auto;
        }
        """
    ) as app:
        # Create the chat interface
        chat_interface.create_interface()
    
    return app

def run_app(api_url: str = None, port: int = None, share: bool = None):
    """
    Run the Gradio application.
    
    Args:
        api_url: The URL for the backend API.
        port: The port to run the application on.
        share: Whether to create a public link.
    """
    # Use environment variables if parameters are not provided
    if api_url is None:
        api_url = os.environ.get("AUTOGEN_API_URL", "http://localhost:8000/api/v1")
    
    if port is None:
        port = int(os.environ.get("AUTOGEN_PORT", 7860))
    
    if share is None:
        share = os.environ.get("AUTOGEN_SHARE", "False").lower() == "true"
    
    app = create_app(api_url=api_url)
    app.launch(server_port=port, share=share)

if __name__ == "__main__":
    # Run the application with settings from environment variables
    run_app() 