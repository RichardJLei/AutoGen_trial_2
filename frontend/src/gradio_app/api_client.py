"""
API client for the Gradio application.

This module defines the API client that communicates with the backend API.
"""

import requests
import json
from typing import Dict, Any, Optional

class APIClient:
    """
    API client for the Gradio application.
    
    This client communicates with the backend API to create plans.
    """
    
    def __init__(self, base_url: str = "http://localhost:8000/api/v1"):
        """
        Initialize the API client.
        
        Args:
            base_url: The base URL for the API.
        """
        self.base_url = base_url
    
    def create_plan(self, query: str) -> str:
        """
        Create a plan based on the user query.
        
        Args:
            query: The user query.
            
        Returns:
            The generated plan.
        """
        # Prepare the request
        url = f"{self.base_url}/plan"
        headers = {"Content-Type": "application/json"}
        data = {"query": query}
        
        try:
            # Send the request
            response = requests.post(url, headers=headers, data=json.dumps(data))
            
            # Check for errors
            response.raise_for_status()
            
            # Parse the response
            result = response.json()
            
            return result.get("plan", "No plan was generated.")
        except requests.exceptions.RequestException as e:
            # In a real application, we would log this error
            print(f"Error creating plan: {e}")
            raise Exception(f"Failed to communicate with the backend API: {str(e)}")
        except json.JSONDecodeError as e:
            # In a real application, we would log this error
            print(f"Error parsing response: {e}")
            raise Exception("Failed to parse the response from the backend API.") 