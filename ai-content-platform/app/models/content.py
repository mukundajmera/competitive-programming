from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum as SQLEnum, JSON
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.schemas.content import ContentType, ContentStatus
import enum


class Content(Base):
    """Content model."""
    
    __tablename__ = "contents"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False)
    body = Column(Text, nullable=False, default="")
    content_type = Column(SQLEnum(ContentType), nullable=False)
    status = Column(SQLEnum(ContentStatus), default=ContentStatus.DRAFT)
    description = Column(Text, nullable=True)
    tags = Column(JSON, default=list)
    metadata = Column(JSON, default=dict)
    
    # Foreign keys
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=True)
    
    # Version tracking
    current_version = Column(Integer, default=1)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    owner = relationship("User", back_populates="contents")
    project = relationship("Project", back_populates="contents")
    versions = relationship("ContentVersion", back_populates="content", cascade="all, delete-orphan")


class ContentVersion(Base):
    """Content version model for version control."""
    
    __tablename__ = "content_versions"
    
    id = Column(Integer, primary_key=True, index=True)
    content_id = Column(Integer, ForeignKey("contents.id"), nullable=False)
    version_number = Column(Integer, nullable=False)
    body = Column(Text, nullable=False)
    commit_message = Column(String(500), nullable=True)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    content = relationship("Content", back_populates="versions")
