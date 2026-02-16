from pinecone import Pinecone
from thirdparty.pinecone_client import pc


## returns the dense index object, otherwise creates it if it doesn't exist
def get_index(index_name: str) -> Pinecone.Index:
    index_name = "course-materials"

    if not pc.has_index(name=index_name):
        pc.create_index_for_model(
            name=index_name,
            cloud="aws",
            region="us-east-1",
            dimension=1024,
            metric="cosine",
            embed={"model": "llama-text-embed-v2", "field_map": {"text": "chunk_text"}},
        )

    # Get an Index client for the index we created
    dense_index = pc.Index(name=index_name)
    return dense_index


## upserts records into the Pinecone index
def upsert_records(dense_index: Pinecone.Index, records: list[dict]) -> None:
    # Upsert records into a namespace
    dense_index.upsert_records(namespace="course-materials", records=records)
