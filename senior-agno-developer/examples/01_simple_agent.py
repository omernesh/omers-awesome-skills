"""
Simple Agent Example
====================
Demonstrates creating a basic agent with web search capabilities.
"""

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

# Create a simple web research agent
agent = Agent(
    name="Web Researcher",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions=[
        "Always cite your sources",
        "Be concise and accurate",
        "Use markdown formatting",
    ],
    markdown=True,
    show_tool_calls=True,
)

if __name__ == "__main__":
    # Run the agent
    response = agent.print_response(
        "What are the latest developments in quantum computing?",
        stream=True,
    )
    
    print("\n✅ Agent completed successfully!")
