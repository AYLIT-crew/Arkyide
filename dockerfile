# This Dockerfile is for running tests only

# Use a Python base image for the builder stage
FROM python:3.12 AS builder

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install any additional dependencies needed for testing
RUN apt-get update && apt-get install -y nmap

# Copy the application code
COPY . .

# Use the builder stage as the base image for the tester stage
FROM builder AS tester

# Install pytest for running tests
RUN pip install pytest

# Set the command to run when the container starts
CMD ["pytest"]
#CMD ["python", "arkyide.py"]