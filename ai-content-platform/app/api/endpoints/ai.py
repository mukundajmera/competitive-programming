from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
from typing import AsyncIterator
import json

from app.api.dependencies import get_current_user
from app.models.user import User
from app.schemas.ai_request import AIRequest, AIResponse, AgentTask, AgentResponse
from app.services.ai_service import get_ai_service, AIService
from app.agents import WriterAgent, CodeAgent, CreativeAgent, AnalystAgent, ReviewerAgent

router = APIRouter()


@router.post("/generate", response_model=AIResponse)
async def generate_content(
    request: AIRequest,
    current_user: User = Depends(get_current_user),
    ai_service: AIService = Depends(get_ai_service)
):
    """Generate content using AI models."""
    try:
        response = await ai_service.generate(request)
        return response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"AI generation failed: {str(e)}"
        )


@router.post("/generate/stream")
async def generate_content_stream(
    request: AIRequest,
    current_user: User = Depends(get_current_user),
    ai_service: AIService = Depends(get_ai_service)
):
    """Generate content with streaming response."""
    
    async def event_generator() -> AsyncIterator[str]:
        try:
            async for chunk in ai_service.generate_stream(request):
                yield f"data: {chunk.json()}\n\n"
        except Exception as e:
            error_chunk = {"error": str(e)}
            yield f"data: {json.dumps(error_chunk)}\n\n"
    
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )


@router.post("/agent/execute", response_model=AgentResponse)
async def execute_agent_task(
    task: AgentTask,
    current_user: User = Depends(get_current_user)
):
    """Execute a task using specialized AI agent."""
    import time
    
    # Select agent based on type
    agent_map = {
        "writer": WriterAgent,
        "code": CodeAgent,
        "creative": CreativeAgent,
        "analyst": AnalystAgent,
        "reviewer": ReviewerAgent,
    }
    
    agent_class = agent_map.get(task.agent_type)
    if not agent_class:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid agent type: {task.agent_type}"
        )
    
    try:
        start_time = time.time()
        agent = agent_class()
        result = await agent.execute(task.prompt, task.context)
        execution_time = time.time() - start_time
        
        return AgentResponse(
            agent_type=task.agent_type,
            result=result["output"],
            steps=result.get("steps", []),
            tokens_used=len(result["output"].split()),  # Approximate
            execution_time=execution_time
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Agent execution failed: {str(e)}"
        )


@router.get("/models")
async def list_available_models(
    current_user: User = Depends(get_current_user)
):
    """List available AI models."""
    return {
        "providers": ["openai", "anthropic", "google"],
        "models": {
            "openai": ["gpt-4-turbo-preview", "gpt-4", "gpt-3.5-turbo"],
            "anthropic": ["claude-3-opus-20240229", "claude-3-sonnet-20240229"],
            "google": ["gemini-pro"]
        }
    }


@router.get("/agents")
async def list_available_agents(
    current_user: User = Depends(get_current_user)
):
    """List available AI agents."""
    return {
        "agents": [
            {
                "type": "writer",
                "name": "Writer Agent",
                "description": "Specialized in blog posts, articles, and documentation"
            },
            {
                "type": "code",
                "name": "Code Agent",
                "description": "Code generation, review, and analysis"
            },
            {
                "type": "creative",
                "name": "Creative Agent",
                "description": "Marketing copy and social media content"
            },
            {
                "type": "analyst",
                "name": "Analyst Agent",
                "description": "Data analysis and reporting"
            },
            {
                "type": "reviewer",
                "name": "Reviewer Agent",
                "description": "Content review and quality assurance"
            }
        ]
    }
