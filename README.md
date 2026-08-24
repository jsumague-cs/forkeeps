# Forkeeps

Forkeeps is a collaborative planning and organization application designed for couples. It provides a shared digital space where partners can manage tasks, plans, finances, and other aspects of their everyday lives while maintaining separate user accounts.

## Overview

Forkeeps is built around the concept of a **shared couple space**. Each partner maintains their own account and can be connected to a shared space with their partner. This allows both users to collaborate without requiring a shared login.

The application aims to reduce the friction of coordinating responsibilities and plans by bringing commonly shared activities into a single platform.

## Core Features

* **User Authentication** — Individual accounts with secure authentication.
* **Couple Spaces** — Two individual accounts can be connected through a shared space.
* **Shared Tasks** — Create, assign, and track responsibilities together.
* **Planning** — Organize schedules, activities, and important plans.
* **Budget Tracking** — Monitor shared expenses and financial activities.
* **Shared Data** — Keep relevant information synchronized between both partners.
* **Personal Data Isolation** — Individual account data remains separate from shared couple data.

## 🛠️ Tech Stack

### 📱 Frontend
- React Native
- Expo
- TypeScript
- Expo Router
- Figma — UI/UX Design

### ⚙️ Backend
- Python
- Flask — REST API
- Flask-SQLAlchemy — ORM
- Flask-Migrate / Alembic — Database Migrations

### 🗄️ Database
- PostgreSQL

### 📸 Storage
**Planned**
- Amazon S3 — Photo and object storage

### 🤖 AI
**Planned**
- Vision-capable AI API — Image analysis and organization
- Embeddings + Vector Search — Semantic memory search

### ☁️ Infrastructure & DevOps
**Planned**
- Docker — Containerization
- GitHub Actions — CI/CD
- AWS — Cloud infrastructure and deployment

### 🧰 Development Tools
- VS Code
- Git
- GitHub
- Figma
- Postman / Insomnia — API testing
## Architecture

Forkeeps follows a client-server architecture with a dedicated backend API and frontend application.

```text
Frontend
   |
   | HTTP / REST API
   v
Backend
   |
   v
Database
```

The backend is responsible for authentication, authorization, business logic, data validation, and persistence. The frontend consumes the API and provides the user interface.

## Data Model

The application distinguishes between **user-owned data** and **couple-owned data**.

```text
User
 └── Couple Membership
       └── Couple Space
            ├── Tasks
            ├── Plans
            └── Shared Expenses
```

This structure allows Forkeeps to support collaboration while preserving clear ownership and access boundaries.

## Development Status

| Component      | Status      |
| -------------- | ----------- |
| Backend        | Completed   |
| Database       | Completed   |
| Authentication | Implemented |
| API            | Implemented |
| UI/UX Design   | In Progress |
| Frontend       | In Progress |
| Deployment     | Planned     |

## Project Goals

1. Build a practical collaborative application with a clear user experience.
2. Implement secure account and authorization flows.
3. Establish a scalable backend architecture.
4. Maintain clear separation between personal and shared data.
5. Deliver a responsive and intuitive frontend experience.

## Future Improvements

* Real-time synchronization
* Push notifications and reminders
* Calendar integration
* Recurring tasks
* Expense splitting and summaries
* Activity history
* Improved personalization
* Production deployment and monitoring

## Project Structure

The repository is organized around the application's backend and frontend components, with supporting documentation and configuration maintained alongside the source code.

## Development

Forkeeps is currently under active development. The backend foundation is complete, while the frontend implementation is being developed from the finalized UI/UX designs.

---

**Forkeeps** — A shared space for planning life together.
