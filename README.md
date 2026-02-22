# 🎓 Exam Generator: Intelligent Multi-Agent Assessment Designer

**Transform your course materials into "distinction-level" university examinations with the power of Multi-Agent RAG orchestration.**

---

## 🚀 Overview

Exam Generator is a sophisticated full-stack application designed to automate the creation of high-quality, conceptually deep academic problems. Leveraging a Multi-Agent architecture built on **LangGraph**, the system retrieves relevant knowledge from a vector store, identifies key learning objectives, and designs multi-part problems that test both foundational understanding and complex application.

## ✨ Features

- **Multi-Agent Orchestration**: A specialized hierarchy of LLM agents (Topic Selector → Problem Designer → Exam Compiler) coordinated via LangGraph state machines.
- **RAG-Driven Retrieval**: Uses **Pinecone** vector database to ground problem generation in specific course content and source materials.
- **Deep Conceptual Testing**: Specifically engineered prompts that move beyond simple calculations to "distinction-level" proofs and limit-case analysis.
- **Professional Math Rendering**: Frontend integrated with **KaTeX** and **Tiptap** for beautiful, LaTeX-compliant mathematical expression editing.
- **Robust API Layer**: Built with **FastAPI**, featuring comprehensive error handling and structured JSON responses.

## 🛠️ Tech Stack

### Backend
- **Core**: Python 13+
- **Agent Framework**: LangGraph, LangChain
- **API Framework**: FastAPI
- **Database**: Pinecone (Vector Store)
- **AI Models**: OpenAI / Anthropic integration

### Frontend
- **Framework**: React, TypeScript, Vite
- **Editor**: Tiptap (with custom Mathematics extension)
- **Styling**: Vanilla CSS (Modern, Responsive)

## 🧠 Key Logic Highlight: Multi-Agent State Machine

The heart of the project is the `ExamAgent` orchestration. Unlike simple linear chains, Exam Generator uses a directed acyclic graph (DAG) to manage the problem creation lifecycle:

1.  **Topic Selector**: Retrieves knowledge from Pinecone and selects the most relevant academic topics.
2.  **Conditional Logic**: The agent evaluates the "usability" of selected topics; if they aren't deep enough, it loops back to re-select, ensuring quality.
3.  **Problem Designer**: Orchestrated parallel execution to design multiple problem parts simultaneously, ensuring a cohesive and challenging final exam.
4.  **Exam Compiler**: Aggregates agent outputs into a structured, ready-to-use exam format.

## ⚙️ Setup Instructions

### Prerequisites
- Python 3.13+
- Node.js & npm
- Pinecone API Key
- OpenAI API Key

### Backend Setup
1. Navigate to the `backend` directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt  # Or use uv sync
   ```
3. Configure your environment variables in a `.env` file (see `config.py`).
4. Start the server:
   ```bash
   uvicorn api.app:app --reload
   ```

### Frontend Setup
1. Navigate to the `frontend` directory.
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```

---

*Built with ❤️ for professional educators and students.*
