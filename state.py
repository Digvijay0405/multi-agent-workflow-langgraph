from typing import TypedDict, List

class AgentState(TypedDict):
    # User input
    task: str

    # Planner output
    plan: str

    # Worker output
    work: str

    # Reviewer feedback
    review: str

    # Workflow status
    status: str      # "accepted", "rejected", "failed"

    # Count reviewer rejections
    reject_count: int

    # Step counter (prevents infinite loops)
    steps: int

    # Stores workflow log
    history: List[str]