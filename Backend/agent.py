from langgraph.graph import StateGraph
from tools import log_interaction, follow_up

class AgentState(dict):
    pass

graph = StateGraph(AgentState)

graph.add_node("log", lambda s: log_interaction(s["text"]))
graph.add_node("follow", lambda s: follow_up(s["summary"]))

graph.set_entry_point("log")
graph.add_edge("log", "follow")

agent_app = graph.compile()
