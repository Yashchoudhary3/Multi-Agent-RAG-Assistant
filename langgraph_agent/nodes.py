from agents.router_agent import route_request
from agents.chat_agent import handle_chat
from agents.search_agent import handle_search


def router_node(state):

    question = state["question"]

    tool_request = route_request(
        question
    )

    state["action"] = (
        tool_request["action"]
    )

    return state


def chat_node(state):

    answer = handle_chat()

    state["answer"] = answer

    return state


def search_node(state):

    answer = handle_search(
        state["question"]
    )

    state["answer"] = answer

    return state