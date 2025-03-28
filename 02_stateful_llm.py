#!/usr/bin/env python3
"""
Simple Augmented LLM Pattern with Agentic Workflow
Shows basic memory, tool use, and workflow execution
"""

import asyncio
from typing import List
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from dapr_agents import tool, AssistantAgent

# Define data models
class FlightOption(BaseModel):
    airline: str = Field(description="Airline name")
    price: float = Field(description="Price in USD")

class DestinationSchema(BaseModel):
    destination: str = Field(description="Destination city name")

@tool(args_model=DestinationSchema)
def search_flights(destination: str) -> List[FlightOption]:
    """Search for flights to the specified destination."""
    return [
        FlightOption(airline="SkyHighAir", price=450.00),
        FlightOption(airline="GlobalWings", price=375.50)
    ]

async def main():
    try:
        # Initialize TravelBuddy agent
        travel_planner = AssistantAgent(
            name="TravelBuddy",
            role="Travel Planner",
            goal="Help users find flights and remember preferences",
            instructions=[
                "Find flights to destinations",
                "Remember user preferences",
                "Provide clear flight info"
            ],
            tools=[search_flights],
            message_bus_name="messagepubsub",
            state_store_name="workflowstatestore",
            state_key="workflow_state",
            agents_registry_store_name="workflowstatestore",
            agents_registry_key="agents_registry",
            service_port=8001,
            daprGrpcPort=50001
        )

        travel_planner.as_service(port=8001)
        await travel_planner.start()
        print("Travel Planner Agent is running")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())