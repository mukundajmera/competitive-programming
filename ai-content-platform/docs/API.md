# AI Content Platform API Documentation

## Overview

The AI Content Platform provides a comprehensive RESTful API and WebSocket endpoints for AI-powered content generation, management, and collaboration.

## Authentication

All endpoints except registration and login require authentication using JWT tokens.

### Getting Started

1. Register a new user:
```bash
POST /api/v1/auth/register
```

2. Login to get access token:
```bash
POST /api/v1/auth/login
```

3. Use token in Authorization header:
```bash
Authorization: Bearer <your-token>
```

## Endpoints

### Authentication Endpoints

#### Register User
- **URL**: `/api/v1/auth/register`
- **Method**: `POST`
- **Body**:
```json
{
  "email": "user@example.com",
  "username": "johndoe",
  "password": "SecurePass123",
  "full_name": "John Doe"
}
```
- **Response**: User object

#### Login
- **URL**: `/api/v1/auth/login`
- **Method**: `POST`
- **Body**: Form data with username and password
- **Response**:
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer"
}
```

### AI Generation Endpoints

#### Generate Content (Sync)
- **URL**: `/api/v1/ai/generate`
- **Method**: `POST`
- **Body**:
```json
{
  "prompt": "Write a blog post about AI",
  "provider": "openai",
  "model": "gpt-4-turbo-preview",
  "temperature": 0.7,
  "max_tokens": 2000,
  "system_message": "You are a helpful assistant"
}
```
- **Response**:
```json
{
  "content": "Generated content...",
  "provider": "openai",
  "model": "gpt-4-turbo-preview",
  "tokens_used": 500,
  "finish_reason": "stop",
  "metadata": {}
}
```

#### Generate Content (Streaming)
- **URL**: `/api/v1/ai/generate/stream`
- **Method**: `POST`
- **Body**: Same as sync generation
- **Response**: Server-Sent Events (SSE) stream

#### Execute Agent Task
- **URL**: `/api/v1/ai/agent/execute`
- **Method**: `POST`
- **Body**:
```json
{
  "agent_type": "writer",
  "prompt": "Write an engaging introduction",
  "context": {"tone": "professional"},
  "max_iterations": 3
}
```

### Content Management Endpoints

#### Create Content
- **URL**: `/api/v1/content/`
- **Method**: `POST`

#### List Content
- **URL**: `/api/v1/content/`
- **Method**: `GET`
- **Query Params**: `skip`, `limit`

#### Get Content
- **URL**: `/api/v1/content/{content_id}`
- **Method**: `GET`

#### Update Content
- **URL**: `/api/v1/content/{content_id}`
- **Method**: `PUT`

#### Delete Content
- **URL**: `/api/v1/content/{content_id}`
- **Method**: `DELETE`

### WebSocket Endpoints

#### Stream AI Content
- **URL**: `ws://localhost:8000/api/v1/ws/stream/{session_id}?token={token}`
- **Protocol**: WebSocket

#### Real-Time Collaboration
- **URL**: `ws://localhost:8000/api/v1/ws/collaborate/{room_id}?token={token}`
- **Protocol**: WebSocket

## Rate Limiting

- 60 requests per minute per IP
- 1000 requests per hour per IP

## Error Responses

All endpoints return standard HTTP status codes:

- `200 OK`: Success
- `201 Created`: Resource created
- `400 Bad Request`: Invalid input
- `401 Unauthorized`: Authentication required
- `403 Forbidden`: Insufficient permissions
- `404 Not Found`: Resource not found
- `429 Too Many Requests`: Rate limit exceeded
- `500 Internal Server Error`: Server error

Error response format:
```json
{
  "detail": "Error message"
}
```

## Best Practices

1. **Always include authentication token**
2. **Handle rate limits gracefully**
3. **Use streaming for long content generation**
4. **Implement proper error handling**
5. **Cache responses when appropriate**
6. **Use WebSockets for real-time features**

## SDK Examples

### Python
```python
from ai_content_client import AIContentClient

client = AIContentClient(api_key="your-api-key")
response = client.generate(prompt="Write about AI")
```

### JavaScript
```javascript
import { AIContentClient } from 'ai-content-client';

const client = new AIContentClient({ apiKey: 'your-api-key' });
const response = await client.generate({ prompt: 'Write about AI' });
```

## Support

For API support, contact: api-support@example.com
