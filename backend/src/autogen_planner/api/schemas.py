"""
API schemas for the AutoGen Planner application.

This module defines the request and response schemas for the API endpoints.
"""

from pydantic import BaseModel, Field
from typing import List, Optional

class UserRequest(BaseModel):
    """
    User request schema.
    
    Attributes:
        query: The user query.
    """
    query: str = Field(..., description="The user query to generate a plan for")
    
class PlanResponse(BaseModel):
    """
    Plan response schema.
    
    Attributes:
        plan: The generated plan.
    """
    plan: str = Field(..., description="The generated execution plan") 