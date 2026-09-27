from flask import Flask, render_template, request
from graph import graph

app = Flask(__name__)

# Store last 5 tasks (search history)
history = []

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        task = request.form["task"]

        # Initial LangGraph state
        state = {
            "task": task,
            "plan": "",
            "work": "",
            "review": "",
            "status": "",
            "reject_count": 0,
            "steps": 0,
            "history": []
        }

        # Run the graph
        result = graph.invoke(state)

        # Save search history
        history.insert(0, task)
        if len(history) > 5:
            history.pop()

        return render_template(
            "index.html",
            task=task,
            plan=result["plan"],
            work=result["work"],
            review=result["review"],
            status=result["status"],
            reject_count=result["reject_count"],
            steps=result["steps"],
            workflow_history=result["history"],
            history=history
        )

    # First page load
    return render_template(
        "index.html",
        task=None,
        plan=None,
        work=None,
        review=None,
        status=None,
        reject_count=0,
        steps=0,
        workflow_history=[],
        history=history
    )


if __name__ == "__main__":
    app.run(debug=True)