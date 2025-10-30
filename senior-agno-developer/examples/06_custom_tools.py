"""
Custom Tools Example
===================
Demonstrates creating and using custom tools with agents.
"""

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import tool
from typing import Optional

# Define custom tools
@tool
def calculate_roi(investment: float, returns: float) -> dict:
    """Calculate return on investment percentage.
    
    Args:
        investment: Initial investment amount in dollars
        returns: Total returns amount in dollars
    
    Returns:
        Dictionary with ROI percentage and profit
    """
    profit = returns - investment
    roi_percentage = (profit / investment) * 100
    
    return {
        "investment": investment,
        "returns": returns,
        "profit": profit,
        "roi_percentage": round(roi_percentage, 2),
    }

@tool
def compound_interest(
    principal: float,
    rate: float,
    time: int,
    compounds_per_year: int = 12
) -> dict:
    """Calculate compound interest.
    
    Args:
        principal: Initial principal amount
        rate: Annual interest rate (as percentage, e.g., 5 for 5%)
        time: Time period in years
        compounds_per_year: Number of times interest compounds per year
    
    Returns:
        Dictionary with final amount and interest earned
    """
    rate_decimal = rate / 100
    amount = principal * (1 + rate_decimal / compounds_per_year) ** (compounds_per_year * time)
    interest = amount - principal
    
    return {
        "principal": principal,
        "rate": rate,
        "time_years": time,
        "final_amount": round(amount, 2),
        "interest_earned": round(interest, 2),
    }

# Create agent with custom tools
agent = Agent(
    name="Financial Calculator",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[calculate_roi, compound_interest],
    instructions=[
        "Help users with financial calculations",
        "Explain results clearly",
        "Use tables for multi-scenario comparisons",
    ],
    markdown=True,
    show_tool_calls=True,
)

if __name__ == "__main__":
    # Test the agent
    response = agent.print_response(
        "If I invest $10,000 and get back $15,000, what's my ROI? "
        "Also, show me what $10,000 grows to in 5 years at 7% interest.",
        stream=True,
    )
