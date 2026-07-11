#Imports 
from langsmith import tracable
from app_config.config import AgenticAIConfig
from agent_workflows.crew_setup import create_crew

#LangSmith Specific
@tracable(name="Agentic AI Capstone Project Demo",run_type="chain")
def run(config:AgenticAIConfig):
    """
    This is the entry point for the Agentic AI Workflow 

    """

    # call CrewAO Specific Steps

    crew = create_crew(config)
    result = crew.kickoff(
        inputs={
            "query": config.user_query,
        }
    )

    config.response = str(result)
    return config
