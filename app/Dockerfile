# Use an official Python runtime as a parent image
FROM --platform=linux/amd64 python:3.8-slim-buster as build

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app.py /app

# Install Flask
RUN pip install flask

# Expose port 5002 for the application
EXPOSE 5002

# Define the environment variable
ENV TOKEN "DefaultTokenValue"

# Run the application
CMD ["python", "app.py"]
