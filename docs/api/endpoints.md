# AutoGen Planner - API Endpoints

This document describes the API endpoints provided by the AutoGen Planner backend.

## Base URL

All endpoints are relative to the base URL:

```
http://localhost:8000/api/v1
```

In production, this would be replaced with your domain.

## Authentication

Currently, the API does not require authentication. In a production environment, you would want to add authentication to secure the API.

## Endpoints

### Create Plan

Creates an execution plan based on a user query.

- **URL**: `/plan`
- **Method**: `POST`
- **Content Type**: `application/json`

#### Request Body

```json
{
  "query": "string"
}
```

| Field | Type | Description |
|-------|------|-------------|
| query | string | The user query to generate a plan for |

#### Response

```json
{
  "plan": "string"
}
```

| Field | Type | Description |
|-------|------|-------------|
| plan | string | The generated execution plan |

#### Example

Request:

```json
{
  "query": "How do I build a web application with React and FastAPI?"
}
```

Response:

```json
{
  "plan": "# Execution Plan: Building a Web Application with React and FastAPI\n\n## Step 1: Set up the development environment\n- Install Node.js and npm for React\n- Install Python for FastAPI\n- Set up a code editor (VS Code recommended)\n\n## Step 2: Create the FastAPI backend\n- Create a virtual environment\n- Install FastAPI and Uvicorn\n- Create a basic API structure\n- Implement API endpoints\n\n## Step 3: Create the React frontend\n- Set up a new React project using Create React App\n- Install necessary dependencies\n- Create components and pages\n- Implement API integration\n\n## Step 4: Connect frontend and backend\n- Configure CORS in FastAPI\n- Set up proxy in React\n- Test the connection\n\n## Step 5: Deploy the application\n- Prepare the backend for deployment\n- Prepare the frontend for deployment\n- Deploy to a hosting service"
}
```

### Error Responses

#### 400 Bad Request

Returned when the request is invalid.

```json
{
  "detail": "Invalid request"
}
```

#### 500 Internal Server Error

Returned when an error occurs on the server.

```json
{
  "detail": "An error occurred while processing the request"
}
```

## Rate Limiting

Currently, there is no rate limiting implemented. In a production environment, you would want to add rate limiting to prevent abuse.

## Versioning

The API is versioned using the URL path. The current version is `v1`.

## Future Endpoints

The following endpoints are planned for future releases:

- **GET /plans**: Retrieve a list of previously generated plans
- **GET /plans/{id}**: Retrieve a specific plan by ID
- **PUT /plans/{id}**: Update a specific plan
- **DELETE /plans/{id}**: Delete a specific plan 