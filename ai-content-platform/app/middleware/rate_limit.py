from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from collections import defaultdict
import time


class RateLimitMiddleware(BaseHTTPMiddleware):
    """Rate limiting middleware."""
    
    def __init__(self, app):
        super().__init__(app)
        self.requests = defaultdict(list)
        self.minute_limit = 60
        self.hour_limit = 1000
    
    async def dispatch(self, request: Request, call_next):
        """Process request with rate limiting."""
        client_ip = request.client.host
        current_time = time.time()
        
        # Clean old requests
        self.requests[client_ip] = [
            req_time for req_time in self.requests[client_ip]
            if current_time - req_time < 3600  # Keep last hour
        ]
        
        # Check rate limits
        minute_requests = sum(
            1 for req_time in self.requests[client_ip]
            if current_time - req_time < 60
        )
        
        if minute_requests >= self.minute_limit:
            return JSONResponse(
                status_code=429,
                content={"detail": "Rate limit exceeded"}
            )
        
        # Add current request
        self.requests[client_ip].append(current_time)
        
        response = await call_next(request)
        return response
