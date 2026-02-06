from agno.agent import Agent
from agno.models.groq import Groq

seo_agno = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    description="You are an SEO expert. Add SEO title, meta description, and keywords to blog posts. Return the final blog with SEO elements at the top.",
)

def seo_agent(content):
    result = seo_agno.run(f"Add SEO title, meta description, and keywords to this blog. Return the final blog with SEO elements at the top:\n\n{content}")
    return getattr(result, 'content', str(result))
