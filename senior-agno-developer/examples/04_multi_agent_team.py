"""
Multi-Agent Team Example
========================
Demonstrates creating a team of specialized agents.
"""

from agno.agent import Agent
from agno.team import Team
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

# Create specialized agents
researcher = Agent(
    name="Research Specialist",
    role="Research and gather information from the web",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools(search=True, news=True)],
    instructions=[
        "Conduct thorough research",
        "Verify information from multiple sources",
        "Provide comprehensive summaries",
    ],
)

analyst = Agent(
    name="Data Analyst",
    role="Analyze data and provide insights",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        company_info=True,
    )],
    instructions=[
        "Analyze data thoroughly",
        "Use tables for structured data",
        "Provide clear insights and trends",
    ],
)

writer = Agent(
    name="Report Writer",
    role="Create comprehensive written reports",
    model=OpenAIChat(id="gpt-4o"),
    instructions=[
        "Write clear, professional reports",
        "Include executive summary",
        "Use proper formatting and structure",
    ],
)

# Create team
team = Team(
    agents=[researcher, analyst, writer],
    instructions=[
        "Collaborate to produce high-quality reports",
        "Researcher gathers information first",
        "Analyst processes and analyzes data",
        "Writer creates final formatted report",
    ],
)

if __name__ == "__main__":
    # Team works together
    response = team.print_response(
        "Research Tesla's recent performance and create a comprehensive report",
        stream=True,
    )
