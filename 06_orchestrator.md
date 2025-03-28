# Orchestrator-Workers Pattern

## Pattern Overview

The Orchestrator-Workers pattern features a central orchestrator LLM that dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results.

![Orchestrator-Workers Pattern](images/06_orchestrator.webp)

## Use Cases

- **Complex Travel Planning**: Creating comprehensive travel itineraries with multiple components
- **Software Development**: Making changes across multiple files based on requirements
- **Research Tasks**: Gathering and analyzing information from multiple sources
- **Business Analysis**: Evaluating different facets of a complex problem
- **Content Creation**: Combining specialized content from various domains

## Dapr Agent Implementation

This example demonstrates a travel planning workflow that:
1. Takes a complex travel request as input
2. Uses an orchestrator LLM to analyze the request and determine required subtasks
3. Dispatches each subtask to worker LLMs that handle specific aspects of the travel plan
4. Uses a synthesizer LLM to combine all worker outputs into a comprehensive travel plan

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
dapr run --app-id orchestrator --resources-path components/ -- python 06_orchestrator.py
```

## How It Works

The key components of this Orchestrator-Workers pattern implementation are:

1. **Dynamic Task Planning**: An orchestrator LLM analyzes the input and dynamically creates a plan of subtasks, each defined with a clear objective.

2. **Specialized Workers**: Each subtask is assigned to a worker LLM that focuses on solving just that specific aspect of the problem.

3. **Result Synthesis**: Once all workers complete their tasks, their outputs are combined by a synthesizer LLM into a cohesive final result.

4. **Flexible Architecture**: Unlike patterns with fixed workflows, this pattern adapts to each input by creating custom task plans.

This implementation demonstrates the core value of the Orchestrator-Workers pattern: handling complex, open-ended problems by dynamically creating and executing subtask plans.

## When to Use This Pattern

This pattern is ideal when:
- Tasks are complex and can't be broken into predefined subtasks
- The number and nature of subtasks depend on the specific input
- Specialized handling is needed for different aspects of a problem
- Results need to be synthesized into a cohesive output

## Key Differences from Parallelization

Unlike the parallelization pattern where subtasks are predefined, the orchestrator-workers pattern:
- Dynamically determines what subtasks are needed
- Provides flexibility to handle a wide range of inputs
- Can create varying numbers and types of subtasks based on the specific request

## References

- [Anthropic: Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [Dapr Agents Documentation](https://dapr.github.io/dapr-agents/)