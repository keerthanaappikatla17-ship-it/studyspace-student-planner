from datetime import date
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("planner.db")
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            deadline TEXT,
            priority TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    filter_by = request.args.get("filter", "all")
    conn = get_db()

    if filter_by == "pending":
        tasks = conn.execute(
            "SELECT * FROM tasks WHERE completed = 0 ORDER BY deadline"
        ).fetchall()
    elif filter_by == "completed":
        tasks = conn.execute("""
    SELECT * FROM tasks
    ORDER BY completed,
    CASE priority
        WHEN 'High' THEN 1
        WHEN 'Medium' THEN 2
        WHEN 'Low' THEN 3
    END,
    CASE WHEN deadline = '' OR deadline IS NULL THEN 1 ELSE 0 END,
    deadline
""").fetchall()
    else:
        tasks = conn.execute(
            "SELECT * FROM tasks ORDER BY completed, deadline"
        ).fetchall()

    total = conn.execute(
        "SELECT COUNT(*) FROM tasks"
    ).fetchone()[0]

    completed = conn.execute(
        "SELECT COUNT(*) FROM tasks WHERE completed = 1"
    ).fetchone()[0]

    pending = total - completed
    progress = round(completed / total * 100) if total else 0

    conn.close()

    return render_template(
    "index.html",
    tasks=tasks,
    total=total,
    completed=completed,
    pending=pending,
    progress=progress,
    filter_by=filter_by,
    today=date.today().isoformat()
)

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    deadline = request.form.get("deadline", "")
    priority = request.form.get("priority", "Medium")

    if title and priority in ["Low", "Medium", "High"]:
        conn = get_db()
        conn.execute(
            "INSERT INTO tasks (title, deadline, priority) VALUES (?, ?, ?)",
            (title, deadline, priority)
        )
        conn.commit()
        conn.close()

    return redirect("/")

@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    conn = get_db()
    conn.execute(
        "UPDATE tasks SET completed = 1 - completed WHERE id = ?",
        (task_id,)
    )
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    conn = get_db()
    conn.execute(
        "DELETE FROM tasks WHERE id = ?", (task_id,)
    )
    conn.commit()
    conn.close()
    return redirect("/")
    
@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    conn = get_db()

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        deadline = request.form.get("deadline", "")
        priority = request.form.get("priority", "Medium")

        if title and priority in ["Low", "Medium", "High"]:
            conn.execute(
                "UPDATE tasks SET title = ?, deadline = ?, priority = ? WHERE id = ?",
                (title, deadline, priority, task_id)
            )
            conn.commit()

        conn.close()
        return redirect("/")

    task = conn.execute(
        "SELECT * FROM tasks WHERE id = ?", (task_id,)
    ).fetchone()
    conn.close()

    if task is None:
        return "Task not found", 404

    return render_template("edit.html", task=task)


if __name__ == "__main__":
    create_table()
    app.run(debug=True)
