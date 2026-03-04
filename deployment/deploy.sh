#!/bin/bash

echo "Building Docker container..."

docker-compose -f deployment/docker-compose.yml build

echo "Starting API service..."

docker-compose -f deployment/docker-compose.yml up