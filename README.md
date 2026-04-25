# DevOps Bootcamp — End-to-End MLOps Project

![CI Pipeline](https://github.com/harri05/devops-bootcamp/actions/workflows/ci.yml/badge.svg)

## 🏗️ Architecture

## 🚀 Stack

| Layer | Technology |
|-------|-----------|
| App | Python, Flask |
| Container | Docker, multi-stage build |
| CI/CD | GitHub Actions |
| Registry | Docker Hub |
| Orchestration | Kubernetes (coming soon) |
| GitOps | ArgoCD + Helm (coming soon) |
| Monitoring | Prometheus + Grafana (coming soon) |
| AIOps | ML model registry (coming soon) |

## 🏃 Run Locally

```bash
git clone https://github.com/harri05/devops-bootcamp.git
cd devops-bootcamp
docker compose up -d
curl http://localhost:5000/health
```

## 📡 Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /` | Home — returns host + request count |
| `GET /health` | Health check — used by Kubernetes |
| `GET /info` | App info + environment |
| `GET /metrics-preview` | Request counter + uptime |
