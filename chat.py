import os
import streamlit as st

def display_chat():
    """Displays chat messages stored in session state."""
    if "messages" not in st.session_state or not st.session_state.messages:
        # Initialize default general chat messages
        st.session_state.messages = [{"role": "assistant", "content": "Hello, How can i help you?"}]
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
            

def clear_chat_history():
    """Clears the chat history and resets the session state."""
    st.session_state.messages = []
    if "chat_engine" in st.session_state:
        del st.session_state.chat_engine
    if "uploaded_file_path" in st.session_state:
        try:
            os.remove(st.session_state.uploaded_file_path)
        except FileNotFoundError:
            pass
        del st.session_state.uploaded_file_path

