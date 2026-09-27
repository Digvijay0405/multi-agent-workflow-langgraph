from langgraph.graph import StateGraph, END
from state import AgentState
from agents import planner_agent, worker_agent, reviewer_agent

MAX_STEPS = 10


# -------------------------
# Planner Node
# -------------------------
def planner_node(state: AgentState):
    print("🧠 Planner Agent...")
    return planner_agent(state)


# -------------------------
# Worker Node
# -------------------------
def worker_node(state: AgentState):
    print("👷 Worker Agent...")
    return worker_agent(state)


# -------------------------
# Reviewer Node
# -------------------------
def reviewer_node(state: AgentState):
    print("✅ Reviewer Agent...")
    return reviewer_agent(state)


# -------------------------
# Conditional Router
# -------------------------
def review_router(state: AgentState):

    # Stop if too many steps
    if state["steps"] >= MAX_STEPS:
        state["status"] = "failed"
        state["review"] = "Workflow stopped because step limit was reached."
        return END

    # Reviewer accepted
    if state["status"] == "accepted":
        return END

    # Reviewer rejected twice
    if state["reject_count"] >= 2:
        state["status"] = "failed"
        state["review"] = "Needs Human Review. Reviewer rejected twice."
        return END

    # Reviewer rejected once → send back to worker
    return "worker"


# -------------------------
# Build Workflow
# -------------------------
builder = StateGraph(AgentState)

builder.add_node("planner", planner_node)
builder.add_node("worker", worker_node)
builder.add_node("reviewer", reviewer_node)

builder.set_entry_point("planner")

builder.add_edge("planner", "worker")
builder.add_edge("worker", "reviewer")

builder.add_conditional_edges(
    "reviewer",
    review_router,
    {
        "worker": "worker",
        END: END
    }
)

# This line is REQUIRED
graph = builder.compile()