# AGENTS.md

## Project Overview

This is a Flask REST API for task management (`gerenciamento-tarefas-flask-postman`). It provides CRUD operations for tasks and user login authentication.

**Tech Stack:** Python 3.10+, Flask 3.1.0, Poetry

---

## Build & Run Commands

### Install Dependencies
```bash
poetry install
```

### Run the Application
```bash
flask run
# or
poetry run python app.py
```

### Run with Flask CLI
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

### Testing with Postman
Import `postman_collection.json` into Postman to test all endpoints:
- `POST /login` - User authentication
- `GET /tasks` - List all tasks
- `GET /tasks/<id>` - Get single task
- `POST /tasks` - Create new task
- `PUT /tasks/<id>` - Update task
- `DELETE /tasks/<id>` - Delete task

---

## Code Style Guidelines

### General
- This codebase uses **Portuguese** for comments and variable names (Brazilian Portuguese)
- Keep functions focused and concise
- Maximum line length: 120 characters

### Imports
- Standard library imports first
- Third-party imports (Flask) second
- One blank line between groups
```python
from flask import Flask, request, jsonify
```

### Naming Conventions
- **Functions/variables:** snake_case (e.g., `get_tasks`, `task_id`)
- **Routes/endpoint names:** lowercase with slashes (e.g., `/tasks`, `/login`)
- **Dictionary keys:** snake_case (e.g., `task_id`, `created_at`)

### Flask Routes
- Use route decorators with explicit HTTP methods
- Use type converters for path parameters (`/<int:task_id>`)
```python
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    ...
```

### JSON Responses
- Use `jsonify()` for all responses
- Return proper HTTP status codes:
  - `200` - Success
  - `201` - Created
  - `400` - Bad request / wrong credentials
  - `404` - Not found
  - `500` - Server error

### Error Handling
- Return JSON error messages consistently
```python
return jsonify({'message': 'task not found'}), 404
```

### Data Model (In-Memory)
Tasks dictionary structure:
```python
{'id': 1, 'title': '...', 'description': '...', 'status': 'done', 'date': '01/01/2025'}
```

Users dictionary structure:
```python
{'id': 1, 'name': 'Ana', 'email': 'ana@example.com', 'password': '123456'}
```

### Request Handling
- Use `request.get_json()` for JSON body parsing
- Validate required fields before processing

---

## File Structure

```
.
├── app.py              # Main Flask application (all routes here)
├── pyproject.toml      # Poetry configuration
├── README.md           # Project documentation
├── postman_collection.json  # Postman API tests
└── AGENTS.md           # This file
```

---

## Development Notes

- App runs in debug mode when executed directly (`app.run(debug=True)`)
- Data is stored in-memory (no database persistence)
- Authentication is simple credential checking (no JWT/tokens)
- Consider adding input validation for production use
