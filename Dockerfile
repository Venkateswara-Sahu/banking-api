# Dockerfile for Flask Banking API

FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "main.py"]