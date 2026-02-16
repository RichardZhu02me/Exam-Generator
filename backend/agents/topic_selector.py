from typing_extensions import TypedDict, Literal
from langgraph.graph import StateGraph, START, END
from agents.core import (
    Topics,
    TopicState,
    get_most_common_attribute,
    get_search_results,
)
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage


class TopicUsability(TypedDict):
    usable_topics: bool


class TopicSelector:
    def search_topics(self, state: TopicState) -> TopicState:
        print(state)
        query = state["messages"][-1].content
        records = get_search_results(state["index"], state["namespace"], query, k=5)
        return {"messages": state["messages"], "retrieved_knowledge": records}

    def select_topics(self, state: TopicState):
        category = get_most_common_attribute(state["retrieved_knowledge"], "category")
        course = get_most_common_attribute(state["retrieved_knowledge"], "course")
        context = ""
        for record in state["retrieved_knowledge"]:
            context += record["text"]
        topic_messages = [
            SystemMessage(
                content=f"You are a University Professor selecting topics from {category} for the course {course}"
            ),
            AIMessage(content=f"Context: {context}"),
            HumanMessage(
                content=f"Choose up to 10 topics from the context that we should test for in a(n) {category} exam"
            ),
        ]
        topics = self.model.with_structured_output(Topics, strict=True).invoke(
            topic_messages, max_tokens=3000
        )
        print(topics)
        print(type(topics))
        return {"messages": state["messages"], "topics": topics["topics"]}

    def decide_topic_usability(
        self, state: TopicState
    ) -> Literal["__end__", "select_topics"]:
        category = get_most_common_attribute(state["retrieved_knowledge"], "category")
        course = get_most_common_attribute(state["retrieved_knowledge"], "course")
        topics = " ".join(state["topics"])
        topic_messages = [
            SystemMessage(
                content=f"You are a University Professor selecting topics from {category} for the course {course}"
            ),
            HumanMessage(
                content=f"Decide whether the following topics can be used to create an interesting question for a {category} exam: {topics}. Provide a dictionary with the key 'usable_topics' and a boolean value, True if the topics are interesting, False otherwise. Give only the dictionary."
            ),
            HumanMessage(content='Example output: {"usable_topics": True}'),
        ]
        usable = self.model.with_structured_output(TopicUsability, strict=True).invoke(
            topic_messages
        )
        if usable["usable_topics"]:
            print(
                "topics can be used to make a creative problem, moving to next subgraph"
            )
        else:
            print("topics are not usable, returning to select_topics")
        return "__end__" if usable["usable_topics"] else "select_topics"

    def get_graph(self):
        return self.graph

    def __init__(self, model):
        self.model = model
        topic_builder = StateGraph(TopicState)
        topic_builder.add_node("search_topics", self.search_topics)
        topic_builder.add_node("select_topics", self.select_topics)
        topic_builder.add_edge(START, "search_topics")
        topic_builder.add_edge("search_topics", "select_topics")
        topic_builder.add_conditional_edges(
            "select_topics", self.decide_topic_usability
        )
        topic_graph = topic_builder.compile()
        self.graph = topic_graph
