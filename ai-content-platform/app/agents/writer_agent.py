from typing import List
from langchain.tools import Tool
from .base_agent import BaseAgent


class WriterAgent(BaseAgent):
    """Agent specialized in writing blog posts, articles, and documentation."""
    
    def _initialize_tools(self) -> List[Tool]:
        """Initialize writer-specific tools."""
        return [
            Tool(
                name="research_topic",
                func=self._research_topic,
                description="Research a topic to gather information for writing"
            ),
            Tool(
                name="generate_outline",
                func=self._generate_outline,
                description="Generate an outline for the content"
            ),
            Tool(
                name="check_grammar",
                func=self._check_grammar,
                description="Check grammar and spelling in the text"
            ),
        ]
    
    def get_system_message(self) -> str:
        """Get writer agent system message."""
        return """You are an expert content writer specialized in creating engaging, 
        well-structured blog posts, articles, and documentation. You excel at:
        - Creating compelling narratives
        - Organizing information logically
        - Using appropriate tone and style
        - Incorporating SEO best practices
        - Ensuring clarity and readability
        
        Always produce high-quality, original content that meets the user's requirements."""
    
    async def _research_topic(self, topic: str) -> str:
        """Research a topic (placeholder for actual implementation)."""
        return f"Research findings for {topic}: [Information would be gathered from web search or knowledge base]"
    
    async def _generate_outline(self, title: str) -> str:
        """Generate content outline."""
        return f"""Outline for '{title}':
        1. Introduction
        2. Main Points
        3. Supporting Details
        4. Conclusion
        """
    
    async def _check_grammar(self, text: str) -> str:
        """Check grammar (placeholder)."""
        return "Grammar check passed. No major issues found."
