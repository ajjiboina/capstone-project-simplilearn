# Imports
from dotenv import load_dotenv
import streamlit as st

from app_config.config import AgenticAIConfig

# Loading Environment Variables
load_dotenv() # it will load all env variables

# Set Page Config 
st.set_page_config(
    page_title="Sree SL Capstone Project - Chatbot", #Show it in the tab
    page_icon=":robot_face:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize config 
if "config" not in st.session_state:
    st.session_state.config = AgenticAIConfig()
config = st.session_state.config

#Initialize Streamlit - Converation History
if "Chat_history" not in st.session_state:
    st.session_state.Chat_history = []

# Setting dic for Available models

# Creating Side bar (LLM Config)

# Setting Page title

# Creating user input section 

# Creating Reponse section 

# Creating button for users to clear all the chats from UI