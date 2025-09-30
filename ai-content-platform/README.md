# AI Content Generation Platform

A cutting-edge, production-grade AI content generation and streaming platform built with FastAPI, LangChain, and modern AI frameworks.

## Features

### Core Capabilities
- **Multi-Modal AI Integration**: Support for OpenAI GPT-4, Anthropic Claude, Google Gemini, and Cohere
- **Real-Time Streaming**: WebSocket and SSE support for live AI content generation
- **Specialized AI Agents**: Writer, Code, Creative, Analyst, and Reviewer agents
- **Content Version Control**: Git-like versioning system for all content
- **Collaborative Editing**: Real-time multi-user content collaboration
- **Advanced Caching**: Redis-based distributed caching layer
- **Comprehensive Monitoring**: Prometheus metrics and Grafana dashboards

### Architecture Highlights
- **Async-First Design**: Full async/await support with asyncpg and aioredis
- **Dependency Injection**: Hierarchical dependencies for clean code organization
- **Modular Structure**: Separate routers for different domains
- **Security**: JWT authentication, API keys, rate limiting, and CORS
- **Production-Ready**: Docker support, health checks, and monitoring

## Quick Start

### Prerequisites
- Python 3.11+
- PostgreSQL 16+
- Redis 7+
- Docker and Docker Compose (optional)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ai-content-platform
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration and API keys
```

5. Initialize database:
```bash
# Create database
createdb ai_content_platform

# Run migrations (if using Alembic)
alembic upgrade head
```

6. Run the application:
```bash
uvicorn app.main:app --reload
```

### Docker Deployment

1. Start all services:
```bash
docker-compose up -d
```

2. View logs:
```bash
docker-compose logs -f api
```

3. Stop services:
```bash
docker-compose down
```

## API Documentation

Once the application is running, access the interactive API documentation:
- **Swagger UI**: http://localhost:8000/api/v1/docs
- **ReDoc**: http://localhost:8000/api/v1/redoc

## API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login and get tokens
- `POST /api/v1/auth/refresh` - Refresh access token

### Users
- `GET /api/v1/users/me` - Get current user info
- `PUT /api/v1/users/me` - Update current user
- `GET /api/v1/users/{user_id}` - Get user by ID

### Content
- `POST /api/v1/content/` - Create content
- `GET /api/v1/content/` - List content
- `GET /api/v1/content/{id}` - Get content with versions
- `PUT /api/v1/content/{id}` - Update content
- `DELETE /api/v1/content/{id}` - Delete content

### Projects
- `POST /api/v1/projects/` - Create project
- `GET /api/v1/projects/` - List projects
- `GET /api/v1/projects/{id}` - Get project
- `PUT /api/v1/projects/{id}` - Update project
- `DELETE /api/v1/projects/{id}` - Delete project

### AI Generation
- `POST /api/v1/ai/generate` - Generate content (synchronous)
- `POST /api/v1/ai/generate/stream` - Generate content (streaming)
- `POST /api/v1/ai/agent/execute` - Execute AI agent task
- `GET /api/v1/ai/models` - List available models
- `GET /api/v1/ai/agents` - List available agents

### WebSocket
- `WS /api/v1/ws/stream/{session_id}` - Stream AI responses
- `WS /api/v1/ws/collaborate/{room_id}` - Real-time collaboration

## Usage Examples

### Register and Login
```python
import requests

# Register
response = requests.post(
    "http://localhost:8000/api/v1/auth/register",
    json={
        "email": "user@example.com",
        "username": "user",
        "password": "SecurePass123",
        "full_name": "John Doe"
    }
)

# Login
response = requests.post(
    "http://localhost:8000/api/v1/auth/login",
    data={
        "username": "user@example.com",
        "password": "SecurePass123"
    }
)
token = response.json()["access_token"]
```

### Generate Content
```python
import requests

headers = {"Authorization": f"Bearer {token}"}

# Synchronous generation
response = requests.post(
    "http://localhost:8000/api/v1/ai/generate",
    headers=headers,
    json={
        "prompt": "Write a blog post about AI",
        "provider": "openai",
        "model": "gpt-4-turbo-preview",
        "temperature": 0.7,
        "max_tokens": 2000
    }
)

# Streaming generation
import sseclient

response = requests.post(
    "http://localhost:8000/api/v1/ai/generate/stream",
    headers=headers,
    json={
        "prompt": "Write a blog post about AI",
        "stream": True
    },
    stream=True
)

client = sseclient.SSEClient(response)
for event in client.events():
    print(event.data)
```

### Use AI Agents
```python
response = requests.post(
    "http://localhost:8000/api/v1/ai/agent/execute",
    headers=headers,
    json={
        "agent_type": "writer",
        "prompt": "Write an engaging introduction for a tech blog",
        "context": {"tone": "professional", "length": "medium"}
    }
)
```

### WebSocket Streaming
```python
import asyncio
import websockets
import json

async def stream_ai_content():
    uri = f"ws://localhost:8000/api/v1/ws/stream/session123?token={token}"
    
    async with websockets.connect(uri) as websocket:
        # Send request
        await websocket.send(json.dumps({
            "prompt": "Generate content",
            "stream": True
        }))
        
        # Receive streaming responses
        async for message in websocket:
            data = json.loads(message)
            print(data)

asyncio.run(stream_ai_content())
```

## Configuration

Key configuration options in `.env`:

```env
# Application
APP_NAME=AI Content Platform
DEBUG=false

# Database
DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/db

# Redis
REDIS_URL=redis://localhost:6379/0

# AI Providers
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_API_KEY=...

# Security
SECRET_KEY=your-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Rate Limiting
RATE_LIMIT_PER_MINUTE=60
RATE_LIMIT_PER_HOUR=1000
```

## Monitoring

### Prometheus Metrics
Access Prometheus at: http://localhost:9090

### Grafana Dashboards
Access Grafana at: http://localhost:3000 (admin/admin)

### Celery Flower
Monitor background tasks at: http://localhost:5555

## Testing

Run tests:
```bash
pytest
pytest --cov=app tests/
```

## Production Deployment

### Environment Setup
1. Set strong SECRET_KEY
2. Configure production database
3. Set up Redis cluster
4. Configure API keys securely
5. Enable HTTPS/TLS
6. Set up monitoring and logging

### Kubernetes Deployment
```bash
kubectl apply -f k8s/
```

### Performance Optimization
- Enable Redis caching
- Use connection pooling
- Configure worker processes
- Set up CDN for static content
- Enable response compression

## Security

- JWT token-based authentication
- API key management
- Rate limiting per IP and user
- CORS configuration
- Input validation with Pydantic
- SQL injection prevention
- XSS protection

## Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## License

MIT License - see LICENSE file for details

## Support

For issues and questions:
- GitHub Issues: <repository-url>/issues
- Documentation: <docs-url>
- Email: support@example.com
