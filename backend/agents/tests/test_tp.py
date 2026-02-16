import sys
import os

# Add parent directory to path so we can import from backend root if needed,
# though running as module is better: python -m agents.test
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import config
from agents import topic_selector, pc
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

print("Successfully imported topic_graph, model, and pc")
# You can add instantiation tests here
message = "build me a comprehensive practice exam at a third year University of Waterloo pure math level"
index_name = "course-materials"
idx = pc.Index(name=index_name)
namespace = "pmath333-ch1"
topics = topic_selector.invoke(
    {"messages": [HumanMessage(message)], "index": idx, "namespace": namespace}
)
print(topics)
