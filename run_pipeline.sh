#!/bin/bash

# Build the Docker image
echo "Building Docker image..."
docker build -t network_analysis_app .

# Run the Docker container
echo "Running Docker container..."
docker run network_analysis_app
