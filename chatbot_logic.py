# Chatbot Functions/Classes
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "YOUR_GROQ_API_KEY")
    if not GROQ_API_KEY or GROQ_API_KEY == "YOUR_GROQ_API_KEY":
        st.error("Please set your GROQ_API_KEY environment variable.")
        st.stop()

    llm = ChatGroq(model="llama3-8b-8192", groq_api_key=GROQ_API_KEY)
    prompt = PromptTemplate(
        input_variables=["history", "input"],
        template="The following is a conversation between a helpful AI assistant and a user.\n\n{history}\nUser: {input}\nAI:"
    )

    if "memory" not in st.session_state:
        st.session_state.memory = ConversationBufferMemory()
    if "conversation" not in st.session_state:
        st.session_state.conversation = ConversationChain(
            llm=llm,
            memory=st.session_state.memory,
            prompt=prompt,
            verbose=False
        )

    # Display chat history
    for msg in st.session_state.memory.chat_memory.messages:
        if msg.type == "human":
            st.markdown(
                f"""
                <div style='background-color:#3858c9; padding:10px; border-radius:10px; margin-bottom:5px; text-align:right; max-width: 80%; float: right; clear: both;'>
                    <b>🧑 Sugana:</b> {msg.content}
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div style='background-color:#3858c9; padding:10px; border-radius:10px; margin-bottom:5px; text-align:left; max-width: 80%; float: left; clear: both;'>
                    <b>🤖 Bot:</b> {msg.content}
                </div>
                """,
                unsafe_allow_html=True
            )
