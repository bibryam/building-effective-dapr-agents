#!/usr/bin/env python3
"""
Routing Pattern - Travel Assistant

This example demonstrates the Routing pattern from Anthropic's "Building Effective Agents"
using Dapr Agents framework. It shows how to classify a travel query and route it to
specialized handlers based on the query type.
"""

import logging
from enum import Enum
from typing import Optional

from dapr_agents.workflow import WorkflowApp, workflow, task
from dapr_agents.types import DaprWorkflowContext
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

# Define query types for the router
class QueryType(str, Enum):
    ATTRACTIONS = "attractions"
    ACCOMMODATIONS = "accommodations"
    TRANSPORTATION = "transportation"

# Define models for routing
class TravelQuery(BaseModel):
    """A travel-related query from a user."""
    query: str = Field(..., description="The user's travel query")
    destination: Optional[str] = Field(None, description="The travel destination if specified")

class RoutingDecision(BaseModel):
    """The routing decision for a travel query."""
    query_type: QueryType = Field(..., description="The type of travel query")
    explanation: str = Field(..., description="Explanation of why this routing was chosen")

# Define Workflow logic
@workflow(name="travel_assistant_workflow")
def travel_assistant_workflow(ctx: DaprWorkflowContext, input_params: dict):
    """Defines a Dapr workflow that routes a travel query to specialized handlers."""

    # Extract the user query
    user_query = input_params.get("query")
    logging.info(f"Received travel query: {user_query}")

    # Route the query to the appropriate handler using an LLM
    routing_result = yield ctx.call_activity(
        route_query,
        input={"query": user_query}
    )

    query_type = routing_result.get("query_type")
    logging.info(f"Query classified as: {query_type}")

    # Route to the appropriate specialized handler based on the classification
    if query_type == QueryType.ATTRACTIONS:
        response = yield ctx.call_activity(
            handle_attractions_query,
            input={"query": user_query}
        )
    elif query_type == QueryType.ACCOMMODATIONS:
        response = yield ctx.call_activity(
            handle_accommodations_query,
            input={"query": user_query}
        )
    elif query_type == QueryType.TRANSPORTATION:
        response = yield ctx.call_activity(
            handle_transportation_query,
            input={"query": user_query}
        )
    else:
        # Fallback if the query type is not recognized
        response = "I'm not sure how to help with that specific travel question."

    return response

@task(description="Classify this travel query into one of these categories: attractions (for questions about sights, activities, or things to do), accommodations (for questions about hotels, rentals, or places to stay), or transportation (for questions about getting around or travel logistics). Query: {query}")
def route_query(query: str) -> RoutingDecision:
    """Classifies a travel query and routes it to the appropriate handler."""
    # This will be implemented as an LLM call by the framework
    pass

@task(description="Answer this question about tourist attractions, sights, or activities: {query}")
def handle_attractions_query(query: str) -> str:
    """Specialized handler for queries about attractions and activities."""
    # This will be implemented as an LLM call by the framework
    pass

@task(description="Answer this question about accommodations, hotels, or places to stay: {query}")
def handle_accommodations_query(query: str) -> str:
    """Specialized handler for queries about accommodations."""
    # This will be implemented as an LLM call by the framework
    pass

@task(description="Answer this question about transportation, getting around, or travel logistics: {query}")
def handle_transportation_query(query: str) -> str:
    """Specialized handler for queries about transportation."""
    # This will be implemented as an LLM call by the framework
    pass

if __name__ == "__main__":
    wfapp = WorkflowApp()

    # Example travel queries for different types
    queries = [
        "What are the must-see attractions in Paris for a 3-day trip?",
        "Can you recommend budget-friendly hotels in central Paris?",
        "What's the best way to get around Paris using public transportation?"
    ]

    print("=== ROUTING PATTERN DEMONSTRATION ===")
    print("This example shows how to route different types of travel queries to specialized handlers\n")

    # Process each query to demonstrate routing
    for i, query in enumerate(queries, 1):
        print(f"Query {i}: {query}")
        result = wfapp.run_and_monitor_workflow(
            travel_assistant_workflow,
            input={"query": query}
        )

        if result:
            preview_length = min(200, len(result))
            print(f"Response: {result[:preview_length]}")
            if len(result) > preview_length:
                print("...")
            print("")

    print("Routing Pattern completed successfully!")