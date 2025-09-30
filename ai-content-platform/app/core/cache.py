import json
from typing import Any, Optional
import redis.asyncio as redis
from .config import settings


class CacheService:
    """Redis cache service for distributed caching."""
    
    def __init__(self):
        self.redis_client: Optional[redis.Redis] = None
    
    async def connect(self):
        """Connect to Redis."""
        self.redis_client = await redis.from_url(
            settings.REDIS_URL,
            encoding="utf-8",
            decode_responses=True
        )
    
    async def disconnect(self):
        """Disconnect from Redis."""
        if self.redis_client:
            await self.redis_client.close()
    
    async def get(self, key: str) -> Optional[Any]:
        """Get value from cache."""
        if not self.redis_client:
            return None
        
        value = await self.redis_client.get(key)
        if value:
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return value
        return None
    
    async def set(
        self,
        key: str,
        value: Any,
        ttl: Optional[int] = None
    ) -> bool:
        """Set value in cache with optional TTL."""
        if not self.redis_client:
            return False
        
        ttl = ttl or settings.REDIS_CACHE_TTL
        
        if not isinstance(value, str):
            value = json.dumps(value)
        
        return await self.redis_client.setex(key, ttl, value)
    
    async def delete(self, key: str) -> bool:
        """Delete key from cache."""
        if not self.redis_client:
            return False
        
        return await self.redis_client.delete(key) > 0
    
    async def exists(self, key: str) -> bool:
        """Check if key exists in cache."""
        if not self.redis_client:
            return False
        
        return await self.redis_client.exists(key) > 0
    
    async def invalidate_pattern(self, pattern: str) -> int:
        """Invalidate all keys matching pattern."""
        if not self.redis_client:
            return 0
        
        keys = []
        async for key in self.redis_client.scan_iter(match=pattern):
            keys.append(key)
        
        if keys:
            return await self.redis_client.delete(*keys)
        return 0


# Global cache instance
cache_service = CacheService()


async def get_cache() -> CacheService:
    """Dependency for getting cache service."""
    return cache_service
