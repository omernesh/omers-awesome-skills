---
name: senior-agno-developer
description: Expert-level skill for building production-ready AI agents and agentic systems using the Agno framework. Covers agent architecture, multi-agent teams, AgentOS deployment, tool integration, RAG patterns, and production best practices.
---

# Senior Agno Developer Skill

## Overview
Expert-level skill for building production-ready AI agents and agentic systems using the Agno framework. This skill enables you to architect, implement, and deploy sophisticated multi-agent systems with proper infrastructure, tooling, and best practices.

**Official Documentation**: https://docs.agno.com/  
**Documentation Reference**: https://docs.agno.com/llms-full.txt

## When to Use This Skill
Invoke this skill when:
- Building AI agents with LLM capabilities (OpenAI, Anthropic, Gemini, etc.)
- Creating multi-agent teams with specialized roles
- Implementing agentic workflows with tool integrations
- Setting up AgentOS for production deployments
- Integrating knowledge bases and memory systems
- Building agent UIs and APIs
- Configuring agent infrastructure and monitoring
- Implementing RAG (Retrieval Augmented Generation) patterns

## Core Concepts

### 1. Agent Architecture
**Agents** are the fundamental building blocks in Agno. Each agent has:
- **Model**: LLM backend (OpenAI, Anthropic, Gemini, etc.)
- **Tools**: Functions the agent can call
- **Instructions**: System prompts and behavior guidelines
- **Memory**: Session and conversation storage
- **Knowledge**: Vector database for RAG

**Basic Agent Structure:**
```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat

agent = Agent(
    name="Web Researcher",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions=["Always cite sources", "Be concise"],
    markdown=True,
    show_tool_calls=True,
)
```

### 2. Supported Models

**OpenAI Models:**
```python
from agno.models.openai import OpenAIChat

model = OpenAIChat(
    id="gpt-4o",              # gpt-4o, gpt-4o-mini, gpt-3.5-turbo
    temperature=0.7,
    max_tokens=2000,
)
```

**Anthropic Models:**
```python
from agno.models.anthropic import Claude

model = Claude(
    id="claude-sonnet-4-20250514",  # claude-opus-4, claude-sonnet-4
    temperature=0.7,
)
```

**Google Models:**
```python
from agno.models.google import Gemini

model = Gemini(
    id="gemini-2.0-flash-exp",      # gemini-2.0-flash, gemini-1.5-pro
    temperature=0.7,
)
```

**Other Supported Models:**
- Groq (groq-llama-3.1, groq-mixtral)
- Ollama (local models)
- xAI (grok-2)
- Together AI
- AWS Bedrock
- Azure OpenAI

### 3. Tool Integration

**Built-in Tools:**
- **DuckDuckGoTools**: Web search capabilities
- **YFinanceTools**: Financial data and stock information
- **XTools**: Twitter/X integration with metrics
- **ExaTools**: Advanced web search with domain filtering
- **ArxivTools**: Academic paper search
- **WebsiteTools**: Website content scraping
- **EmailTools**: Email operations
- **ShellTools**: Command execution
- **FileTools**: File operations
- **PythonTools**: Python code execution

**Tool Usage Pattern:**
```python
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

tools = [
    DuckDuckGoTools(search=True, news=True),
    YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        company_info=True,
    )
]

agent = Agent(
    model=model,
    tools=tools,
    instructions=["Use tables for financial data"],
)
```

**Custom Tool Creation:**
```python
from agno.tools import tool

@tool
def calculate_roi(investment: float, returns: float) -> float:
    """Calculate return on investment percentage.
    
    Args:
        investment: Initial investment amount
        returns: Total returns amount
    
    Returns:
        ROI percentage
    """
    return ((returns - investment) / investment) * 100

agent = Agent(tools=[calculate_roi])
```

### 4. Memory and Storage

**Database Options:**
- **PostgreSQL**: Production-grade storage (recommended)
- **SQLite**: Development and testing
- **DuckDB**: Analytics workloads

**PostgreSQL Configuration:**
```python
from agno.db.postgres import PostgresDb

db = PostgresDb(
    db_url="postgresql://user:pass@localhost:5432/agno_db",
    table_name="agent_sessions",
)

agent = Agent(
    db=db,
    add_history_to_context=True,
    num_history_runs=10,
)
```

