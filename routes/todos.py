from flask import Blueprint, jsonify, request

todos_bp = Blueprint('todos', __name__)

# Simulasi data
todos = [
    {"id": 1, "task": "Belajar Flask", "done": False},
    {"id": 2, "task": "Push ke GitHub", "done": False},
]

@todos_bp.route("/todos", methods=["GET"])
def get_todos():
    return jsonify({"todos": todos})

@todos_bp.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if todo:
        return jsonify(todo)
    return jsonify({"error": "Todo not found"}), 404

@todos_bp.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()
    if not data or "task" not in data:
        return jsonify({"error": "Invalid input"}), 400
    new_todo = {
        "id": len(todos) + 1,
        "task": data["task"],
        "done": False
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

@todos_bp.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return jsonify({"message": "Todo deleted"})
