#!/usr/bin/env python3
"""
Augmented LLM Pattern

This example demonstrates the Augmented LLM pattern from Anthropic's "Building Effective Agents"
using Dapr Agents framework. The pattern showcases:
1. Memory - remembering user preferences
2. Tool use - accessing external data

"""

from typing import List
from pydantic import BaseModel, Field
from dapr_agents import tool, Agent
from dotenv import load_dotenv

# Define tool output model
class FlightOption(BaseModel):
    airline: str = Field(description="Airline name")
    price: float = Field(description="Price in USD")

# Define tool input model
class DestinationSchema(BaseModel):
    destination: str = Field(description="Destination city name")

# Define flight search tool
@tool(args_model=DestinationSchema)
def search_flights(destination: str) -> List[FlightOption]:
    """Search for flights to the specified destination."""
    # Mock flight data (would be an external API call in a real app)
    return [
        FlightOption(airline="SkyHighAir", price=450.00),
        FlightOption(airline="GlobalWings", price=375.50)
    ]

def main():
    load_dotenv()

    # Create agent with memory and tools
    travel_planner = Agent(
        name="TravelBuddy",
        role="Travel Planner Assistant",
        instructions=["Remember destinations and help find flights"],
        tools=[search_flights]
    )

    # First interaction
    print("\n--- First interaction ---")
    response = travel_planner.run("I want to visit Paris")
    print(response)

    # Second interaction (uses memory and tool)
    print("\n--- Second interaction (uses memory and tool) ---")
    response = travel_planner.run("Show me flights")
    print(response)

if __name__ == "__main__":
    main()