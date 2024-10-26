# src/app/routes/habits_routes.py
from flask import Blueprint, current_app, request, jsonify
from ..models.habit import Habit

habits_routes = Blueprint('habits_routes', __name__)

@habits_routes.route('/add-habit', methods=['POST'])
def add_habit():
    try:
        db = current_app.config['FIRESTORE_DB']
        habit_data = request.get_json()
        habit_name = habit_data.get('name')
        description = habit_data.get('description')
        weekly_time_commitment = habit_data.get('weekly_time_commitment')
        goal_length = habit_data.get('goal_length')
        success_measurement = habit_data.get('success_measurement')

        if not habit_name:
            return jsonify({"error": "Habit name is required"}), 400

        new_habit = Habit(
            name=habit_name,
            description=description,
            weekly_time_commitment=weekly_time_commitment,
            goal_length=goal_length,
            success_measurement=success_measurement
        )

        doc_ref = db.collection('habits').document(habit_name)
        doc_ref.set(new_habit.to_dict())

        return jsonify({"message": "Habit added successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
