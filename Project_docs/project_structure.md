# AutoGen Planner with Gradio UI - Project Structure

This document outlines the recommended project structure for the AutoGen Planner with Gradio UI application, following industry best practices for maintainability, scalability, and deployment.

## Overview

The project is structured with a clear separation between frontend and backend components to facilitate independent development, testing, and deployment. This separation follows standard practices in full-stack development.

## Project Structure

```
.
├── README.md                       # Project documentation
├── .gitignore                      # Git ignore file
├── .env.example                    # Environment variables template
├── backend/                        # Backend server
│   ├── requirements.txt            # Backend dependencies
│   ├── setup.py                    # Backend package installation
│   ├── pyproject.toml              # Project metadata and build system
│   ├── src/
│   │   └── autogen_planner/        # Main backend package
│   │       ├── __init__.py         # Package initialization
│   │       ├── api/                # API endpoints
│   │       │   ├── __init__.py
│   │       │   ├── routes.py       # API routes
│   │       │   └── schemas.py      # API request/response schemas
│   │       ├── agents/             # AutoGen agents
│   │       │   ├── __init__.py
│   │       │   ├── base.py         # Base agent class
│   │       │   ├── user_agent.py   # User interaction agent
│   │       │   └── plan_agent.py   # Planning agent
│   │       ├── config/             # Configuration
│   │       │   ├── __init__.py
│   │       │   └── settings.py     # Application settings
│   │       ├── services/           # External services
│   │       │   ├── __init__.py
│   │       │   └── ai/
│   │       │       ├── __init__.py
│   │       │       ├── base.py     # Base AI client
│   │       │       └── gemini.py   # Gemini API client
│   │       ├── utils/              # Utility functions
│   │       │   ├── __init__.py
│   │       │   └── logging.py      # Logging utilities
│   │       └── main.py             # Backend entry point
│   └── tests/                      # Backend tests
│       ├── __init__.py
│       ├── conftest.py             # Test fixtures and configuration
│       ├── unit/                   # Unit tests
│       │   ├── __init__.py
│       │   ├── agents/             # Tests for agents
│       │   │   ├── __init__.py
│       │   │   ├── test_user_agent.py
│       │   │   └── test_plan_agent.py
│       │   └── services/           # Tests for services
│       │       ├── __init__.py
│       │       └── ai/
│       │           ├── __init__.py
│       │           └── test_gemini.py
│       └── integration/            # Integration tests
│           ├── __init__.py
│           └── test_api.py         # API integration tests
├── frontend/                       # Frontend application
│   ├── requirements.txt            # Frontend dependencies
│   ├── src/
│   │   └── gradio_app/             # Gradio application
│   │       ├── __init__.py
│   │       ├── app.py              # Main Gradio app
│   │       ├── components/         # UI components
│   │       │   ├── __init__.py
│   │       │   ├── chat.py         # Chat interface
│   │       │   └── plan_display.py # Plan display component
│   │       ├── api_client.py       # Client for backend API
│   │       └── utils/              # Frontend utilities
│   │           ├── __init__.py
│   │           └── formatting.py   # Text formatting utilities
│   └── tests/                      # Frontend tests
│       ├── __init__.py
│       └── test_components/
│           ├── __init__.py
│           └── test_chat.py        # Tests for chat component
├── deployment/                     # Deployment configurations
│   ├── docker-compose.yml          # Local deployment with Docker
│   ├── backend/
│   │   ├── Dockerfile              # Backend Docker configuration
│   │   └── gunicorn.conf.py        # Gunicorn configuration
│   └── frontend/
│       └── Dockerfile              # Frontend Docker configuration
├── docs/                           # Documentation
│   ├── architecture/               # Architecture diagrams and docs
│   │   └── system_overview.md      # System architecture overview
│   ├── api/                        # API documentation
│   │   └── endpoints.md            # API endpoints documentation
│   └── user_guides/                # User guides and tutorials
│       └── getting_started.md      # Getting started guide
└── scripts/                        # Utility scripts
    ├── setup_dev_env.sh            # Development environment setup
    └── run_local.sh                # Script to run locally
```

## Component Details

### Backend

The backend is responsible for:
- Implementing the AutoGen agents
- Processing user requests
- Communicating with the Gemini AI model
- Exposing API endpoints for the frontend

Key components:
- **API**: Defines the interface between frontend and backend
- **Agents**: Implements the AutoGen agents for user interaction and planning
- **Services**: Handles external service integrations, such as the Gemini AI model

### Frontend

The frontend is responsible for:
- Providing a user interface with Gradio
- Collecting user input
- Displaying execution plans
- Communicating with the backend API

Key components:
- **App**: Main Gradio application
- **Components**: Reusable UI components
- **API Client**: Client for communicating with the backend API

### Deployment

The deployment directory contains configuration files for deploying the application:
- Docker Compose for local deployment
- Dockerfiles for containerization
- Configuration files for production deployment

## Development Workflow

1. **Local Development**:
   - Run backend and frontend separately during development
   - Use the provided scripts in the `scripts/` directory

2. **Testing**:
   - Run backend tests with `pytest backend/tests/`
   - Run frontend tests with `pytest frontend/tests/`

3. **Deployment**:
   - Use Docker Compose for local deployment: `docker-compose -f deployment/docker-compose.yml up`
   - For production, deploy backend and frontend separately using their respective Dockerfiles

## Benefits of This Structure

1. **Separation of Concerns**:
   - Clear separation between frontend and backend
   - Each component has a single responsibility

2. **Scalability**:
   - Components can be scaled independently
   - New features can be added to the appropriate component

3. **Maintainability**:
   - Well-organized code is easier to maintain
   - Clear boundaries between components

4. **Deployment Flexibility**:
   - Components can be deployed separately
   - Different deployment strategies can be used for each component

5. **Testing**:
   - Components can be tested independently
   - Clear boundaries make testing easier
