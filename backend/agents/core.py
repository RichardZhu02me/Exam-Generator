from langgraph.graph.message import MessagesState
from typing import Annotated
from pydantic import BaseModel
from pinecone import SearchQuery, SearchRerank
from pinecone.core.openapi.db_data.models import SearchRecordsResponse
from pinecone.db_data.index import Index as PineconeIndex
from typing import TypedDict
from operator import add


def replace(a, b):
    return b


def update(a: list, b: list):
    set_a = set(a)
    set_b = set(b)
    return list(set_a.union(set_b))


# records that we retrieve
class CourseRecord(BaseModel):
    text: str
    category: str
    course: str
    subject: str


class Problem(TypedDict):
    problem: str
    solution: str
    rubric: str


class Topics(TypedDict):
    topics: list[str]


class TopicState(MessagesState):
    retrieved_knowledge: Annotated[list[CourseRecord], replace]
    topics: Annotated[list[str], update]
    index: PineconeIndex
    namespace: str


class ProblemState(MessagesState):
    problems: Annotated[list[Problem], add]


class ExamState(MessagesState):
    retrieved_knowledge: Annotated[list[CourseRecord], replace]
    topics: Annotated[list[str], update]
    problems: Annotated[list[Problem], add]
    index: PineconeIndex
    namespace: str


def get_most_common_attribute(records: list[CourseRecord], attribute: str):
    attributes = [record[attribute] for record in records]
    return max(set(attributes), key=attributes.count)


def search(
    index: PineconeIndex, namespace: str, query: str, k: int = 3
) -> SearchRecordsResponse:
    # Search the dense index
    results: SearchRecordsResponse = index.search(
        namespace=namespace,
        query=SearchQuery(top_k=k, inputs={"text": query}),
        rerank=SearchRerank(model="bge-reranker-v2-m3", top_n=10, rank_fields=["text"]),
    )
    return results


def get_search_results(
    index: PineconeIndex, namespace: str, query: str, k: int = 3
) -> list[CourseRecord]:
    results = search(index, namespace, query, k=5)
    records = []
    for hit in results["result"]["hits"]:
        records.append(hit["fields"])
    return records
