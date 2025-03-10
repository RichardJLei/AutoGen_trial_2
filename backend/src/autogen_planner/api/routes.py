"""
API routes for the AutoGen Planner application.

This module defines the API routes for the AutoGen Planner application.
"""

from fastapi import APIRouter, Depends, HTTPException
from ..agents.user_agent import UserAgent
from ..agents.plan_agent import PlanAgent
from .schemas import UserRequest, PlanResponse

router = APIRouter()

@router.post("/plan", response_model=PlanResponse)
async def create_plan(request: UserRequest):
    """
    Create a plan based on the user request.
    
    Args:
        request: The user request containing the query.
        
    Returns:
        A plan response containing the generated plan.
    """
    try:
        # Initialize agents
        user_agent = UserAgent()
        plan_agent = PlanAgent()
        
        # Process the request through the agents
        user_message = user_agent.process_request(request.query)
        plan = plan_agent.generate_plan(user_message)
        
        return PlanResponse(plan=plan)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 