# Sprint 01 — Backend e Autenticação

## 1. Objetivo

Construir a fundação do backend do Orbe e implementar o primeiro fluxo completo de autenticação de usuários.

Ao final do sprint, o sistema deve permitir:

- criar usuários;
- armazenar senhas de forma segura;
- autenticar usuários;
- gerar tokens JWT;
- identificar usuários autenticados;
- proteger endpoints da API.

---

## 2. Tecnologias

- Python
- FastAPI
- SQLAlchemy
- Alembic
- MySQL 8
- Pydantic
- Pydantic Settings
- PyJWT
- pwdlib
- Argon2
- pytest
- Docker

---

## 3. Arquitetura

O backend utiliza uma arquitetura organizada por responsabilidades:

```text
API
 ↓
Services
 ↓
Models / Database