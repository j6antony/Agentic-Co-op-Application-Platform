# Co-op Agent Platform

An end-to-end LLM-powered co-op application platform for managing job postings, resumes, application tracking, and AI-assisted job analysis.

The goal of this project is to build a production-style full-stack application using a real backend, database, Dockerized infrastructure, and eventually LLM/agent workflows.

## Current Scope

The first version focuses on building the foundation:

- FastAPI backend
- PostgreSQL database running through Docker
- Job posting storage
- Basic API endpoints
- Future Next.js frontend

## Planned Features

- Paste and save job postings
- Parse job postings using an LLM
- Upload resumes
- Compare resumes against job postings
- Generate resume suggestions
- Generate cover letters
- Generate interview prep questions
- Track application statuses
- Add background workers for longer AI tasks
- Add CI/CD and production deployment

## Tech Stack

- Frontend: Next.js, TypeScript
- Backend: FastAPI, Python
- Database: PostgreSQL
- Infrastructure: Docker Compose
- Future: Redis, pgvector, LangGraph/OpenAI Agents, GitHub Actions

## Running the Database

From the project root:

```bash
docker compose -f infra/docker-compose.yml up -d