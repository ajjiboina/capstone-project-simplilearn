# Imports
from dotenv import load_dotenv
from agent_workflows.agent_orchestration import run
import streamlit as st

from app_config.config import AgenticAIConfig
from observability.logger import logger

logger.info("Agentic AI Application is starting...")


# Loading Environment Variables
load_dotenv() # it will load all env variables

# Set Page Config 
logger.info("Setting Streamlit page configuration...")
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
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Setting dic for Available models
MODEL_REGISTRY= {
    "openAI": ["gpt-3.5-turbo", "gpt-4"],
    "ollama": ["llama2", "llama3.2","mistral","phi3","gemma"]

}

# Creating Side bar (LLM Config)
with st.sidebar:
    st.title("LLM Configuration")
    config.provider = st.selectbox(" LLM Provider", options=list(MODEL_REGISTRY.keys()), index=0)

    # Dynamic Model Selection Logic
    available_models = MODEL_REGISTRY.get(config.provider, [])
    config.model = st.selectbox("Model", options=available_models, index=0)
    config.temparature = st.slider("Temparature", min_value=0.0, max_value=2.0, value = config.temparature,step=0.1)
    config.max_tokens = st.slider("Max Tokens", min_value=100, max_value=4000, value = config.max_tokens, step=100)
    st.divider()

    # Display the current configuration seperately 
    st.subheader("Current Configuration")
    st.write(f"**Provider:** {config.provider}")
    st.write(f"**Model:** {config.model}")
    st.write(f"**Temperature:** {config.temparature}")
    st.write(f"**Max Tokens:** {config.max_tokens}")

# Setting Page title
st.title("Sree SL Agentic AI Capstone Project - Chatbot")


# Creating user input section 
config.user_query = st.text_area("Enter your query here:", value=config.user_query, height=300, placeholder="Ask about anything here...") 

# Creating Reponse section 
if st.button("Generate Response",type="primary"):
    if config.user_query.strip() == "":
        st.warning("Please enter a query before generating a response.")
    else:
        #store user query in chat history
        st.session_state.chat_history.append(
            {
                "role": "user",
                "message": config.user_query
            }
        )
        # create a spinner until the response is generated
        with st.spinner("AI Agent is thinking for your response..."):
            # Call crewAI Flow -- To do 
            run(config)

            # Store the response in coversation History
            st.session_state.chat_history.append(
            {
                "role": "assistant",
                "message": config.response
            }
            )
            st.session_state.config = config

# Call the function to generate response based on user query
st.subheader("Conversation History")          
           
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        with st.chat_message("user"):
            st.write(chat["message"])
       
    else:
           with st.chat_message("assistant"):
                st.write(chat["message"])       

# Creating button for users to clear all the chats from UI

if st.sidebar.button("Clear Chat History"):
    st.session_state.chat_history = []
    st.success("Chat history cleared successfully!")
    st.rerun()