# 🤖 Multi-Agent Blog Writing Pipeline — High Level Overview

This project uses **5 AI Agents** built with **Agno + Groq LLMs** to generate a complete, SEO-optimized blog post from a single topic.

---

## 🔄 Pipeline Flow

```
User Input (Topic)
      │
      ▼
┌─────────────────────┐
│  1. Web Search Agent │  ──→  Searches the internet for latest info
└─────────────────────┘
      │ web_info
      ▼
┌─────────────────────┐
│  2. Outline Agent    │  ──→  Creates a structured blog outline
└─────────────────────┘
      │ outline
      ▼
┌─────────────────────┐
│  3. Content Writer   │  ──→  Writes the full blog post
└─────────────────────┘
      │ blog
      ▼
┌─────────────────────┐
│  4. Review Agent     │  ──→  Reviews & improves grammar, clarity
└─────────────────────┘
      │ reviewed
      ▼
┌─────────────────────┐
│  5. SEO Agent        │  ──→  Adds SEO title, meta, keywords
└─────────────────────┘
      │ final
      ▼
   Final Blog Output (shown in Streamlit UI)
```

---

## 📌 Pipeline Code (main.py)

```python
# Step 1: Web Search
web_info = search(user_query)

# Step 2: Create Outline
outline = outline_agent(user_query, web_info)

# Step 3: Write Blog
blog = content_writing_agent(user_query, outline, web_info)

# Step 4: Review & Improve
reviewed = review_agent(blog)

# Step 5: Add SEO
final = seo_agent(reviewed)
```

---

## 🧠 Agent Details

### 1️⃣ Web Search Agent
| Item | Detail |
|------|--------|
| **File** | `agent/web_search_agent.py` |
| **Model** | `llama-3.3-70b-versatile` (Groq) |
| **Tool** | TavilyTools (real-time web search) |
| **Description** | `"You are a web research agent. Search the web and return key facts and info."` |
| **Prompt** | The user's topic is directly passed as the query |
| **Input** | `user_query` (e.g., "AI Agent") |
| **Output** | `web_info` — latest facts, stats, and info from the web |

---

### 2️⃣ Outline Agent
| Item | Detail |
|------|--------|
| **File** | `agent/outline_agent.py` |
| **Model** | `llama-3.3-70b-versatile` (Groq) |
| **Description** | `"You are a blog outline expert. Create detailed blog outlines with clear sections and sub-points."` |
| **Prompt** | `"Create a detailed blog outline for: {topic}. Use this research: {web_info}"` |
| **Input** | `user_query` + `web_info` |
| **Output** | `outline` — structured blog sections and sub-points |

---

### 3️⃣ Content Writing Agent
| Item | Detail |
|------|--------|
| **File** | `agent/content_writing_agent.py` |
| **Model** | `mixtral-8x7b-32768` (Groq) |
| **Description** | `"You are a professional blog writer. Write detailed, engaging, SEO-friendly blog posts. Do not repeat the prompt in the output."` |
| **Prompt** | `"Write a detailed blog post about: {topic}. Follow this outline: {outline}. Use this research: {web_info}"` |
| **Input** | `user_query` + `outline` + `web_info` |
| **Output** | `blog` — full detailed blog post |

---

### 4️⃣ Review Agent
| Item | Detail |
|------|--------|
| **File** | `agent/review_agent.py` |
| **Model** | `llama-3.1-8b-instant` (Groq) |
| **Description** | `"You are an editor. Review blog posts, fix grammar, improve clarity and engagement. Return only the improved version."` |
| **Prompt** | `"Review and improve this blog post. Return the improved version only:\n\n{content}"` |
| **Input** | `blog` (from content writer) |
| **Output** | `reviewed` — improved, polished blog post |

---

### 5️⃣ SEO Agent
| Item | Detail |
|------|--------|
| **File** | `agent/seo_agent.py` |
| **Model** | `gemma2-9b-it` (Groq) |
| **Description** | `"You are an SEO expert. Add SEO title, meta description, and keywords to blog posts. Return the final blog with SEO elements at the top."` |
| **Prompt** | `"Add SEO title, meta description, and keywords to this blog. Return the final blog with SEO elements at the top:\n\n{content}"` |
| **Input** | `reviewed` (from review agent) |
| **Output** | `final` — SEO-optimized blog with title, meta, keywords |

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| **Agno** | Agent framework (creates AI agents) |
| **Groq** | LLM provider (fast inference) |
| **TavilyTools** | Real-time web search |
| **Streamlit** | Web UI for user interaction |
| **python-dotenv** | Load API keys from `.env` |

---

## 🔑 Key Concepts for Students

1. **Agent** = An AI program with a specific role, model, and instructions
2. **Pipeline** = Agents connected in sequence — output of one feeds into the next
3. **Each agent uses a different LLM model** — this shows how to pick the right model for each task
4. **Web Search Agent** has a **tool** (Tavily) — other agents only use their LLM brain
5. **Prompt Engineering** — each agent gets a carefully crafted prompt to do its job well

---

## 📂 Project Structure

```
Streamlit_demo/
├── main.py                          # Streamlit UI + Pipeline
├── requirements.txt                 # Dependencies
├── .env                             # API Keys (GROQ_API_KEY, TAVILY_API_KEY)
├── agent/
│   ├── __init__.py
│   ├── web_search_agent.py          # Agent 1: Web Search
│   ├── outline_agent.py             # Agent 2: Blog Outline
│   ├── content_writing_agent.py     # Agent 3: Blog Writer
│   ├── review_agent.py              # Agent 4: Editor/Reviewer
│   └── seo_agent.py                 # Agent 5: SEO Optimizer
```

# How to run the Streamlit app

1. Open a terminal in this folder.
2. Run the following command:
```bash
    streamlit run app.py
```

3. Your browser will open with the app. If not, copy the link from the terminal and open it manually.
