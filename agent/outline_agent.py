from agno.agent import Agent
from agno.models.groq import Groq

outline_agno = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    description="You are a blog outline expert. Create detailed blog outlines with clear sections and sub-points.",
)

def outline_agent(topic, web_info):
    result = outline_agno.run(f"Create a detailed blog outline for: {topic}. Use this research: {web_info}")
    return getattr(result, 'content', str(result))
