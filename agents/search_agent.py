from agentTools.search import search_web
from llm import client
from memory import chat_history
from memory import document_text


def handle_search(user_question):
    
    
    results = search_web(
        user_question
    )
    

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"system",
                "content":"""
Answer using the search results.
"""
            },
            {
                "role":"user",
                "content":f"""
Question:
{user_question}

Document Context:
{document_text[:5000]}

Search Results:
{results}
"""
            }
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
            "role":"assistant",
            "content":answer
        }
    )

    return answer