# Prompt Chaining Pattern

## Pattern Overview

The Prompt Chaining pattern decomposes a complex task into a sequence of steps, where each LLM call processes the output of the previous one. This pattern allows for breaking down complex tasks into simpler, more manageable steps with validation gates between them.

![Prompt Chaining Pattern](images/03_chaining.webp)

## Use Cases

- **Content Generation**: Creating outlines first, then expanding to full documents
- **Multi-stage Analysis**: Breaking complex analysis into sequential steps
- **Quality Assurance Workflows**: Adding validation between processing steps
- **Translation Services**: First understanding content, then translating with context
- **Planning Systems**: Creating high-level plans before detailed implementation

## Dapr Agent Implementation

This example demonstrates a travel planning workflow that:
1. Extracts the destination from user input (using simple prompt)
2. Validates the destination with a gate function
3. Generates a travel outline (using agent with tools)
4. Expands the outline into a detailed itinerary (using agent without tools)

The implementation showcases three different approaches to task execution:
- Basic prompt-based task (no agent)
- Agent-based task with tools
- Agent-based task without tools

## Setup

```bash
# Create a virtual environment
python3.10 -m venv .venv

# Activate the virtual environment 
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

Set up your environment variables:

```bash
# Create .env file with your API key
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

Run the example:

```bash
# Run with Dapr
dapr run --app-id prompt-chaining --resources-path components/ -- python 03_chaining.py
```

## How It Works

The key components of this Prompt Chaining pattern implementation are:

1. **Sequential Tasks**: The workflow chains multiple LLM operations together, with each building on the previous step's output.

2. **Validation Gate**: A simple check ensures the extracted destination is valid before proceeding to more complex (and costly) operations.

3. **Multiple Execution Types**:
    - Simple prompt (destination extraction): Uses a basic prompt without an agent
    - Planning agent (outline creation): Uses an agent with tools for attraction search
    - Itinerary agent (detail expansion): Uses an agent without tools for creative content generation

4. **Tool Integration**: The planning agent uses a tool to search for attractions based on type.

This implementation demonstrates how to combine different task types in a single workflow while maintaining a clear sequential flow with validation gates.

## When to Use This Pattern

This pattern is ideal when:
- Tasks can be naturally decomposed into sequential steps
- Each step builds on the output of the previous step
- You need validation between processing steps
- You're willing to trade some latency for higher quality results

## References

- [Anthropic: Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [Dapr Agents Documentation](https://dapr.github.io/dapr-agents/)