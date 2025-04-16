# Routing Pattern

## Pattern Overview

The Routing pattern classifies an input and directs it to a specialized followup task. This pattern enables separation of concerns, allowing each specialized handler to focus on a specific type of input without the complexity of handling all possible cases.

![Routing Pattern](images/05_routing.webp)

## Use Cases

- **Customer Support**: Directing different types of queries (refunds, technical help, general questions) to specialized agents
- **Content Creation**: Routing writing tasks to topic specialists (finance, tech, healthcare)
- **Resource Optimization**: Sending simple queries to smaller, faster models and complex ones to more capable models
- **Multi-lingual Support**: Routing queries to language-specific handlers
- **Hybrid LLM Systems**: Using different models for different tasks based on their strengths

## Dapr Agent Implementation

This example demonstrates a travel assistant that:
1. Takes a user's travel query as input
2. Classifies the query into one of three categories:
    - Attractions (sightseeing, activities)
    - Accommodations (hotels, rentals)
    - Transportation (getting around, travel logistics)
3. Routes the query to a specialized handler optimized for that category
4. Returns a detailed response from the appropriate specialist

The implementation uses the Dapr Agents framework to handle query classification and routing to specialized handlers.

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
dapr run --app-id routing --resources-path components/ -- python 04_routing.py
```

## How It Works

The key components of this Routing pattern implementation are:

1. **Query Classification**: An LLM-based router analyzes the input query and determines its category using a structured output format (RoutingDecision).

2. **Specialized Handlers**: Three task handlers with optimized prompts focus on different travel domains:
    - Attractions handler: Optimized for questions about sights and activities
    - Accommodations handler: Specialized for hotel and lodging inquiries
    - Transportation handler: Focused on travel logistics questions

3. **Workflow Orchestration**: The Dapr workflow engine manages the process flow:
    - First sending the query to the classifier
    - Then routing to the appropriate specialized handler
    - Finally returning the response to the user

This implementation demonstrates the core value of the Routing pattern: improved response quality through specialization while maintaining a simple interface for users.

## When to Use This Pattern

This pattern is ideal when:
- Tasks involve distinct categories that are better handled separately
- Classification can be done accurately by an LLM
- Different types of inputs benefit from specialized prompts
- You want to optimize cost/performance by routing simpler queries to smaller models

## References

- [Anthropic: Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [Dapr Agents Documentation](https://dapr.github.io/dapr-agents/)