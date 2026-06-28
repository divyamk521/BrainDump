# BrainDump

BrainDump is a multimodal AI-powered second brain.

Users can store:

- Text
- PDFs
- Images
- Screenshots
- Audio
- URLs
- Notes

and later chat with all of their knowledge using Retrieval-Augmented Generation (RAG).

---

## Tech Stack

### Backend

- FastAPI
- PostgreSQL
- SQLAlchemy Async
- Alembic
- Qdrant
- Redis
- Celery
- LangChain
- LangGraph
- Groq
- Faster Whisper

### Frontend

- Next.js 14
- TypeScript
- TailwindCSS
- shadcn/ui

---

## Development Setup

Start the development databases:

```bash
docker compose -f infra/docker-compose.dev.yml up -d
```

Check containers:

```bash
docker ps
```

Later, the backend will be started with:

```bash
uvicorn app.main:app --reload
```

The FastAPI application is intentionally **not** containerized during development. It runs locally and connects to the Dockerized PostgreSQL, Redis, and Qdrant services.

The frontend will also run locally during development.

Application containerization will be completed during Phase 3.