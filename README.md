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

4. Create a `.env` file in the backend directory with your Gemini API key:
   ```
   AUTOGEN_GEMINI_API_KEY=your_api_key_here
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