# AutoGen Planner - System Architecture Overview

This document provides an overview of the AutoGen Planner system architecture.

## System Components

The AutoGen Planner system consists of the following main components:

1. **Frontend (Gradio UI)**
   - Provides a user-friendly interface for interacting with the system
   - Communicates with the backend API to send requests and receive responses
   - Displays execution plans in a readable format

2. **Backend (FastAPI)**
   - Hosts the AutoGen agents
   - Provides API endpoints for the frontend
   - Communicates with the Gemini AI model

3. **AutoGen Agents**
   - **User Agent**: Handles user interactions and formats requests
   - **Plan Agent**: Generates execution plans using the Gemini AI model

4. **External Services**
   - **Gemini AI**: Provides the AI capabilities for generating execution plans

## Component Interactions

The following diagram illustrates the interactions between the components:

```
+----------------+        +----------------+        +----------------+
|                |        |                |        |                |
|   Gradio UI    | <----> |   FastAPI      | <----> |   AutoGen      |
|   (Frontend)   |        |   (Backend)    |        |   Agents       |
|                |        |                |        |                |
+----------------+        +----------------+        +-------+--------+
                                                           |
                                                           v
                                                   +----------------+
                                                   |                |
                                                   |   Gemini AI    |
                                                   |   Model        |
                                                   |                |
                                                   +----------------+
```

## Data Flow

1. The user submits a request through the Gradio UI.
2. The frontend sends the request to the backend API.
3. The backend processes the request through the User Agent.
4. The User Agent formats the request and passes it to the Plan Agent.
5. The Plan Agent generates a prompt for the Gemini AI model.
6. The Gemini AI model generates an execution plan.
7. The Plan Agent processes the response and returns it to the User Agent.
8. The User Agent formats the response and returns it to the backend API.
9. The backend API returns the response to the frontend.
10. The frontend displays the execution plan to the user.

## Deployment Architecture

The system is designed to be deployed in a variety of environments:

1. **Local Development**
   - Frontend and backend run on the same machine
   - Useful for development and testing

2. **Containerized Deployment**
   - Frontend and backend run in separate containers
   - Managed by Docker Compose
   - Suitable for production environments

3. **Cloud Deployment**
   - Frontend and backend deployed to separate cloud services
   - Scalable and resilient
   - Suitable for high-traffic applications

## Security Considerations

1. **API Key Management**
   - Gemini API key stored securely in environment variables
   - Not exposed to the frontend

2. **CORS Configuration**
   - Backend configured to accept requests only from trusted origins

3. **Input Validation**
   - All user inputs validated before processing

## Performance Considerations

1. **Caching**
   - Frequently used plans can be cached to improve performance

2. **Asynchronous Processing**
   - FastAPI supports asynchronous request handling

3. **Scalability**
   - Backend can be scaled horizontally to handle increased load 