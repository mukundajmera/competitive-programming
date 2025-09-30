from typing import List
from langchain.tools import Tool
from .base_agent import BaseAgent


class AnalystAgent(BaseAgent):
    """Agent specialized in data analysis and reporting."""
    
    def _initialize_tools(self) -> List[Tool]:
        """Initialize analyst tools."""
        return [
            Tool(
                name="analyze_data",
                func=self._analyze_data,
                description="Analyze data and extract insights"
            ),
            Tool(
                name="create_report",
                func=self._create_report,
                description="Create comprehensive analytical reports"
            ),
        ]
    
    def get_system_message(self) -> str:
        """Get analyst agent system message."""
        return """You are a data analyst expert specializing in:
        - Data interpretation and insights
        - Statistical analysis
        - Report generation
        - Trend identification
        - Data visualization recommendations
        
        Provide clear, actionable insights from complex data."""
    
    async def _analyze_data(self, data: str) -> str:
        """Analyze data."""
        return f"Analysis of data: [insights would be provided]"
    
    async def _create_report(self, findings: str) -> str:
        """Create analytical report."""
        return f"Report based on: {findings}"
