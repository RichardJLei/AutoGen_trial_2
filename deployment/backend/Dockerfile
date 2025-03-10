FROM python:3.10-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Install the package
RUN pip install -e .

# Expose the port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "src.autogen_planner.main:app", "--host", "0.0.0.0", "--port", "8000"] 