from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
import logging
import time

logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseHTTPMiddleware):
    """Logging middleware for request/response tracking."""
    
    async def dispatch(self, request: Request, call_next):
        """Log requests and responses."""
        start_time = time.time()
        
        # Log request
        logger.info(f"Request: {request.method} {request.url.path}")
        
        response = await call_next(request)
        
        # Calculate duration
        duration = time.time() - start_time
        
        # Log response
        logger.info(
            f"Response: {request.method} {request.url.path} "
            f"status={response.status_code} duration={duration:.3f}s"
        )
        
        # Add custom header
        response.headers["X-Process-Time"] = str(duration)
        
        return response
