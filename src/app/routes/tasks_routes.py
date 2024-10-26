# src/app/routes/tasks_routes.py
from flask import Blueprint, current_app, request, jsonify
from ..models.task import Task

tasks_routes = Blueprint('tasks_routes', __name__)

@tasks_routes.route('/add-task', methods=['POST'])
def add_task():
    try:
        db = current_app.config['FIRESTORE_DB']
        task_data = request.get_json()
        title = task_data.get('title')
        description = task_data.get('description')
        due_date = task_data.get('due_date')
        priority = task_data.get('priority')
        status = task_data.get('status')

        if not title:
            return jsonify({"error": "Task title is required"}), 400

        new_task = Task(
            title=title,
            description=description,
            due_date=due_date,
            priority=priority,
            status=status
        )

        doc_ref = db.collection('tasks').document(title)
        doc_ref.set(new_task.to_dict())

        return jsonify({"message": "Task added successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
