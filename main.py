import streamlit as st
from agent.web_search_agent import search
from agent.outline_agent import outline_agent
from agent.content_writing_agent import content_writing_agent
from agent.review_agent import review_agent
from agent.seo_agent import seo_agent

st.title("AI Blog Writing Smart Agent Team")
st.write("Enter a blog topic. The pipeline will: Web Search → Outline → Write → Review → SEO")

user_query = st.text_input("Enter your blog topic")

if st.button("Generate Blog") and user_query:
    with st.spinner("Step 1: Searching the web..."):
        web_info = search(user_query)

    with st.spinner("Step 2: Creating outline..."):
        outline = outline_agent(user_query, web_info)

    with st.spinner("Step 3: Writing blog..."):
        blog = content_writing_agent(user_query, outline, web_info)

    with st.spinner("Step 4: Reviewing & improving..."):
        reviewed = review_agent(blog)

    with st.spinner("Step 5: Adding SEO..."):
        final = seo_agent(reviewed)

    st.subheader("Final Blog Output")
    st.markdown(final)
