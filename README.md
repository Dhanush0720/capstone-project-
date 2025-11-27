Smart Career Path Recommendation Agent
A Multi-Agent AI System Using Gemini + Google Agent Framework
🚀 Overview

Choosing the right career path is confusing for most students. They do not know which jobs align with their skills, interests, or market trends. This project solves that problem using a multi-agent AI system powered by Gemini.

The system takes the user's skills & interests → analyzes market trends → produces the most accurate career recommendations with explanations & skill-gap roadmap.

🧠 Why This Project?

This project meets the Kaggle Capstone requirements by demonstrating:

✔ Multi-agent system
✔ Tools (Google Search, Code Execution, custom matching tool)
✔ Sessions & Memory
✔ Context engineering
✔ Logging & Observability
✔ Effective use of Gemini
✔ Modular architecture
✔ Deployment-ready design

🎯 Problem

Students struggle to identify a suitable career path. Existing tools are:

Not personalized

Not dynamic

Not aligned with real job market trends

Not explainable

💡 Solution

A four-agent system:

1. Profile Analyzer Agent

Parses user input → generates structured JSON profile
(uses Gemini for extraction)

2. Job Market Research Agent

Uses Google Search + Tools to fetch real-time trends.

3. Career Matching Agent

Matches user profile → job demand → computes best-fit roles.

4. Explainer Agent

Creates a final report:

recommended careers

why those careers

skill-gap analysis

learning roadmap

🏗 Architecture
User → Profile Analyzer Agent → Job Market Agent
     → Career Matching Agent → Explainer Agent → Final Report


Each agent runs sequentially with memory stored between steps.

🔑 Key Concepts Used (Required ≥3)

✔ Multi-agent system (Sequential + parallel)
✔ MCP Tools (Google Search, Code Execution)
✔ Sessions & Memory
✔ Context Engineering
✔ Observability (Logging, Tracing)
✔ Gemini Integration

📁 Project Structure
career-agent/
│── agents/
│    ├── profile_agent.py
│    ├── job_agent.py
│    ├── matcher_agent.py
│    └── explainer_agent.py
│
│── tools/
│    ├── market_search.py
│    └── skill_matcher.py
│
│── main.py
│── requirements.txt
│── README.md
