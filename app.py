import streamlit as st
from chatbot_logic import get_bot_response

st.image("assets/your_logo.png", width=120)
st.title("Sugana's Conversational AI")

st.markdown(
    """
    <style>
    body {
        background-color: #39556e;
    }
    .stApp {
        background-color: #39556e;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    st.image("logo.png", width=120)
    st.title("Sugana's Conversational AI")
    st.markdown(
    """
    Welcome to my end-to-end Conversational AI Chatbot project, built using **Streamlit**, **LangChain**, and **Llama3** via the **Groq API**.  
    This application demonstrates my expertise in **Python**, **AI/ML integration**, **prompt engineering**, and **user interface design**.

    **Key Features & Technologies:**
    - **Natural Language Processing (NLP):** Seamless multi-turn conversations powered by Llama3.
    - **LangChain Integration:** Utilizes advanced memory modules for context-aware dialogue.
    - **Streamlit UI:** Interactive, responsive web interface for real-time chat.
    - **API Integration:** Secure access to Llama3 through the Groq API.
    - **State Management:** Efficient use of `st.session_state` for chat history and navigation.
    - **Custom Theming:** Professional look with branding and custom styles.
    - **Production-Ready Patterns:** Modular, scalable code suitable for real-world deployment.

    **Skills Demonstrated:**  
    Python | Streamlit | LangChain | Llama3 | Prompt Engineering | API Integration | UI/UX | Chatbot Development | State Management | Software Engineering Best Practices

    ---

    #### Limitations
    - **No Real-Time Data:** The AI model does not access or retrieve real-time information (e.g., live news, stock prices, weather).
    - **No Internet Browsing:** The chatbot cannot browse the web or access external databases during conversation.
    - **No Personal Data Access:** The model does not access user files, emails, or private information.
    - **Static Knowledge Base:** All responses are generated based on the model's pre-trained knowledge up to its last update.
    - **No Transactional Actions:** The chatbot cannot perform actions such as making purchases, bookings, or sending emails on behalf of users.
    - **For Demonstration Only:** Not intended for use in production or for providing professional/legal/medical advice.
    ---
    """
)
