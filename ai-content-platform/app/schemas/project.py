from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class ProjectBase(BaseModel):
    """Base project schema."""
    name: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    settings: Dict[str, Any] = Field(default_factory=dict)
    is_active: bool = True


class ProjectCreate(ProjectBase):
    """Schema for creating a project."""
    pass


class ProjectUpdate(BaseModel):
    """Schema for updating a project."""
    name: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    settings: Optional[Dict[str, Any]] = None
    is_active: Optional[bool] = None


class Project(ProjectBase):
    """Schema for project response."""
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class ProjectWithContent(Project):
    """Schema for project with content."""
    content_count: int = 0
