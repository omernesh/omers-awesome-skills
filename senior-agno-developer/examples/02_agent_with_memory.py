"""
Agent with Memory Example
=========================
Demonstrates creating an agent with persistent memory using PostgreSQL.
"""

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.postgres import PostgresDb
from agno.tools.duckduckgo import DuckDuckGoTools
import os

# Configure database
db = PostgresDb(
    db_url=os.getenv("DATABASE_URL", "postgresql://localhost:5432/agno_db"),
    table_name="agent_sessions",
)

# Create agent with memory
agent = Agent(
    name="Memory Assistant",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DuckDuckGoTools()],
    db=db,
    add_history_to_context=True,
    num_history_runs=10,
    add_datetime_to_context=True,
    instructions=[
        "Remember previous conversations",
        "Reference past interactions when relevant",
    ],
)

if __name__ == "__main__":
    session_id = "user-demo-session"
    
    # First interaction
    print("=== First Message ===")
    agent.print_response(
        "My name is Alice and I'm interested in quantum computing.",
        session_id=session_id,
        stream=True,
    )
    
    print("\n\n=== Second Message (with memory) ===")
    agent.print_response(
        "What did I say I was interested in?",
        session_id=session_id,
        stream=True,
    )
