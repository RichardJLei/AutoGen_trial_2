"""
Main entry point for the AutoGen Planner application.

This module defines the FastAPI application and includes the API routes.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.routes import router
from .config.settings import settings
from .utils.logging import logger

def create_app() -> FastAPI:
    """
    Create the FastAPI application.
    
    Returns:
        The configured FastAPI application.
    """
    # Create the FastAPI app
    app = FastAPI(
        title=settings.app_name,
        description="API for the AutoGen Planner application",
        version="0.1.0",
        debug=settings.debug,
    )
    
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # In production, this should be restricted
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Include the API router
    app.include_router(router, prefix=settings.api_prefix)
    
    # Add startup event
    @app.on_event("startup")
    async def startup_event():
        logger.info(f"Starting {settings.app_name}")
    
    # Add shutdown event
    @app.on_event("shutdown")
    async def shutdown_event():
        logger.info(f"Shutting down {settings.app_name}")
    
    return app

# Create the application instance
app = create_app()

if __name__ == "__main__":
    import uvicorn
    
    # Run the application
    uvicorn.run(
        "autogen_planner.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
    ) 