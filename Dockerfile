# Use official Python image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install curl for health checks
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copy dependency file and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the port your FastAPI app runs on
EXPOSE 5000

# Run the application with proper host binding
# Option 1: If using uvicorn (FastAPI)
#CMD ["python", "app/main.py"]

# Option 2: If using Flask or direct Python
#CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]

# Option 3: If you have a custom run command in main.py
# Make sure main.py binds to 0.0.0.0:5000, then:
CMD ["python", "main.py"]