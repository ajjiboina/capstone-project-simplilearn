# Imports
from asyncio import Task
import os
import sys
from pathlib import Path
import sqlite3
from crewai import Crew,LLM, Agent, Task
from crewai.tools import  tool


# DB Connection to read the DB data
connection = sqlite3.connect("db/products.db")
cursor = connection.cursor()
cursor.execute("SELECT name, details FROM products")
db_data = cursor.fetchall()
PRODUCTS_DB = {
    name.lower(): {
        "price":price,
        "stock":stock,
        "brand":brand
    }
    for _,name, price, stock, brand in db_data
}

# Creating tools that will fetch data from DB
@tool("product_db_tool")
def product_db_tool(product_name:str)-> str:
    """
    Get Product details from the Product Database

    """
    product_name = product_name.lower()

    if product_name in PRODUCTS_DB:
        return str(PRODUCTS_DB[product_name])
    else:
        return "Product not found"

# Crew AI Specific steps 
def create_crew(config):
    # Config LLM
    llm=LLM(
        model=config.model,
        api_key=os.getenv("OPENAI_API_KEY") if config.provider == "openai" else None,
        temperature=config.temperature
    )
    # Define Agents 
    # Classifier Agent
    classifier_agent = Agent(
        role="Classifier Agent",
        goal="Classify the user query into product or general.",
        backstory="Expert at understanding uder intent.",
        llm=llm,
        verbose=True
        )
    # db Agent
    db_agent = Agent(
        role="Database Agent",
        goal="""
        You must call product_db_tool.
        Never Answer from your trained Knowledge
        If the tool return 'Product Not Found' then 
        Your final answer should be 'Product Not Found' and nothing else.""",
        backstory="Expert at fetching product details from the database.",
        tools=[product_db_tool],
        llm=llm,
        verbose=True
        )
    # research agent
    research_agent = Agent(
        role="Research Agent",
        goal="""
        Research and explain general topics clearly.
        Strictly do not answer product related queries.""",
        backstory="Expert Researcher.",
        llm=llm,
        verbose=True
        )
    # Writer agent
    writer_agent = Agent(
        role="Writer Agent",
        goal="Covert information into structured answer. Keep the answers within 50 words.",
        backstory="Format the responses into clean numbered lists.",
        llm=llm,
        verbose=True
        )
    #Fetch user query from the config
    query = config.user_query
    #define tasks
    classify_task = Task(
        description="Classify the user query into 'product' or 'general' : Query is {query}",
        expected_output="product or general",
        agent=classifier_agent
    )
    db_taks = Task(
        description="""
        Fetch product info for: {query}
        If infor is not presented in the DB then respond - 'Product details not finf in the DB'
        Do not Provide any general information 
        """,
        expected_output="Product details or 'Product details not found in the DB'",
        agent=db_agent
        context = [classify_task]
    )
    research_task = Task(
        description="Research and explain the general topic: {query}",
        expected_output="General topic explanation",
        agent=research_agent,
        context = [classify_task]
    )
    writer_task = Task(
        description="Format previous output into numbered lists",
        expected_output="Final Structured answer in 50 words",
        agent=writer_agent,
        context = [classify_task, db_taks, research_task]
    )
# Create the crew
    crew= Crew(
        agents=[classifier_agent, db_agent, research_agent, writer_agent],
        tasks=[classify_task, db_taks, research_task, writer_task]
    )

    return crew