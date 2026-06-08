import streamlit as st
from orchestrator import run_agent
from memory import chat_history
from agentTools.document_reader import read_pdf
import memory
from agentTools.chunker import (
    chunk_text
)

from agentTools.vectordb import (
    store_chunks
)

st.title("Research Agent")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    pdf_text = read_pdf(
        uploaded_file
    )

    chunks = chunk_text(
        pdf_text
    )

    store_chunks(
        chunks
    )

    st.success(
        "Document Indexed Successfully"
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

question = st.chat_input(
    "Ask something..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    result = run_agent(
    question
)
    print(result,"======================")

    agent_name = result["agent"]

    answer = result["answer"]
    
    st.info(
    f"🤖 {agent_name}"
)
    
    

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):
        st.write(
            message["content"]
        )