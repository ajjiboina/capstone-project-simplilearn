#1 - Imports
from dataclasses import dataclass, field
from typing import List

#2 - Create a "dataclass" for all configs that can be anywhere in this project. T

@dataclass
class AgenticAIConfig:
    # UI Selections from users
    provider:str = "OpenAI"
    model:str = "gpt-4o"
    temparature:float = 0.7
    max_tokens:int = 1000

    # User Input 
    user_query:str = ""
    
    #Agent Settings (Crew AI Specific)
    agent_name:str = "CrewAI"
    tools:List[str] = field(default_factory=list)

    # Run time
    response:str = ""
    chat_history:List[dict] = field(default_factory=list)
    