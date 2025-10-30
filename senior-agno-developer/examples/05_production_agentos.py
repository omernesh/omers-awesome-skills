"""
Production AgentOS Example
==========================
Demonstrates setting up AgentOS for production deployment.
"""

from agno.agent import Agent
from agno.os import AgentOS
from agno.models.openai import OpenAIChat
from agno.models.anthropic import Claude
from agno.db.postgres import PostgresDb
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
import os

# Configure shared database
db = PostgresDb(
    db_url=os.getenv("DATABASE_URL"),
    table_name="production_sessions",
)

# Create production agents
web_agent = Agent(
    name="web_agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    db=db,
    instructions=["Provide accurate web search results"],
    markdown=True,
)

finance_agent = Agent(
    name="finance_agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        company_info=True,
    )],
    db=db,
    instructions=["Provide financial data and analysis"],
    markdown=True,
)

assistant_agent = Agent(
    name="assistant_agent",
    model=Claude(id="claude-sonnet-4-20250514"),
    db=db,
    instructions=["Helpful general purpose assistant"],
    markdown=True,
)

# Create AgentOS
agent_os = AgentOS(
    agents=[web_agent, finance_agent, assistant_agent],
    security_key=os.getenv("AGENTOS_SECURITY_KEY"),
)

# Export FastAPI app
app = agent_os.get_app()

if __name__ == "__main__":
    # Serve with auto-reload for development
    agent_os.serve("agentos:app", reload=True, port=7777)
