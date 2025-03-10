"""
Setup script for the AutoGen Planner backend package.
"""

from setuptools import setup, find_packages

setup(
    name="autogen_planner",
    version="0.1.0",
    description="AutoGen Planner with Gradio UI - Backend",
    author="AutoGen Team",
    author_email="info@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "fastapi>=0.104.1",
        "uvicorn>=0.24.0",
        "pydantic>=2.4.2",
        "python-dotenv>=1.0.0",
        "autogen>=0.2.0",
        "google-generativeai>=0.3.1",
        "requests>=2.31.0",
    ],
    python_requires=">=3.8",
) 