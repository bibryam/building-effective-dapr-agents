"""
Workflow utilities for the building-effective-agents examples.
"""

from dapr_agents.agent.patterns.toolcall.base import ToolCallAgent
from typing import Union, Dict, Any, Optional

class WorkflowToolCallAgent(ToolCallAgent):
    """
    Extension of ToolCallAgent that handles the 'task' parameter expected by workflow tasks.
    This adapter makes ToolCallAgent compatible with the workflow task interface.
    
    Use this class whenever you need to use ToolCallAgent in a workflow task context.
    """
    
    def run(self, task: Optional[Union[str, Dict[str, Any]]] = None, **kwargs) -> Any:
        """
        Adapter method that maps the 'task' parameter to the 'input_data' parameter expected by ToolCallAgent.
        
        Args:
            task (Optional[Union[str, Dict[str, Any]]]): The task input for the agent.
            **kwargs: Additional keyword arguments.
            
        Returns:
            Any: The result from the agent's processing.
        """
        # Forward the task input as input_data to the parent ToolCallAgent.run method
        return super().run(input_data=task) 