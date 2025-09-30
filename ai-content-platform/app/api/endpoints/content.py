from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List

from app.core.database import get_db
from app.api.dependencies import get_current_user
from app.models.user import User
from app.models.content import Content, ContentVersion
from app.schemas.content import (
    Content as ContentSchema,
    ContentCreate,
    ContentUpdate,
    ContentWithVersions,
    ContentStatus
)

router = APIRouter()


@router.post("/", response_model=ContentSchema, status_code=status.HTTP_201_CREATED)
async def create_content(
    content_in: ContentCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Create new content."""
    content = Content(
        **content_in.dict(),
        owner_id=current_user.id,
        body="",
        status=ContentStatus.DRAFT,
    )
    db.add(content)
    await db.commit()
    await db.refresh(content)
    return content


@router.get("/", response_model=List[ContentSchema])
async def list_content(
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """List user's content."""
    result = await db.execute(
        select(Content)
        .where(Content.owner_id == current_user.id)
        .offset(skip)
        .limit(limit)
    )
    return result.scalars().all()


@router.get("/{content_id}", response_model=ContentWithVersions)
async def get_content(
    content_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get content by ID with versions."""
    result = await db.execute(
        select(Content).where(
            Content.id == content_id,
            Content.owner_id == current_user.id
        )
    )
    content = result.scalar_one_or_none()
    
    if not content:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Content not found"
        )
    
    # Load versions
    versions_result = await db.execute(
        select(ContentVersion)
        .where(ContentVersion.content_id == content_id)
        .order_by(ContentVersion.version_number.desc())
    )
    content.versions = versions_result.scalars().all()
    
    return content


@router.put("/{content_id}", response_model=ContentSchema)
async def update_content(
    content_id: int,
    content_update: ContentUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Update content."""
    result = await db.execute(
        select(Content).where(
            Content.id == content_id,
            Content.owner_id == current_user.id
        )
    )
    content = result.scalar_one_or_none()
    
    if not content:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Content not found"
        )
    
    # Create version if body changed
    if content_update.body and content_update.body != content.body:
        version = ContentVersion(
            content_id=content.id,
            version_number=content.current_version + 1,
            body=content_update.body,
            created_by=current_user.id,
        )
        db.add(version)
        content.current_version += 1
    
    # Update content
    for field, value in content_update.dict(exclude_unset=True).items():
        setattr(content, field, value)
    
    await db.commit()
    await db.refresh(content)
    return content


@router.delete("/{content_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_content(
    content_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Delete content."""
    result = await db.execute(
        select(Content).where(
            Content.id == content_id,
            Content.owner_id == current_user.id
        )
    )
    content = result.scalar_one_or_none()
    
    if not content:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Content not found"
        )
    
    await db.delete(content)
    await db.commit()
