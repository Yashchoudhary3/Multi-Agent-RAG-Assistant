from llm import client
from memory import chat_history
from agentTools.retriever import (
    retrieve_context
)

def handle_chat():
    
    context = retrieve_context(
    chat_history[-1]["content"]
)
    
    response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role":"system",
            "content":f"""
You are a helpful assistant.

If document context exists,
use it when relevant.

Document Context:

{context}
"""
        },
        *chat_history
    ]
)

    answer = (
        response
        .choices[0]
        .message
        .content
    )

    chat_history.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    return answer