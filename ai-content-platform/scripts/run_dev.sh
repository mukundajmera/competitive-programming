#!/bin/bash

# Development server script

echo "Starting AI Content Platform development server..."

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Set development environment
export ENVIRONMENT=development
export DEBUG=true
export RELOAD=true

# Run with uvicorn
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
