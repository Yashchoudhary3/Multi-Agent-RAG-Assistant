from agentTools.vectordb import (
    search_chunks
)


def retrieve_context(
    question
):

    chunks = search_chunks(
        question
    )

    return "\n".join(chunks)