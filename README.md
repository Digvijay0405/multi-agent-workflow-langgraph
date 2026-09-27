# 🤖 Multi-Agent Workflow using LangGraph

A LangGraph-powered multi-agent system where specialized AI agents collaborate to complete a task.

## 📌 Overview

This project demonstrates how multiple AI agents communicate through a workflow graph using LangGraph.

The workflow consists of:

* 🧠 Planner Agent
* 👷 Worker Agent
* ✅ Reviewer Agent

The Reviewer Agent validates the Worker Agent's output and can send the task back for revision. After two rejections, the workflow stops and returns a failure state.

---

## 🚀 Features

* Planner → Worker → Reviewer workflow.
* LangGraph state machine with explicit shared state.
* Conditional routing based on reviewer decision.
* Reviewer can reject work and send it back.
* Maximum rejection limit (2).
* Flask web interface with modern UI.
* Workflow execution history.

---

## 🏗️ Architecture

User Task
↓
Planner Agent
↓
Worker Agent
↓
Reviewer Agent
├── Accepted → Final Output
└── Rejected → Worker Agent

Rejected Twice
↓
Needs Human Review (Workflow Ends)

---

## 📊 State Schema

| State        | Description                  |
| ------------ | ---------------------------- |
| task         | User input task              |
| plan         | Planner output               |
| work         | Worker output                |
| review       | Reviewer feedback            |
| status       | accepted / rejected / failed |
| reject_count | Reviewer rejection counter   |
| steps        | Workflow step counter        |
| history      | Execution timeline           |

---

## ⚙️ Tech Stack

* Python
* LangGraph
* Flask
* HTML
* CSS
* JavaScript

---

## ▶️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/multi-agent-workflow-langgraph.git
cd multi-agent-workflow-langgraph

pip install -r requirements.txt
python app.py
```

Open:

`http://127.0.0.1:5000`

---

## 🧪 Example Workflow

**Input**

Explain Artificial Intelligence.

**Execution**

1. Planner creates a plan.
2. Worker generates a response.
3. Reviewer validates the response.
4. If accepted → Final output.
5. If rejected → Worker revises.
6. After two rejections → Workflow ends.

---

## ⚠️ Failure Mode

If the Reviewer Agent rejects the Worker Agent's response twice:

* The workflow stops.
* Status becomes `failed`.
* Final message: **Needs Human Review**.

This prevents infinite retry loops.

---

## 📁 Project Structure

```text
multi-agent-workflow/
├── app.py
├── graph.py
├── agents.py
├── state.py
├── templates/
├── static/
├── requirements.txt
└── README.md
```

---

## 👨‍💻 Author

**Digvijay Dipak Kadam**

Final Year BE Information Technology Student

Zeal College of Engineering and Research, Pune






