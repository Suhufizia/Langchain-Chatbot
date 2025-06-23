import os
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain_groq import ChatGroq
import streamlit as st

def get_conversation_chain():
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "YOUR_GROQ_API_KEY")
    if not GROQ_API_KEY or GROQ_API_KEY == "YOUR_GROQ_API_KEY":
        st.error("Please set your GROQ_API_KEY environment variable.")
        st.stop()

    if "llm" not in st.session_state:
        st.session_state.llm = ChatGroq(model="llama3-8b-8192", groq_api_key=GROQ_API_KEY)
    if "prompt" not in st.session_state:
        st.session_state.prompt = PromptTemplate(
            input_variables=["history", "input"],
            template="The following is a conversation between a helpful AI assistant and a user.\n\n{history}\nUser: {input}\nAI:"
        )
    if "memory" not in st.session_state:
        st.session_state.memory = ConversationBufferMemory()
    if "conversation" not in st.session_state:
        st.session_state.conversation = ConversationChain(
            llm=st.session_state.llm,
            memory=st.session_state.memory,
            prompt=st.session_state.prompt,
            verbose=False
        )
    return st.session_state.conversation
