from typing import AsyncIterator, Optional, Dict, Any
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain.schema import HumanMessage, SystemMessage
from langchain.callbacks.base import AsyncCallbackHandler
from app.core.config import settings
from app.schemas.ai_request import AIRequest, AIResponse, StreamChunk, AIProvider


class StreamingCallbackHandler(AsyncCallbackHandler):
    """Callback handler for streaming responses."""
    
    def __init__(self):
        self.tokens = []
    
    async def on_llm_new_token(self, token: str, **kwargs) -> None:
        """Handle new token from LLM."""
        self.tokens.append(token)


class AIService:
    """Service for AI model interactions."""
    
    def __init__(self):
        self.models: Dict[str, Any] = {}
        self._initialize_models()
    
    def _initialize_models(self):
        """Initialize AI models based on available API keys."""
        if settings.OPENAI_API_KEY:
            self.models["openai"] = ChatOpenAI(
                api_key=settings.OPENAI_API_KEY,
                model=settings.DEFAULT_LLM_MODEL,
                temperature=settings.DEFAULT_TEMPERATURE,
                streaming=True,
            )
        
        if settings.ANTHROPIC_API_KEY:
            self.models["anthropic"] = ChatAnthropic(
                api_key=settings.ANTHROPIC_API_KEY,
                model="claude-3-opus-20240229",
                temperature=settings.DEFAULT_TEMPERATURE,
                streaming=True,
            )
    
    def get_model(self, provider: Optional[str] = None):
        """Get AI model by provider."""
        provider = provider or settings.DEFAULT_LLM_PROVIDER
        if provider not in self.models:
            raise ValueError(f"Provider {provider} not configured")
        return self.models[provider]
    
    async def generate(self, request: AIRequest) -> AIResponse:
        """Generate content using AI model."""
        model = self.get_model(request.provider)
        
        # Prepare messages
        messages = []
        if request.system_message:
            messages.append(SystemMessage(content=request.system_message))
        messages.append(HumanMessage(content=request.prompt))
        
        # Generate response
        response = await model.ainvoke(messages)
        
        return AIResponse(
            content=response.content,
            provider=request.provider or settings.DEFAULT_LLM_PROVIDER,
            model=request.model or settings.DEFAULT_LLM_MODEL,
            tokens_used=len(response.content.split()),  # Approximate
            finish_reason="stop",
            metadata={}
        )
    
    async def generate_stream(
        self,
        request: AIRequest
    ) -> AsyncIterator[StreamChunk]:
        """Generate content with streaming."""
        model = self.get_model(request.provider)
        
        # Prepare messages
        messages = []
        if request.system_message:
            messages.append(SystemMessage(content=request.system_message))
        messages.append(HumanMessage(content=request.prompt))
        
        # Stream response
        async for chunk in model.astream(messages):
            if hasattr(chunk, 'content') and chunk.content:
                yield StreamChunk(
                    delta=chunk.content,
                    finish_reason=None
                )
        
        # Send finish chunk
        yield StreamChunk(
            delta="",
            finish_reason="stop"
        )


# Global AI service instance
ai_service = AIService()


def get_ai_service() -> AIService:
    """Dependency for getting AI service."""
    return ai_service
