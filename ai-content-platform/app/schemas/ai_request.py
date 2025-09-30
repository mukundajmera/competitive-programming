from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field
from enum import Enum


class AIProvider(str, Enum):
    """AI provider enumeration."""
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GOOGLE = "google"
    COHERE = "cohere"


class AIModel(str, Enum):
    """AI model enumeration."""
    GPT4_TURBO = "gpt-4-turbo-preview"
    GPT4 = "gpt-4"
    GPT35_TURBO = "gpt-3.5-turbo"
    CLAUDE_3_OPUS = "claude-3-opus-20240229"
    CLAUDE_3_SONNET = "claude-3-sonnet-20240229"
    GEMINI_PRO = "gemini-pro"


class AIRequest(BaseModel):
    """Schema for AI generation request."""
    prompt: str = Field(..., min_length=1)
    provider: Optional[AIProvider] = None
    model: Optional[AIModel] = None
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: int = Field(default=2000, ge=1, le=8000)
    stream: bool = False
    system_message: Optional[str] = None
    context: Optional[Dict[str, Any]] = None
    tools: Optional[List[str]] = None


class AIResponse(BaseModel):
    """Schema for AI generation response."""
    content: str
    provider: str
    model: str
    tokens_used: int
    finish_reason: str
    metadata: Dict[str, Any] = Field(default_factory=dict)


class StreamChunk(BaseModel):
    """Schema for streaming chunk."""
    delta: str
    finish_reason: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class AgentType(str, Enum):
    """Agent type enumeration."""
    WRITER = "writer"
    CODE = "code"
    CREATIVE = "creative"
    ANALYST = "analyst"
    REVIEWER = "reviewer"


class AgentTask(BaseModel):
    """Schema for agent task."""
    agent_type: AgentType
    prompt: str
    context: Optional[Dict[str, Any]] = None
    tools: Optional[List[str]] = None
    max_iterations: int = Field(default=3, ge=1, le=10)


class AgentResponse(BaseModel):
    """Schema for agent response."""
    agent_type: str
    result: str
    steps: List[Dict[str, Any]]
    tokens_used: int
    execution_time: float
