from agents import exam_agent, pc
from langchain_core.messages import HumanMessage


message = "build me a comprehensive practice exam at a third year University of Waterloo pure math level"
index_name = "course-materials"
idx = pc.Index(name=index_name)
namespace = "pmath333-ch2"


result = exam_agent.invoke(
    {"messages": [HumanMessage(message)], "index": idx, "namespace": namespace}
)
print(result)