**SQLite Configuration:**
```python
from agno.db.sqlite import SqliteDb

db = SqliteDb(
    db_file="tmp/agents.db",
    table_name="sessions",
)
```

### 5. Knowledge Base and RAG

**Vector Database Integration:**
```python
from agno.knowledge.pdf import PDFUrlKnowledge
from agno.vectordb.pgvector import PgVector

knowledge = PDFUrlKnowledge(
    urls=["https://example.com/doc.pdf"],
    vector_db=PgVector(
        table_name="documents",
        db_url="postgresql://localhost/vectors",
    ),
)

agent = Agent(
    knowledge=knowledge,
    search_knowledge=True,  # Enable RAG
    read_chat_history=True,
)
```

**Knowledge Sources:**
- PDF files (local/URL)
- Text files
- JSON documents
- CSV data
- Website content
- Custom sources

### 6. Teams and Multi-Agent Systems

**Team Structure:**
```python
from agno.team import Team

researcher = Agent(
    name="Researcher",
    role="Research and gather information",
    tools=[DuckDuckGoTools()],
)

writer = Agent(
    name="Writer",
    role="Write comprehensive reports",
)

team = Team(
    agents=[researcher, writer],
    instructions=["Collaborate to produce reports"],
)

response = team.print_response(
    "Research AI trends and write a report",
    stream=True,
)
```

### 7. Workflows

**Sequential Workflows:**
```python
from agno.workflow import Workflow, Task

workflow = Workflow(
    name="Research Pipeline",
    tasks=[
        Task(
            description="Research the topic",
            agent=researcher,
        ),
        Task(
            description="Summarize findings",
            agent=summarizer,
        ),
    ],
)

result = workflow.run("AI safety research")
```

### 8. AgentOS Infrastructure

**Project Setup:**
```bash
# Initialize Agno project
ag init my-agentic-app
cd my-agentic-app

# Project structure created:
# my-agentic-app/
# ├── app/           # Agent implementations
# ├── infra/         # Infrastructure config
# ├── notebooks/     # Jupyter notebooks
# ├── scripts/       # Utility scripts
# └── tests/         # Test files
```

**Infrastructure Management:**
```bash
# Spin up AgentOS infrastructure
ag infra up

# Check infrastructure status
ag infra status

# Stop infrastructure
ag infra down

# View logs
ag infra logs
```

**AgentOS Server:**
```python
from agno.os import AgentOS

# Create AgentOS with agents
agent_os = AgentOS(agents=[web_agent, finance_agent])

# Get FastAPI app
app = agent_os.get_app()

# Serve with auto-reload
if __name__ == "__main__":
    agent_os.serve("agentos:app", reload=True)
```

### 9. AgentOS API

**API Endpoints:**
- `POST /v1/agents/{agent_id}/runs` - Run an agent
- `POST /v1/teams/{team_id}/runs` - Run a team
- `POST /v1/workflows/{workflow_id}/runs` - Execute workflow
- `GET /v1/sessions` - List sessions
- `GET /v1/sessions/{session_id}` - Get session details
- `DELETE /v1/sessions/{session_id}` - Delete session

**API Usage:**
```bash
# Create agent run
curl -X POST http://localhost:7777/v1/agents/web_agent/runs \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "message": "Search for latest AI news",
    "stream": false,
    "session_id": "optional-session-id"
  }'
```

**Python API Client:**
```python
import requests

response = requests.post(
    "http://localhost:7777/v1/agents/web_agent/runs",
    headers={"Authorization": "Bearer YOUR_TOKEN"},
    json={
        "message": "What's the weather?",
        "stream": False,
    }
)

result = response.json()
print(result['content'])
```

### 10. Agent UI

**Setup Agent UI:**
```bash
# Create Agent UI
npx create-agent-ui@latest

# Start development server
cd agent-ui && npm run dev

# Access at http://localhost:3000
```

**Connect to AgentOS:**
- Enter AgentOS endpoint (e.g., `localhost:7777`)
- View agents, teams, and workflows
- Chat with agents through UI
- View memory and knowledge bases

## Implementation Patterns

### Pattern 1: Simple Single Agent
**Use Case**: Basic task with one model and tools

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    name="Research Assistant",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions=["Be accurate", "Cite sources"],
    markdown=True,
)

