"""
Text formatting utilities for the Gradio application.

This module defines text formatting utilities for the Gradio application.
"""

def format_plan(plan: str) -> str:
    """
    Format a plan for display.
    
    Args:
        plan: The plan to format.
        
    Returns:
        The formatted plan.
    """
    if not plan:
        return "*No plan generated yet.*"
    
    # Add markdown formatting to the plan
    formatted_plan = f"## Execution Plan\n\n{plan}"
    
    return formatted_plan 