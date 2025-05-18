# Use official Python image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency file and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the port your FastAPI app runs on
EXPOSE 5000

# Run the application
CMD ["python", "main.py"]
