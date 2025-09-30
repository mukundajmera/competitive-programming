from datetime import datetime
from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field
from enum import Enum


class ContentType(str, Enum):
    """Content type enumeration."""
    TEXT = "text"
    CODE = "code"
    IMAGE = "image"
    BLOG = "blog"
    ARTICLE = "article"
    SOCIAL = "social"
    MARKETING = "marketing"
    TECHNICAL = "technical"


class ContentStatus(str, Enum):
    """Content status enumeration."""
    DRAFT = "draft"
    GENERATING = "generating"
    COMPLETED = "completed"
    PUBLISHED = "published"
    ARCHIVED = "archived"


class ContentBase(BaseModel):
    """Base content schema."""
    title: str = Field(..., min_length=1, max_length=500)
    content_type: ContentType
    description: Optional[str] = None
    tags: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class ContentCreate(ContentBase):
    """Schema for creating content."""
    project_id: Optional[int] = None
    parent_version_id: Optional[int] = None


class ContentUpdate(BaseModel):
    """Schema for updating content."""
    title: Optional[str] = Field(None, min_length=1, max_length=500)
    body: Optional[str] = None
    status: Optional[ContentStatus] = None
    tags: Optional[List[str]] = None
    metadata: Optional[Dict[str, Any]] = None


class ContentVersion(BaseModel):
    """Schema for content version."""
    id: int
    content_id: int
    version_number: int
    body: str
    created_at: datetime
    created_by: int
    commit_message: Optional[str] = None
    
    class Config:
        from_attributes = True


class Content(ContentBase):
    """Schema for content response."""
    id: int
    body: str
    status: ContentStatus
    project_id: Optional[int]
    owner_id: int
    current_version: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class ContentWithVersions(Content):
    """Schema for content with version history."""
    versions: List[ContentVersion] = []
