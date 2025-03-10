# AutoGen Planner with Gradio UI

This project integrates AutoGen with Google's Gemini AI model to create a planning system with a Gradio UI. The system allows users to input requests, which are processed by AutoGen agents to generate execution plans using the Gemini AI model.

## Project Structure

The project is structured with a clear separation between frontend and backend components:

- **Backend**: FastAPI server that hosts the AutoGen agents and communicates with the Gemini AI model
- **Frontend**: Gradio application that provides a user interface for interacting with the system

## Features

- User-friendly chat interface for submitting requests
- AI-powered execution plan generation
- Clean display of generated plans
- Separation of concerns between frontend and backend

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/autogen_planner.git
   cd autogen_planner
   ```

2. Set up the backend:
   ```
   cd backend
   pip install -e .
   ```

3. Set up the frontend:
   ```
   cd ../frontend
   pip install -r requirements.txt
   ```

4. Create environment files:
   
   For the backend, create a `.env` file in the `backend` directory:
   ```
   # AutoGen Planner Backend Environment Variables
   
   # Application settings
   AUTOGEN_APP_NAME=AutoGen Planner
   AUTOGEN_API_PREFIX=/api/v1
   AUTOGEN_DEBUG=False
   
   # API keys
   AUTOGEN_GEMINI_API_KEY=your_gemini_api_key_here
   ```
   
   For the frontend, create a `.env` file in the `frontend` directory:
   ```
   # AutoGen Planner Frontend Environment Variables
   
   # API settings
   AUTOGEN_API_URL=http://localhost:8000/api/v1
   
   # UI settings
   AUTOGEN_PORT=7860
   AUTOGEN_SHARE=False
   ```

   Alternatively, you can run the setup script which will create these files for you:
   ```
   .\scripts\setup_dev_env.ps1
   ```

### Running the Application

1. Start the backend server:
   ```
   cd backend
   python -m src.autogen_planner.main
   ```

2. Start the frontend application:
   ```
   cd frontend
   python -m src.gradio_app.app
   ```

3. Open your browser and navigate to `http://localhost:7860` to access the application.

Alternatively, you can use the provided script to run both components:
```
.\scripts\run_local.ps1
```

## Development

### Backend Development

The backend is built with FastAPI and includes:
- AutoGen agents for processing user requests and generating plans
- API endpoints for communication with the frontend
- Integration with the Gemini AI model

### Frontend Development

The frontend is built with Gradio and includes:
- Chat interface for user interaction
- Plan display for showing generated plans
- API client for communication with the backend

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [AutoGen](https://github.com/microsoft/autogen) for the agent framework
- [Gradio](https://gradio.app/) for the UI components
- [Google Gemini](https://ai.google.dev/) for the AI model 