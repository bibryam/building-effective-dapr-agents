# Augmented LLM Pattern

## Pattern Overview

The Augmented LLM pattern is a foundational building block for agentic systems. It enhances a language model with external capabilities such as memory, tools, and retrieval systems. This pattern enables LLMs to overcome their inherent limitations by connecting them to the outside world, allowing them to remember context across interactions and access external data or services.

![01_augmented_llm.webp](images/01_augmented_llm.webp)

## Use Cases

- **Personal Assistants**: Remembering user preferences and accessing calendars, emails, or other personal data
- **Customer Support**: Retrieving product information or account details to provide accurate assistance
- **Research Tools**: Searching and retrieving information from databases or knowledge bases
- **Domain-Specific Applications**: Connecting to specialized tools like calculators, data analyzers, or external APIs

## Dapr Agent Implementation

This example demonstrates a simple travel planning assistant that:
1. Remembers user context (desired travel destination)
2. Uses a tool to search for flight options to that destination

The implementation uses the Dapr Agents framework, which provides a clean way to enhance LLMs with memory and tool-using capabilities.

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
python 01_augmented_llm.py
```

## How It Works

The key components of this Augmented LLM pattern implementation are:

1. **Memory**: The agent automatically maintains conversation history, allowing it to remember that the user wants to visit Paris.

2. **Tool Integration**: A flight search tool is defined using the `@tool` decorator, which automatically handles:
    - Input validation with Pydantic models
    - Type conversion
    - Structured output formatting

3. **Agent Configuration**: The agent is configured with:
    - A specific role ("Travel Planner Assistant")
    - Instructions that guide its behavior
    - Access to the defined tools

When the user asks for flights without specifying a destination in the second interaction, the agent:
- Recalls the previously mentioned destination (Paris) from memory
- Invokes the flight search tool with "Paris" as the parameter
- Presents the flight options in a natural, conversational format

This demonstrates the core value of the Augmented LLM pattern: enhancing an LLM with memory and external capabilities to provide more useful and contextually aware responses.

## References

- [Anthropic: Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [Dapr Agents Documentation](https://dapr.github.io/dapr-agents/)