"""
RAG Agent Example
================
Demonstrates creating an agent with knowledge base for RAG.
"""

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.knowledge.pdf import PDFKnowledge
from agno.vectordb.pgvector import PgVector
import os

# Configure vector database
vector_db = PgVector(
    table_name="doc_embeddings",
    db_url=os.getenv("VECTOR_DB_URL", "postgresql://localhost:5432/vectors"),
)

# Create knowledge base from PDFs
knowledge = PDFKnowledge(
    path="docs/",  # Directory with PDF files
    vector_db=vector_db,
)

# Create RAG agent
agent = Agent(
    name="Document Assistant",
    model=OpenAIChat(id="gpt-4o"),
    knowledge=knowledge,
    search_knowledge=True,
    instructions=[
        "Answer based on the provided documents",
        "Cite specific sections when possible",
        "If information isn't in documents, say so",
    ],
    markdown=True,
)

if __name__ == "__main__":
    # Query the knowledge base
    response = agent.print_response(
        "What are the key findings in the research papers?",
        stream=True,
    )
