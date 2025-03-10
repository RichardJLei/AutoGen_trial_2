"""
Plan agent for the AutoGen Planner application.

This module defines the plan agent that generates execution plans.
"""

import autogen
from .base import BaseAgent
from ..services.ai.gemini import GeminiClient

class PlanAgent(BaseAgent):
    """
    Plan agent that generates execution plans.
    """
    
    def __init__(self):
        """
        Initialize the plan agent.
        """
        super().__init__()
        # Initialize the AutoGen agent
        self.agent = autogen.ConversableAgent(
            name="Plan_Agent",
            system_message="You are a helpful assistant that generates execution plans.",
            human_input_mode="NEVER"
        )
        # Initialize the Gemini client
        self.gemini_client = GeminiClient()
    
    def generate_plan(self, user_message: str) -> str:
        """
        Generate an execution plan based on the user message.
        
        Args:
            user_message: The user message.
            
        Returns:
            The generated execution plan.
        """
        # Compose a prompt for the AI model
        prompt = f"""
        Based on the following user request, generate a detailed execution plan:
        
        {user_message}
        
        The plan should include:
        1. Clear steps to accomplish the task
        2. Any necessary resources or tools
        3. Potential challenges and how to address them
        
        Please format the plan in a structured way.
        """
        
        # Get the response from the Gemini model
        response = self.gemini_client.generate_text(prompt)
        
        return response
    
    def process_message(self, message: str) -> str:
        """
        Process a message.
        
        Args:
            message: The message to process.
            
        Returns:
            The processed message.
        """
        return self.agent.generate_reply(message) 