#!/bin/bash

# Database initialization script

echo "Initializing database..."

# Create database if not exists
createdb ai_content_platform 2>/dev/null || echo "Database already exists"

# Run migrations
if [ -d "alembic" ]; then
    echo "Running migrations..."
    alembic upgrade head
else
    echo "Creating initial migration..."
    alembic revision --autogenerate -m "Initial migration"
    alembic upgrade head
fi

echo "Database initialized successfully!"
