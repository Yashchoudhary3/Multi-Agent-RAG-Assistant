from memory import chat_history

from agents.router_agent import (
    route_request
)

from agents.chat_agent import (
    handle_chat
)


from agents.search_agent import (
    handle_search
)

from agents.research_agent import (
    handle_research
)


def run_agent(
    user_question,
):
    
    chat_history.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    tool_request = route_request(
    user_question
)

    action = tool_request["action"]
    
    

    if action == "chat":
     return {
        "agent": "Chat Agent",
        "answer": handle_chat()
    }

    if action == "search":
     return {
        "agent": "Search Agent",
        "answer": handle_search(
            user_question
        )
    }

    if action == "research":
     return {
        "agent": "Research Agent",
        "answer": handle_research(
            user_question
        )
    }

    return "Unknown action"