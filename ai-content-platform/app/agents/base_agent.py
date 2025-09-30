from abc import ABC, abstractmethod
from typing import Dict, Any, List
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from app.core.config import settings


class BaseAgent(ABC):
    """Base class for all AI agents."""
    
    def __init__(self):
        self.llm = ChatOpenAI(
            api_key=settings.OPENAI_API_KEY,
            model=settings.DEFAULT_LLM_MODEL,
            temperature=settings.DEFAULT_TEMPERATURE,
        )
        self.tools = self._initialize_tools()
        self.agent = self._create_agent()
    
    @abstractmethod
    def _initialize_tools(self) -> List[Tool]:
        """Initialize agent-specific tools."""
        pass
    
    @abstractmethod
    def get_system_message(self) -> str:
        """Get agent-specific system message."""
        pass
    
    def _create_agent(self) -> AgentExecutor:
        """Create the agent executor."""
        prompt = ChatPromptTemplate.from_messages([
            ("system", self.get_system_message()),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])
        
        agent = create_openai_functions_agent(self.llm, self.tools, prompt)
        return AgentExecutor(agent=agent, tools=self.tools, verbose=True)
    
    async def execute(
        self,
        task: str,
        context: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """Execute the agent task."""
        context = context or {}
        
        result = await self.agent.ainvoke({
            "input": task,
            **context
        })
        
        return {
            "output": result["output"],
            "steps": result.get("intermediate_steps", []),
        }
