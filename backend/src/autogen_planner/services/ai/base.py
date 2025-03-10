"""
Base AI client class for the AutoGen Planner application.

This module defines the base AI client class that all AI clients should inherit from.
"""

from abc import ABC, abstractmethod

class BaseAIClient(ABC):
    """
    Base AI client class.
    
    All AI clients should inherit from this class and implement the required methods.
    """
    
    def __init__(self):
        """
        Initialize the AI client.
        """
        pass
    
    @abstractmethod
    def generate_text(self, prompt: str) -> str:
        """
        Generate text based on a prompt.
        
        Args:
            prompt: The prompt to generate text from.
            
        Returns:
            The generated text.
        """
        pass 