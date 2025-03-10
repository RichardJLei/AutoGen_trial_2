"""
Gemini API client for the AutoGen Planner application.

This module defines the Gemini API client that interacts with the Gemini API.
"""

import google.generativeai as genai
from .base import BaseAIClient
from ...config.settings import settings

class GeminiClient(BaseAIClient):
    """
    Gemini API client.
    
    This client interacts with the Gemini API to generate text.
    """
    
    def __init__(self):
        """
        Initialize the Gemini client.
        """
        super().__init__()
        # Configure the Gemini API
        genai.configure(api_key=settings.gemini_api_key)
        # Initialize the model
        self.model = genai.GenerativeModel('gemini-2.0-flash')
    
    def generate_text(self, prompt: str) -> str:
        """
        Generate text based on a prompt using the Gemini API.
        
        Args:
            prompt: The prompt to generate text from.
            
        Returns:
            The generated text.
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            # In a real application, we would log this error
            print(f"Error generating text: {e}")
            return "I'm sorry, I couldn't generate a plan at this time. Please try again later." 