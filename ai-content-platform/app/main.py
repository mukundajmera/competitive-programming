from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from prometheus_fastapi_instrumentator import Instrumentator

from app.core.config import settings
from app.core.database import init_db, close_db
from app.core.cache import cache_service
from app.api.endpoints import (
    auth,
    users,
    content,
    projects,
    ai,
    websocket_router,
)
from app.middleware.rate_limit import RateLimitMiddleware
from app.middleware.logging import LoggingMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events."""
    # Startup
    await init_db()
    await cache_service.connect()
    yield
    # Shutdown
    await cache_service.disconnect()
    await close_db()


# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc",
    lifespan=lifespan,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom middleware
app.add_middleware(RateLimitMiddleware)
app.add_middleware(LoggingMiddleware)

# Prometheus metrics
if settings.PROMETHEUS_ENABLED:
    Instrumentator().instrument(app).expose(app)

# Include routers
app.include_router(
    auth.router,
    prefix=f"{settings.API_V1_STR}/auth",
    tags=["authentication"]
)
app.include_router(
    users.router,
    prefix=f"{settings.API_V1_STR}/users",
    tags=["users"]
)
app.include_router(
    content.router,
    prefix=f"{settings.API_V1_STR}/content",
    tags=["content"]
)
app.include_router(
    projects.router,
    prefix=f"{settings.API_V1_STR}/projects",
    tags=["projects"]
)
app.include_router(
    ai.router,
    prefix=f"{settings.API_V1_STR}/ai",
    tags=["ai"]
)
app.include_router(
    websocket_router.router,
    prefix=f"{settings.API_V1_STR}/ws",
    tags=["websocket"]
)


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "operational"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "version": settings.APP_VERSION
    }


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler."""
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error", "error": str(exc)}
    )
