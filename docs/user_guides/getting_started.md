# AutoGen Planner - Getting Started

This guide will help you get started with the AutoGen Planner application.

## Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.8 or higher
- Git (optional, for cloning the repository)

You will also need a Google Gemini API key. You can get one by following these steps:

1. Go to the [Google AI Studio](https://ai.google.dev/)
2. Sign in with your Google account
3. Navigate to the API keys section
4. Create a new API key

## Installation

### Option 1: Clone the Repository

If you have Git installed, you can clone the repository:

```bash
git clone https://github.com/yourusername/autogen_planner.git
cd autogen_planner
```

### Option 2: Download the Source Code

Alternatively, you can download the source code as a ZIP file and extract it.

### Setting Up the Environment

1. Create a `.env` file in the root directory of the project:

```
AUTOGEN_GEMINI_API_KEY=your_gemini_api_key_here
```

Replace `your_gemini_api_key_here` with your actual Gemini API key.

2. Run the setup script:

```bash
# On Windows
.\scripts\setup_dev_env.ps1

# On Linux/Mac
./scripts/setup_dev_env.sh
```

This script will create virtual environments for the backend and frontend, and install the required dependencies.

## Running the Application

1. Run the application using the provided script:

```bash
# On Windows
.\scripts\run_local.ps1

# On Linux/Mac
./scripts/run_local.sh
```

2. Open your browser and navigate to:
   - Frontend: http://localhost:7860
   - Backend API: http://localhost:8000/docs (Swagger UI)

## Using the Application

1. Enter your request in the text box on the left side of the interface.
2. Click the "Submit" button or press Enter.
3. Wait for the system to generate an execution plan.
4. The plan will be displayed on the right side of the interface.

### Example Requests

Here are some example requests you can try:

- "How do I build a web application with React and FastAPI?"
- "Create a plan for setting up a machine learning pipeline for image classification."
- "What steps should I follow to deploy a containerized application to Kubernetes?"

## Troubleshooting

### Backend Not Starting

If the backend fails to start, check the following:

1. Make sure you have set the Gemini API key correctly in the `.env` file.
2. Check if the required ports (8000 for the backend, 7860 for the frontend) are available.

### Frontend Not Connecting to Backend

If the frontend cannot connect to the backend, check the following:

1. Make sure the backend is running.
2. Check if the `AUTOGEN_API_URL` environment variable is set correctly.

### Other Issues

If you encounter any other issues, please check the logs for error messages. If you cannot resolve the issue, please open an issue on the GitHub repository.

## Next Steps

Now that you have the AutoGen Planner up and running, you can:

1. Explore the API documentation at http://localhost:8000/docs
2. Customize the application to suit your needs
3. Contribute to the project by submitting pull requests

For more information, check out the other documentation files in the `docs` directory. 