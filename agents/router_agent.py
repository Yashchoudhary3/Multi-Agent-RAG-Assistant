import json

from llm import client
from memory import chat_history


def route_request(user_question):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content":"""
You are a routing assistant.

Available actions:

1. chat
2. search
3. research

Use:

{
    "action":"search"
}

for:
- latest news
- current events
- recent updates
- today's information
- web searches

Examples:
"What is today's news?"
"Latest React version"
"Current Azure updates"

Use:

{
    "action":"research"
}

for:
- questions that require BOTH the uploaded document and web information
- comparing a document against current trends
- analyzing a document using external information

Examples:
"Compare this resume with current React market trends"
"Analyze this document against latest industry standards"
"Are the skills in this resume relevant today?"
"Compare technologies in this document with modern alternatives"

Use:

{
    "action":"chat"
}

for:
- normal conversation
- questions about uploaded documents
- summarization
- explanations
- questions answerable from document context alone

Examples:
"Summarize this document"
"What skills are mentioned?"
"What is this document about?"
"Explain section 3"

Return ONLY JSON.

Example:

{
    "action":"chat"
}
"""
            },
            {
        "role": "user",
        "content": user_question
    }
        ]
    )

    content = response.choices[0].message.content

    clean_content = (
        content
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(clean_content)