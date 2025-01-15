# Use an updated Python base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies for building Python packages (like gcc, g++, python3-dev, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install dependencies from requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

# Copy the application code into the container
COPY . .

# Install additional tools for linting, formatting, and testing
RUN pip install black pylint pytest

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=flask_app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5001

# Expose the port Flask will run on (default is 5001)
EXPOSE 5001

# Command to run the application with gunicorn
CMD ["gunicorn", "-w", "4", "app.flask_app:app", "-b", "0.0.0.0:5001"]