from agents.core import ProblemState, ExamState
from langgraph.graph import StateGraph, START, END
from agents.topic_selector import TopicSelector
from agents.problem_designer import ProblemDesigner
from langgraph.types import Send
from agents.core import TopicState
from langchain_core.messages import HumanMessage
from schemas import Prompt
from thirdparty.pinecone_client import pc

### TODO: implement a more thorough exam compiler


def exam_compiler(state: ProblemState) -> ExamState:
    # print("in exam compiler")
    for problem in state["problems"]:
        print(problem)


def continue_to_problem_design(state: TopicState):
    return [Send("Problem Designer", state) for i in range(3)]


class ExamAgent:
    def __init__(self, model):
        agent_builder = StateGraph(
            ExamState, input_schema=TopicState, output_schema=ExamState
        )
        agent_builder.add_node("Topic Selector", TopicSelector(model).get_graph())
        agent_builder.add_node("Problem Designer", ProblemDesigner(model).get_graph())
        agent_builder.add_node("Exam Compiler", exam_compiler)
        agent_builder.add_edge(START, "Topic Selector")
        agent_builder.add_conditional_edges(
            "Topic Selector", continue_to_problem_design, ["Problem Designer"]
        )
        agent_builder.add_edge("Problem Designer", "Exam Compiler")
        agent_builder.add_edge("Exam Compiler", END)
        agent_graph = agent_builder.compile()
        self.graph = agent_graph

    def get_graph(self):
        return self.graph

    def invoke(self, prompt: Prompt):
        return self.graph.invoke(
            {
                "messages": [HumanMessage(prompt.prompt)],
                "index": pc.Index(name=prompt.index_name),
                "namespace": prompt.namespace,
            }
        )
