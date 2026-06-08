from agentTools.retriever import (
    retrieve_context
)

from agents.search_agent import (
    handle_search
)

from llm import client


def handle_research(
    question
):

    context = retrieve_context(
        question
    )

    web_result = handle_search(
        question
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"system",
                "content":"""
You are a research assistant.

Use BOTH:

1. Document Context
2. Web Search Results

to answer.
"""
            },
            {
                "role":"user",
                "content":f"""
Question:
{question}

Document Context:
{context}

Web Search Results:
{web_result}
"""
            }
        ]
    )

    return (
        response
        .choices[0]
        .message
        .content
    )