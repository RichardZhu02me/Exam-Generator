from .topic_selector import TopicSelector
from .problem_designer import ProblemDesigner
from .initialize_models import model
from .agent import ExamAgent
from pinecone import Pinecone

topic_selector = TopicSelector(model).get_graph()
problem_designer = ProblemDesigner(model).get_graph()
exam_agent = ExamAgent(model)
pc = Pinecone()
