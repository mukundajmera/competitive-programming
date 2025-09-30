from typing import List
from langchain.tools import Tool
from .base_agent import BaseAgent


class CreativeAgent(BaseAgent):
    """Agent specialized in creative content and marketing."""
    
    def _initialize_tools(self) -> List[Tool]:
        """Initialize creative tools."""
        return [
            Tool(
                name="brainstorm_ideas",
                func=self._brainstorm_ideas,
                description="Brainstorm creative ideas for campaigns"
            ),
            Tool(
                name="write_social_post",
                func=self._write_social_post,
                description="Write engaging social media posts"
            ),
        ]
    
    def get_system_message(self) -> str:
        """Get creative agent system message."""
        return """You are a creative marketing specialist with expertise in:
        - Compelling copywriting
        - Social media engagement
        - Brand voice development
        - Viral content creation
        - Emotional storytelling
        
        Create content that captures attention and drives engagement."""
    
    async def _brainstorm_ideas(self, topic: str) -> str:
        """Brainstorm creative ideas."""
        return f"Creative ideas for {topic}"
    
    async def _write_social_post(self, platform: str) -> str:
        """Write social media post."""
        return f"Social post for {platform}"
