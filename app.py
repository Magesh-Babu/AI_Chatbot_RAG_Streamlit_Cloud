import streamlit as st
import tempfile
import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llm import initialize_llm
from query_type import handle_general_query, handle_document_query
from chat import display_chat, clear_chat_history

# Initialize the Azure LLM
llm = initialize_llm()

def create_index(documents):
    """Creates and returns a VectorStore index from the documents."""
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
    return index

# Sidebar for file upload and settings
with st.sidebar:
    st.title("🧑‍🏫 LLM Chatbot with RAG")
    st.markdown("Upload a document and start asking questions. Or ask general questions without uploading any document.")

    # File uploader for document (supports PDF and text files)
    uploaded_document = st.file_uploader("Upload Document (PDF or Text)", type=["pdf", "txt"])

    if uploaded_document is not None:
        # Save the uploaded file to a temporary file on disk
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_document.name)[1]) as tmp_file:
            tmp_file.write(uploaded_document.read())
            tmp_file_path = tmp_file.name

        # Use SimpleDirectoryReader to read the document from the file path
        with st.spinner("Processing document..."):
            reader = SimpleDirectoryReader(input_files=[tmp_file_path])
            documents = reader.load_data()

        # Load data and create an index
        index = create_index(documents)
        st.success(f"Document '{uploaded_document.name}' uploaded successfully! You can now ask questions.")

    st.sidebar.button('Clear Chat History', on_click=clear_chat_history)  

# Main app logic
if uploaded_document:
    display_chat()
    if prompt := st.chat_input("Ask a question about uploaded document"):
        handle_document_query(index, prompt, llm)
else:
    # Show general chat interface if no document is uploaded or after reset
    display_chat()
    if prompt := st.chat_input("Ask a general question"):
        handle_general_query(prompt, llm)
