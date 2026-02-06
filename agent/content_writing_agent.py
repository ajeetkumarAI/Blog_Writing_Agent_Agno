from agno.agent import Agent
from agno.models.groq import Groq

writer_agno = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    description="You are a professional blog writer. Write detailed, engaging, SEO-friendly blog posts. Do not repeat the prompt in the output.",
)

def content_writing_agent(topic, outline, web_info):
    result = writer_agno.run(f"Write a detailed blog post about: {topic}. Follow this outline: {outline}. Use this research: {web_info}")
    return getattr(result, 'content', str(result))
