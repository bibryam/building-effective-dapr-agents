# Evaluator-Optimizer Pattern

## Pattern Overview

The Evaluator-Optimizer pattern features two complementary LLM roles in a feedback loop: one generates content while another evaluates it, leading to iterative improvements until quality criteria are met.

![Evaluator-Optimizer Pattern](images/07_evaluator.webp)

## Use Cases

- **Content Creation**: Refining written content to match specific style guidelines or quality standards
- **Translation**: Improving literary translations that require nuanced understanding and expression
- **Code Generation**: Creating code that meets specific requirements and handles edge cases
- **Complex Search**: Multi-round information gathering and refinement
- **Travel Planning**: Creating detailed itineraries that meet traveler preferences

## Dapr Agent Implementation

This example demonstrates an iterative travel planning workflow that:
1. Takes a travel request as input
2. Uses a generator LLM to create an initial travel plan
3. Uses an evaluator LLM to assess the plan and provide specific feedback
4. Iteratively improves the plan based on evaluation feedback
5. Terminates when the plan meets quality criteria or reaches maximum iterations

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
dapr run --app-id evaluator-optimizer --resources-path components/ -- python 07_evaluator.py
```

## How It Works

The key components of this Evaluator-Optimizer pattern implementation are:

1. **Generator LLM**: Creates or refines content based on input requirements and feedback
2. **Evaluator LLM**: Analyzes content against specific criteria and provides structured feedback
3. **Feedback Loop**: Enables multiple rounds of generation and evaluation
4. **Quality Criteria**: Defines when the process should terminate with measurable metrics

This implementation demonstrates the core value of the Evaluator-Optimizer pattern: achieving higher quality outputs through structured feedback and refinement, similar to human revision processes.

## When to Use This Pattern

This pattern is ideal when:
- There are clear evaluation criteria for the generated content
- Iterative refinement provides measurable value improvement
- LLM responses can be improved through explicit feedback
- Quality is more important than latency or cost

## Key Benefits

- Produces higher quality outputs through iterative refinement
- Allows for clear articulation of quality standards
- Enables continuous improvement of generated content
- Mimics the human editing and revision process

## References

- [Anthropic: Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [Dapr Agents Documentation](https://dapr.github.io/dapr-agents/)