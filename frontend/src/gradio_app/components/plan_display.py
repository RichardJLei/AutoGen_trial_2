"""
Plan display component for the Gradio application.

This module defines the plan display component for the Gradio application.
"""

import gradio as gr
from ..utils.formatting import format_plan

class PlanDisplay:
    """
    Plan display component.
    
    This component displays the execution plan generated by the system.
    """
    
    def __init__(self):
        """
        Initialize the plan display.
        """
        pass
    
    def create_display(self) -> gr.Blocks:
        """
        Create the plan display.
        
        Returns:
            The Gradio Blocks component for the plan display.
        """
        with gr.Blocks() as plan_display:
            gr.Markdown("## Execution Plan")
            
            plan_markdown = gr.Markdown(
                value="*No plan generated yet.*",
                label="Plan",
            )
            
            copy_button = gr.Button("Copy Plan", variant="secondary")
            
            def copy_plan(plan):
                # In a real application, this would copy the plan to the clipboard
                # For now, we'll just return a message
                return "Plan copied to clipboard!"
            
            # Connect the components
            copy_button.click(
                copy_plan,
                inputs=[plan_markdown],
                outputs=[gr.Textbox(visible=False)],
            )
        
        return plan_display
    
    def update_plan(self, plan: str) -> str:
        """
        Update the plan display with a new plan.
        
        Args:
            plan: The new plan to display.
            
        Returns:
            The formatted plan.
        """
        return format_plan(plan) 