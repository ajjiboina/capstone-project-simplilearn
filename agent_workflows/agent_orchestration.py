#Imports 
from langsmith import traceable  # type: ignore
from app_config.config import AgenticAIConfig
from agent_workflows.crew_setup import create_crew
from observability.logger import logger

#LangSmith Specific
@traceable(name="Agentic AI Capstone Project Demo",run_type="chain")
def run(config:AgenticAIConfig):
    """
    This is the entry point for the Agentic AI Workflow 

    """
    logger.info("Crew setup started.")
    
    # call CrewAO Specific Steps
    logger.info("Creating crew...")
    crew = create_crew(config)
    logger.info("Crew created successfully.")
    result = crew.kickoff(
        inputs={
            "query": config.user_query,
        }
    )

    config.response = str(result)
    return config
