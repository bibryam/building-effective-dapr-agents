#!/usr/bin/env python3
"""
Autonomous Agent Pattern - Simple Travel Assistant

This example demonstrates the Autonomous Agent pattern from Anthropic's "Building Effective Agents"
using Dapr Agents framework with a simplified ReActAgent implementation.
"""

import asyncio
from dapr_agents import tool, ReActAgent
from dotenv import load_dotenv

load_dotenv()

@tool
def search_weather(city: str) -> str:
    """Get weather information for a city."""
    weather_data = {
        "london": "rainy, 12°C",
        "paris": "sunny, 18°C",
        "tokyo": "cloudy, 16°C"
    }
    return weather_data.get(city.lower(), "Weather data not available")

@tool
def find_activities(city: str) -> str:
    """Find popular activities for a city."""
    activities = {
        "london": "Visit British Museum, See Big Ben, Ride the London Eye",
        "paris": "Visit Eiffel Tower, Explore Louvre Museum, Walk along Seine River",
        "tokyo": "Visit Tokyo Skytree, Explore Senso-ji Temple, Shop in Shibuya"
    }
    return activities.get(city.lower(), "Activity data not available")

async def run_agent():
    # Create the ReAct agent with both tools
    travel_agent = ReActAgent(
        name="TravelHelper",
        role="Travel Assistant",
        instructions=["Help users plan trips by providing weather and activities"],
        tools=[search_weather, find_activities]
    )

    print("=== AUTONOMOUS AGENT EXAMPLE ===")
    print("Ask about travel information for cities like London, Paris, or Tokyo.")
    print("The agent will decide which information to get first.\n")

    # Example query that requires both tools
    result = await travel_agent.run("I'm planning a trip to Paris. What should I know?")
    print(f"Result: {result}")

def main():
    asyncio.run(run_agent())

if __name__ == "__main__":
    main()