response = agent.print_response(
    "Latest developments in quantum computing",
    stream=True,
)
```

### Pattern 2: Agent with Memory
**Use Case**: Conversational agent with history

```python
from agno.db.postgres import PostgresDb

agent = Agent(
    name="Support Bot",
    model=OpenAIChat(id="gpt-4o-mini"),
    db=PostgresDb(db_url=DATABASE_URL),
    add_history_to_context=True,
    num_history_runs=10,
    add_datetime_to_context=True,
)

# Continues previous conversation
agent.print_response(
    "What did I ask about earlier?",
    session_id="user-123",
)
```

### Pattern 3: RAG Agent
**Use Case**: Agent with knowledge base

```python
from agno.knowledge.pdf import PDFKnowledge
from agno.vectordb.pgvector import PgVector

knowledge = PDFKnowledge(
    path="docs/",
    vector_db=PgVector(
        table_name="doc_embeddings",
        db_url=VECTOR_DB_URL,
    ),
)

agent = Agent(
    knowledge=knowledge,
    search_knowledge=True,
    instructions=[
        "Answer based on provided documents",
        "Cite specific sections",
    ],
)
```

### Pattern 4: Multi-Agent Team
**Use Case**: Complex tasks requiring specialization

```python
from agno.team import Team

researcher = Agent(
    name="Researcher",
    role="Gather data and information",
    tools=[DuckDuckGoTools(), ExaTools()],
)

analyst = Agent(
    name="Analyst",
    role="Analyze data and draw insights",
    instructions=["Use statistical methods"],
)

writer = Agent(
    name="Writer",
    role="Create comprehensive reports",
    instructions=["Professional tone", "Executive summary"],
)

team = Team(
    agents=[researcher, analyst, writer],
    instructions=[
        "Collaborate to produce high-quality reports",
        "Researcher gathers data first",
        "Analyst processes the data",
        "Writer creates final report",
    ],
)
```

### Pattern 5: Production AgentOS
**Use Case**: Deployed agentic system

```python
from agno.os import AgentOS
from agno.db.postgres import PostgresDb

# Configure production database
db = PostgresDb(db_url=os.getenv("DATABASE_URL"))

# Create agents with shared storage
web_agent = Agent(
    name="Web Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    db=db,
)

finance_agent = Agent(
    name="Finance Agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[YFinanceTools()],
    db=db,
)

# Create AgentOS
agent_os = AgentOS(
    agents=[web_agent, finance_agent],
    security_key=os.getenv("AGENTOS_SECURITY_KEY"),
)

# Export FastAPI app
app = agent_os.get_app()
```

## Best Practices

### 1. Model Selection
- **gpt-4o**: Complex reasoning, high-quality outputs
- **gpt-4o-mini**: Fast responses, cost-effective
- **claude-sonnet-4**: Large context, detailed analysis
- **gemini-2.0-flash**: Fast, multimodal tasks

### 2. Tool Configuration
- Enable only necessary tools to reduce costs
- Provide clear tool descriptions and docstrings
- Test tools individually before integration
- Handle tool errors gracefully

### 3. Memory Management
- Use PostgreSQL for production
- Set appropriate `num_history_runs` (5-20)
- Clear old sessions periodically
- Implement session expiration

### 4. Knowledge Base
- Chunk documents appropriately (500-1000 tokens)
- Use meaningful metadata for filtering
- Update embeddings when content changes
- Monitor vector database performance

### 5. Instructions
- Be specific and actionable
- Use examples when possible
- Define output format requirements
- Include edge case handling

### 6. Security
- Always set `security_key` in production
- Use environment variables for secrets
- Implement rate limiting
- Validate user inputs

### 7. Monitoring
- Log all agent interactions
- Track token usage and costs
- Monitor tool execution times
- Set up error alerting

### 8. Testing
- Unit test individual agents
- Integration test teams and workflows
- Test with edge cases
- Validate output formats

## Common Patterns

### Structured Output
```python
from pydantic import BaseModel

class Analysis(BaseModel):
    sentiment: str
    confidence: float
    key_points: list[str]

agent = Agent(
    model=OpenAIChat(
        id="gpt-4o",
        response_model=Analysis,  # Enforce structure
    )
)
```

### Streaming Responses
```python
agent = Agent(stream=True)

