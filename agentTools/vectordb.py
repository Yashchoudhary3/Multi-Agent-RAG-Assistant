import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="documents"
)


def store_chunks(chunks):

    ids = []

    for i in range(len(chunks)):
        ids.append(str(i))

    collection.add(
        documents=chunks,
        ids=ids
    )


def search_chunks(
    query,
    top_k=5
):

    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )

    return results["documents"][0]