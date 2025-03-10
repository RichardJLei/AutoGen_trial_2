"""
User agent for the AutoGen Planner application.

This module defines the user agent that handles user interactions.
"""

import autogen
from .base import BaseAgent

class UserAgent(BaseAgent):
    """
    User agent that handles user interactions.
    """
    
    def __init__(self):
        """
        Initialize the user agent.
        """
        super().__init__()
        # Initialize the AutoGen agent
        self.agent = autogen.ConversableAgent(
            name="User_Agent",
            system_message="You are a helpful assistant that processes user requests.",
            human_input_mode="NEVER"
        )
    
    def process_request(self, query: str) -> str:
        """
        Process a user request.
        
        Args:
            query: The user query.
            
        Returns:
            The processed request to be sent to the plan agent.
        """
        # In a real implementation, this would use AutoGen's capabilities
        # For now, we'll just format the query
        return f"User request: {query}"
    
    def process_message(self, message: str) -> str:
        """
        Process a message.
        
        Args:
            message: The message to process.
            
        Returns:
            The processed message.
        """
        return self.agent.generate_reply(message) 