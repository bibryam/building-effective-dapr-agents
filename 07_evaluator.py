#!/usr/bin/env python3
"""
Evaluator-Optimizer Pattern - Travel Planner

This example demonstrates the Evaluator-Optimizer pattern from Anthropic's "Building Effective Agents"
using Dapr Agents framework. It shows how one LLM generates a travel plan while another evaluates
and provides feedback in a loop until the plan meets quality criteria.
"""

import logging
from typing import Dict, Any, List

from dapr_agents.workflow import WorkflowApp, workflow, task
from dapr_agents.types import DaprWorkflowContext
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define models for the evaluation process
class Evaluation(BaseModel):
    """Evaluation of a travel plan with feedback for improvement."""
    score: int = Field(..., description="Quality score from 1-10", ge=1, le=10)
    feedback: List[str] = Field(..., description="Specific feedback points for improvement")
    meets_criteria: bool = Field(..., description="Whether the plan meets all required criteria")

# Define Workflow logic
@workflow(name="evaluator_optimizer_travel_planner")
def evaluator_optimizer_travel_planner(ctx: DaprWorkflowContext, input_params: dict):
    """Defines a Dapr workflow that iteratively improves a travel plan through evaluation and feedback."""

    # Extract parameters
    travel_request = input_params.get("request")
    max_iterations = input_params.get("max_iterations", 3)
    score_threshold = input_params.get("score_threshold", 8)

    print(f"Starting Evaluator-Optimizer workflow for travel request")

    # Generate initial travel plan
    print("Generating initial travel plan...")
    current_plan = yield ctx.call_activity(
        generate_travel_plan,
        input={"request": travel_request, "feedback": None}
    )

    # Evaluation loop
    iteration = 1
    meets_criteria = False
    evaluation_results = None

    while iteration <= max_iterations and not meets_criteria:
        print(f"Iteration {iteration}: Evaluating travel plan...")

        # Evaluate the current plan
        evaluation = yield ctx.call_activity(
            evaluate_travel_plan,
            input={"request": travel_request, "plan": current_plan}
        )

        score = evaluation.get("score", 0)
        feedback = evaluation.get("feedback", [])
        meets_criteria = evaluation.get("meets_criteria", False)

        print(f"Evaluation score: {score}/10")
        print(f"Meets criteria: {meets_criteria}")

        if feedback:
            feedback_str = "\n- ".join([""] + feedback)
            print(f"Feedback:{feedback_str}")

        evaluation_results = evaluation

        # Check if we should continue optimizing
        if meets_criteria or score >= score_threshold or iteration >= max_iterations:
            break

        # Optimize the plan based on feedback
        print(f"Iteration {iteration}: Optimizing travel plan based on feedback...")
        current_plan = yield ctx.call_activity(
            generate_travel_plan,
            input={"request": travel_request, "feedback": feedback}
        )

        iteration += 1

    # Final assessment
    if meets_criteria:
        print("Travel plan meets all criteria!")
    elif evaluation_results and evaluation_results.get("score", 0) >= score_threshold:
        print(f"Travel plan reached acceptable quality score: {evaluation_results.get('score')}/10")
    else:
        print(f"Reached maximum iterations ({max_iterations}). Using best plan so far.")

    return {
        "final_plan": current_plan,
        "iterations": iteration,
        "final_evaluation": evaluation_results
    }

@task(description="Create a comprehensive travel plan for this request: {request}. If feedback is provided, incorporate these improvements: {feedback}")
def generate_travel_plan(request: str, feedback: List[str] = None) -> str:
    """Generates or optimizes a travel plan based on the request and any feedback."""
    # This will be implemented as an LLM call by the framework
    pass

@task(description="Evaluate this travel plan for the given request. Provide a score (1-10), specific feedback for improvement, and whether it meets all criteria. Request: {request} | Plan: {plan}")
def evaluate_travel_plan(request: str, plan: str) -> Evaluation:
    """Evaluates a travel plan and provides feedback for improvement."""
    # This will be implemented as an LLM call by the framework
    pass

if __name__ == "__main__":
    wfapp = WorkflowApp()

    # Example travel request
    travel_request = """
    I'm planning a 4-day cultural trip to Kyoto, Japan next spring during cherry blossom season. 
    I'm interested in traditional temples, Japanese gardens, authentic cuisine, and cultural experiences 
    like tea ceremonies. I prefer a mix of famous sites and off-the-beaten-path locations. 
    I'd like to stay at a traditional ryokan for at least part of my stay, and I'm looking for 
    a balance of scheduled activities and time to wander. My budget is mid-range.
    """

    print("=== EVALUATOR-OPTIMIZER PATTERN DEMONSTRATION ===")
    print("This example shows how a travel plan is iteratively improved through evaluation and feedback")

    print("\nTravel request:")
    print(travel_request)

    print("\nStarting evaluator-optimizer workflow...")
    workflow_params = {
        "request": travel_request,
        "max_iterations": 3,
        "score_threshold": 8
    }

    result = wfapp.run_and_monitor_workflow(
        evaluator_optimizer_travel_planner,
        input=workflow_params
    )

    if result:
        final_plan = result.get("final_plan", "")
        iterations = result.get("iterations", 0)
        final_score = result.get("final_evaluation", {}).get("score", 0)

        print(f"\nFinal travel plan after {iterations} iterations (final score: {final_score}/10):")

        # Display a preview of the result
        preview_length = min(500, len(final_plan))
        print(f"\n{final_plan[:preview_length]}...")
        if len(final_plan) > preview_length:
            print("...(truncated)")

    print("\nEvaluator-Optimizer Pattern completed successfully!")