import sqlite3
from pathlib import Path

from flask import Flask, jsonify, request


app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "tasks.db"


def get_db_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def row_to_dict(row):
    return dict(row) if row else None


def init_db():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT NOT NULL CHECK (status IN ('to do', 'in progress', 'done')),
            due_date TEXT,
            priority TEXT NOT NULL DEFAULT 'medium' CHECK (priority IN ('low', 'medium', 'high')),
            user_id INTEGER,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
        """
    )

    cursor.execute("SELECT COUNT(*) AS total FROM users")
    if cursor.fetchone()["total"] == 0:
        cursor.executemany(
            "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
            [
                ("Ana", "ana@example.com", "123456"),
                ("Agatha", "agatha@example.com", "678910"),
            ],
        )

    cursor.execute("SELECT COUNT(*) AS total FROM tasks")
    if cursor.fetchone()["total"] == 0:
        cursor.executemany(
            """
            INSERT INTO tasks (title, description, status, due_date, priority, user_id)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            [
                ("dar comida pro cachorro", "marca da racao", "done", "2025-01-01", "medium", 1),
                ("comprar leite", "zero lactose", "done", "2025-02-02", "low", 2),
                ("estudar SQL", "praticar SELECT, WHERE e JOIN", "in progress", "2026-06-20", "high", 1),
            ],
        )

    connection.commit()
    connection.close()


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok", "database": DB_PATH.name})


@app.route("/login", methods=["POST"])
def login():
    login_user = request.get_json() or {}
    email = login_user.get("email")
    password = login_user.get("password")

    if not email or not password:
        return jsonify({"message": "email and password are required"}), 400

    connection = get_db_connection()
    user = connection.execute(
        "SELECT id, name, email FROM users WHERE email = ? AND password = ?",
        (email, password),
    ).fetchone()
    connection.close()

    if user:
        return jsonify({"message": "login successful", "user": row_to_dict(user)}), 200

    return jsonify({"message": "wrong credentials"}), 400


@app.route("/users", methods=["GET"])
def get_users():
    connection = get_db_connection()
    users = connection.execute("SELECT id, name, email FROM users ORDER BY id").fetchall()
    connection.close()
    return jsonify([row_to_dict(user) for user in users])


@app.route("/tasks", methods=["GET"])
def get_tasks():
    status = request.args.get("status")
    priority = request.args.get("priority")
    user_id = request.args.get("user_id")

    query = """
        SELECT
            tasks.id,
            tasks.title,
            tasks.description,
            tasks.status,
            tasks.due_date,
            tasks.priority,
            tasks.user_id,
            users.name AS user_name,
            tasks.created_at,
            tasks.updated_at
        FROM tasks
        LEFT JOIN users ON users.id = tasks.user_id
    """
    filters = []
    params = []

    if status:
        filters.append("tasks.status = ?")
        params.append(status)
    if priority:
        filters.append("tasks.priority = ?")
        params.append(priority)
    if user_id:
        filters.append("tasks.user_id = ?")
        params.append(user_id)

    if filters:
        query += " WHERE " + " AND ".join(filters)

    query += " ORDER BY tasks.id"

    connection = get_db_connection()
    tasks = connection.execute(query, params).fetchall()
    connection.close()

    return jsonify([row_to_dict(task) for task in tasks])


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    connection = get_db_connection()
    task = connection.execute(
        """
        SELECT
            tasks.id,
            tasks.title,
            tasks.description,
            tasks.status,
            tasks.due_date,
            tasks.priority,
            tasks.user_id,
            users.name AS user_name,
            tasks.created_at,
            tasks.updated_at
        FROM tasks
        LEFT JOIN users ON users.id = tasks.user_id
        WHERE tasks.id = ?
        """,
        (task_id,),
    ).fetchone()
    connection.close()

    if task:
        return jsonify(row_to_dict(task))

    return jsonify({"message": "task not found"}), 404


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json() or {}
    title = data.get("title")
    status = data.get("status", "to do")
    priority = data.get("priority", "medium")

    if not title:
        return jsonify({"message": "title is required"}), 400

    if status not in ("to do", "in progress", "done"):
        return jsonify({"message": "status must be: to do, in progress or done"}), 400

    if priority not in ("low", "medium", "high"):
        return jsonify({"message": "priority must be: low, medium or high"}), 400

    connection = get_db_connection()
    cursor = connection.execute(
        """
        INSERT INTO tasks (title, description, status, due_date, priority, user_id)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            title,
            data.get("description"),
            status,
            data.get("due_date"),
            priority,
            data.get("user_id"),
        ),
    )
    connection.commit()
    task_id = cursor.lastrowid
    task = connection.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    connection.close()

    return jsonify(row_to_dict(task)), 201


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json() or {}

    allowed_fields = ["title", "description", "status", "due_date", "priority", "user_id"]
    updates = []
    params = []

    if "status" in data and data["status"] not in ("to do", "in progress", "done"):
        return jsonify({"message": "status must be: to do, in progress or done"}), 400

    if "priority" in data and data["priority"] not in ("low", "medium", "high"):
        return jsonify({"message": "priority must be: low, medium or high"}), 400

    for field in allowed_fields:
        if field in data:
            updates.append(f"{field} = ?")
            params.append(data[field])

    if not updates:
        return jsonify({"message": "no valid fields to update"}), 400

    updates.append("updated_at = CURRENT_TIMESTAMP")
    params.append(task_id)

    connection = get_db_connection()
    existing_task = connection.execute("SELECT id FROM tasks WHERE id = ?", (task_id,)).fetchone()

    if not existing_task:
        connection.close()
        return jsonify({"message": "task not found"}), 404

    connection.execute(f"UPDATE tasks SET {', '.join(updates)} WHERE id = ?", params)
    connection.commit()
    task = connection.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    connection.close()

    return jsonify(row_to_dict(task))


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    connection = get_db_connection()
    task = connection.execute("SELECT id FROM tasks WHERE id = ?", (task_id,)).fetchone()

    if not task:
        connection.close()
        return jsonify({"message": "task not found"}), 404

    connection.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    connection.commit()
    connection.close()

    return jsonify({"message": "task deleted"})


@app.route("/reports/tasks-by-status", methods=["GET"])
def get_tasks_by_status():
    connection = get_db_connection()
    rows = connection.execute(
        """
        SELECT status, COUNT(*) AS total
        FROM tasks
        GROUP BY status
        ORDER BY total DESC
        """
    ).fetchall()
    connection.close()

    return jsonify([row_to_dict(row) for row in rows])


@app.route("/reports/tasks-by-user", methods=["GET"])
def get_tasks_by_user():
    connection = get_db_connection()
    rows = connection.execute(
        """
        SELECT
            users.id AS user_id,
            users.name AS user_name,
            COUNT(tasks.id) AS total_tasks
        FROM users
        LEFT JOIN tasks ON tasks.user_id = users.id
        GROUP BY users.id, users.name
        ORDER BY total_tasks DESC
        """
    ).fetchall()
    connection.close()

    return jsonify([row_to_dict(row) for row in rows])


init_db()


if __name__ == "__main__":
    app.run(debug=True)