for chunk in agent.run("Explain quantum physics"):
    print(chunk.content, end="", flush=True)
```

### Session Management
```python
# Create new session
response = agent.run(
    "Hello",
    session_id=None,  # Auto-creates new session
)

# Continue session
agent.run(
    "Tell me more",
    session_id=response.session_id,
)
```

### Error Handling
```python
from agno.exceptions import ModelException, ToolException

try:
    response = agent.run(message)
except ModelException as e:
    print(f"Model error: {e}")
except ToolException as e:
    print(f"Tool error: {e}")
```

## Advanced Features

### 1. Custom Model Integration
```python
from agno.models.base import Model

class CustomModel(Model):
    def invoke(self, messages):
        # Custom model logic
        pass
```

### 2. Tool Caching
```python
from agno.tools import tool

@tool(cache_ttl=3600)  # Cache for 1 hour
def expensive_operation(param: str) -> str:
    # Expensive computation
    pass
```

### 3. Multi-modal Agents
```python
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[ImageTools(), VisionTools()],
)

response = agent.run(
    "Analyze this image",
    images=["path/to/image.jpg"],
)
```

### 4. Parallel Tool Execution
```python
agent = Agent(
    parallel_tool_calls=True,  # Enable parallel execution
    tools=[tool1, tool2, tool3],
)
```

## Troubleshooting

### Agent Not Responding
- Check API keys are set correctly
- Verify model availability
- Check tool configurations
- Review error logs

### Memory Issues
- Check database connection
- Verify table schemas
- Clear old sessions
- Check disk space

### Knowledge Base Problems
- Verify vector database connection
- Check embedding model configuration
- Validate document formatting
- Review chunk sizes

### Performance Issues
- Use faster models for simple tasks
- Reduce `num_history_runs`
- Optimize tool execution
- Implement caching

## Environment Setup

### Required Environment Variables
```bash
# LLM API Keys
export OPENAI_API_KEY=sk-...
export ANTHROPIC_API_KEY=sk-ant-...
export GOOGLE_API_KEY=...

# Database
export DATABASE_URL=postgresql://user:pass@host:5432/db
export VECTOR_DB_URL=postgresql://user:pass@host:5432/vectors

# AgentOS
export AGENTOS_SECURITY_KEY=your-secret-key
export AGENTOS_PORT=7777

# Tool-specific
export X_API_KEY=...
export EXA_API_KEY=...
```

### Dependencies
```bash
# Core
pip install agno

# Database
pip install sqlalchemy psycopg2-binary

# Tools (as needed)
pip install duckduckgo-search yfinance

# Web framework
pip install "fastapi[standard]"
```

## Production Deployment

### Docker Deployment
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "uvicorn", "agentos:app", "--host", "0.0.0.0", "--port", "7777"]
```

### Infrastructure
```bash
# Start services
docker-compose up -d

# Scale AgentOS
docker-compose up --scale agentos=3
```

### Monitoring
```python
from agno.monitoring import setup_monitoring

setup_monitoring(
    prometheus_port=9090,
    log_level="INFO",
)
```

## Quick Reference

### Agent Creation
```python
Agent(
    name="Agent Name",
    model=OpenAIChat(id="gpt-4o"),
    tools=[Tool1(), Tool2()],
    instructions=["Instruction 1"],
    db=database,
    knowledge=knowledge_base,
    markdown=True,
    show_tool_calls=True,
)
```

### Team Creation
```python
Team(
    agents=[agent1, agent2],
    instructions=["Team instructions"],
)
```

### AgentOS Setup
```python
agent_os = AgentOS(
    agents=[agent1, agent2],
    security_key="secret",
)
app = agent_os.get_app()
```

### Run Agent
```python
# Direct run
response = agent.run("message")

# Print with streaming
agent.print_response("message", stream=True)

# With session
agent.run("message", session_id="session-123")
```

## Resources

- **Documentation**: https://docs.agno.com/
- **GitHub**: https://github.com/agno-agi/agno
- **Discord**: Join the Agno community
- **Examples**: https://github.com/agno-agi/agno/tree/main/cookbook

## Skill Metadata

**Version**: 1.0  
**Last Updated**: 2025-01-29  
**Agno Version**: Latest  
**Skill Type**: Technical Framework  
**Expertise Level**: Senior Developer
