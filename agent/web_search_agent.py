from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools
from dotenv import load_dotenv
import os
load_dotenv()

web_search_agent = Agent(
    model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"),
    tools=[TavilyTools(api_key=os.getenv("TAVILY_API_KEY"))],
    description="You are a web research agent. Search the web and return key facts and info.",
)

def search(query):
    result = web_search_agent.run(query)
    return getattr(result, 'content', str(result))

# web_search_agent = Agent(
#     model=Groq(id="llama-3.3-70b-versatile"),
#     tools=[TavilyTools(api_key=os.getenv("TAVILY_API_KEY"))],
#     description="You are a web research agent. Search the web and return key facts and info.",
# )

# def search(query):
#     result = web_search_agent.run(query)
#     return getattr(result, 'content', str(result))
