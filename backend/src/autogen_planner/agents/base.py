"""
Base agent class for the AutoGen Planner application.

This module defines the base agent class that all agents should inherit from.
"""

from abc import ABC, abstractmethod

class BaseAgent(ABC):
    """
    Base agent class.
    
    All agents should inherit from this class and implement the required methods.
    """
    
    def __init__(self):
        """
        Initialize the agent.
        """
        pass
    
    @abstractmethod
    def process_message(self, message: str) -> str:
        """
        Process a message.
        
        Args:
            message: The message to process.
            
        Returns:
            The processed message.
        """
        pass 