from agno.agent import Agent
from agno.models.groq import Groq

reviewer_agno = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    description="You are an editor. Review blog posts, fix grammar, improve clarity and engagement. Return only the improved version.",
)

def review_agent(content):
    result = reviewer_agno.run(f"Review and improve this blog post. Return the improved version only:\n\n{content}")
    return getattr(result, 'content', str(result))
