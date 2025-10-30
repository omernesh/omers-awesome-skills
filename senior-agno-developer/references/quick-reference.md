# Agno Quick Reference

## Installation
```bash
pip install agno
```

## Basic Agent
```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat

agent = Agent(
    name="Assistant",
    model=OpenAIChat(id="gpt-4o"),
)
response = agent.run("Hello")
```

## Common Models
```python
# OpenAI
OpenAIChat(id="gpt-4o")
OpenAIChat(id="gpt-4o-mini")

# Anthropic
Claude(id="claude-sonnet-4-20250514")
Claude(id="claude-opus-4-20250514")

# Google
Gemini(id="gemini-2.0-flash-exp")
```

## Built-in Tools
```python
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from agno.tools.exa import ExaTools

tools = [
    DuckDuckGoTools(),
    YFinanceTools(stock_price=True),
    ExaTools(),
]
```

## Custom Tools
```python
from agno.tools import tool

@tool
def my_function(param: str) -> str:
    """Function description for LLM."""
    return f"Result: {param}"
```

## Memory (PostgreSQL)
```python
from agno.db.postgres import PostgresDb

db = PostgresDb(
    db_url="postgresql://localhost/db",
    table_name="sessions",
)

agent = Agent(
    db=db,
    add_history_to_context=True,
    num_history_runs=10,
)
```

## Knowledge Base (RAG)
```python
from agno.knowledge.pdf import PDFKnowledge
from agno.vectordb.pgvector import PgVector

knowledge = PDFKnowledge(
    path="docs/",
    vector_db=PgVector(
        table_name="embeddings",
        db_url="postgresql://localhost/vectors",
    ),
)

agent = Agent(
    knowledge=knowledge,
    search_knowledge=True,
)
```

## Multi-Agent Team
```python
from agno.team import Team

team = Team(
    agents=[agent1, agent2, agent3],
    instructions=["Team instructions"],
)
response = team.run("Task")
```

## AgentOS
```python
from agno.os import AgentOS

agent_os = AgentOS(
    agents=[agent1, agent2],
    security_key="secret-key",
)
app = agent_os.get_app()
```

## Run Agent
```python
# Direct run
response = agent.run("message")

# Streaming
agent.print_response("message", stream=True)

# With session
agent.run("message", session_id="session-123")
```

## Environment Variables
```bash
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
DATABASE_URL=postgresql://localhost/db
AGENTOS_SECURITY_KEY=secret
```

## CLI Commands
```bash
# Initialize project
ag init my-project

# Start infrastructure
ag infra up

# Check status
ag infra status

# Stop infrastructure
ag infra down
```
