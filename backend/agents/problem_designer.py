from langgraph.graph import StateGraph, START, END
from .core import Topics, TopicState, Problem, ProblemState, get_most_common_attribute
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage


class ProblemDesigner:
    def connect_topics(self, state: TopicState) -> TopicState:
        # print("in connect topics")
        category = get_most_common_attribute(state["retrieved_knowledge"], "category")
        course = get_most_common_attribute(state["retrieved_knowledge"], "course")
        context: str = ""
        for topic in state["topics"]:
            context += topic + ", "
        topic_messages = [
            SystemMessage(
                content=f"You are a University Professor teaching {category} for the course {course}. You are creating a single problem for an exam"
            ),
            AIMessage(content=f"Topics: {context}"),
            HumanMessage(
                content=f"Choose topics from the above list that work cohesively with eachother, to create a meaningful problem for {course} students"
            ),
        ]
        response = self.model.with_structured_output(Topics).invoke(topic_messages)
        return {"messages": state["messages"], "topics": response["topics"]}

    def problem_designer(self, state: TopicState) -> ProblemState:
        print("in problem designer")
        category = get_most_common_attribute(state["retrieved_knowledge"], "category")
        course = get_most_common_attribute(state["retrieved_knowledge"], "course")
        context: str = ""
        for topic in state["topics"]:
            context += topic + ", "
        topic_messages = [
            SystemMessage(
                content=f"""
        Act as a senior academic examiner. Your goal is to design a "distinction-level" problem for a high-stakes university or advanced placement examination.

        The Parameters:

        Course: {course}, {category}

        Specific Topic(s): {context}

        Target Audience: Undergraduate students for {course} in the University of Waterloo
    ZZ
        Problem Requirements:

        Conceptual Depth: The problem must test the intersection of [Topic] and [Secondary Topic, e.g., Trigonometry or Matrix Transformations].

        Structure:Part A: A foundational calculation to build confidence.Part B: A "show that..." proof that requires a non-obvious substitution.Part C: A high-level application or limit-case analysis.

        The "Twist": Include a constraint that prevents the use of a standard calculator or direct software solver (e.g., use variables like $n$, $k$, or $\alpha$ instead of integers).

        Deliverables:

        Provide the problem statement.

        Provide a marking rubric or solution key explaining the "trap" in the logic.
        """
            ),
            HumanMessage(
                content=f"Create a problem for {course} students that combines all the following topics."
            ),
            AIMessage(
                content="""Example output: {"problem": problem, "solution": solution, "rubric": rubric}"""
            ),
        ]
        response = self.model.with_structured_output(Problem).invoke(
            topic_messages, max_tokens=5000
        )
        print([response])

        return {"problems": [response]}
        # return {"problem": response["problem"], "solution": response["solution"]}

    def __init__(self, model):
        self.model = model
        problem_builder = StateGraph(
            TopicState, input_schema=TopicState, output_schema=ProblemState
        )
        problem_builder.add_node("connector", self.connect_topics)
        problem_builder.add_node("designer", self.problem_designer)
        problem_builder.add_edge(START, "connector")
        problem_builder.add_edge("connector", "designer")
        problem_builder.add_edge("designer", END)
        designer_graph = problem_builder.compile()
        self.graph = designer_graph

    def get_graph(self):
        return self.graph
