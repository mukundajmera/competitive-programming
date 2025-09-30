from typing import List
from langchain.tools import Tool
from .base_agent import BaseAgent


class CodeAgent(BaseAgent):
    """Agent specialized in code generation and analysis."""
    
    def _initialize_tools(self) -> List[Tool]:
        """Initialize code-specific tools."""
        return [
            Tool(
                name="generate_code",
                func=self._generate_code,
                description="Generate code in specified programming language"
            ),
            Tool(
                name="review_code",
                func=self._review_code,
                description="Review code for best practices and potential issues"
            ),
            Tool(
                name="explain_code",
                func=self._explain_code,
                description="Explain what a piece of code does"
            ),
        ]
    
    def get_system_message(self) -> str:
        """Get code agent system message."""
        return """You are an expert software engineer specialized in:
        - Writing clean, efficient, and maintainable code
        - Following best practices and design patterns
        - Code review and optimization
        - Debugging and problem-solving
        - Multiple programming languages and frameworks
        
        Always write production-quality code with proper error handling,
        documentation, and test coverage considerations."""
    
    async def _generate_code(self, specification: str) -> str:
        """Generate code based on specification."""
        return f"Generated code for: {specification}"
    
    async def _review_code(self, code: str) -> str:
        """Review code quality."""
        return "Code review: Follows best practices with minor suggestions for improvement."
    
    async def _explain_code(self, code: str) -> str:
        """Explain code functionality."""
        return f"Explanation of code: [Detailed explanation would be provided]"


class CreativeAgent(BaseAgent):
    """Agent specialized in creative content generation."""
    
    def _initialize_tools(self) -> List[Tool]:
        """Initialize creative tools."""
        return [
            Tool(
                name="generate_ideas",
                func=self._generate_ideas,
                description="Generate creative ideas for campaigns or content"
            ),
            Tool(
                name="write_copy",
                func=self._write_copy,
                description="Write marketing copy or social media content"
            ),
        ]
    
    def get_system_message(self) -> str:
        """Get creative agent system message."""
        return """You are a creative content specialist focused on:
        - Marketing copy and advertising
        - Social media content
        - Brand messaging
        - Engaging headlines and hooks
        - Persuasive writing
        
        Create compelling, original content that resonates with the target audience."""
    
    async def _generate_ideas(self, brief: str) -> str:
        """Generate creative ideas."""
        return f"Creative ideas for: {brief}"
    
    async def _write_copy(self, requirements: str) -> str:
        """Write marketing copy."""
        return f"Copy for: {requirements}"
