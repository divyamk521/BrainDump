# BrainDump

BrainDump is a production-grade multimodal AI-powered **Second Brain** that allows users to capture, organize, search, and chat with everything they know.

Instead of storing information across bookmarks, screenshots, PDFs, notes, voice memos, and articles, BrainDump centralizes everything into a single knowledge base powered by Retrieval-Augmented Generation (RAG).

Users can upload:

- Text notes
- PDFs
- Images
- Screenshots
- Voice recordings
- YouTube links
- Web articles
- URLs

BrainDump processes each piece of content using AI, stores semantic embeddings, and enables natural language conversations across the entire personal knowledge base.

---

# Tech Stack

## Backend

- Python 3.11+
- FastAPI (Async)
- PostgreSQL
- SQLAlchemy Async
- Alembic
- Redis
- Celery
- Qdrant
- LangChain
- LangGraph
- Groq API
- Faster Whisper
- Unstructured.io

---

## Frontend

- Next.js 14
- TypeScript
- Tailwind CSS
- shadcn/ui
- Zustand
- TanStack Query
- Framer Motion

---

## AI Stack

- BAAI/bge-m3 Embeddings
- Groq LLMs
- Faster Whisper
- OCR
- Hybrid Search
- LangGraph Agents

---

# Project Structure

```
BrainDump/

│

├── backend/

│ ├── app/

│ │ ├── api/

│ │ ├── core/

│ │ ├── models/

│ │ ├── schemas/

│ │ ├── services/

│ │ ├── rag/

│ │ │ ├── ingestion/

│ │ │ ├── embeddings/

│ │ │ ├── retrieval/

│ │ │ └── graph/

│ │ ├── tasks/

│ │ └── utils/

│ │

│ ├── tests/

│ ├── requirements.txt

│ └── Dockerfile

│

├── frontend/

├── infra/

│ └── docker-compose.dev.yml

│

├── .env

├── .env.example

├── .gitignore

└── README.md
```

---

# Development Workflow

During development **only the databases run inside Docker**.

The FastAPI backend runs locally using **uvicorn**.

The Next.js frontend also runs locally using **npm run dev**.

Application containerization will happen later during **Phase 3**.

---

# Prerequisites

Install:

- Docker Desktop
- Python 3.11+
- Git

Verify installation:

```bash
docker --version

python --version

git --version
```

---

# Clone Repository

```bash
git clone <repository-url>

cd BrainDump
```

---

# Start Development Databases

Run:

```bash
docker compose -f infra/docker-compose.dev.yml up -d
```

Verify:

```bash
docker ps
```

You should see:

- PostgreSQL
- Redis
- Qdrant

running successfully.

---

# Create Python Virtual Environment

Inside the backend folder:

```bash
cd backend

python -m venv .venv
```

Activate it:

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```