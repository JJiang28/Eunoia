from flask import Blueprint, current_app, request, jsonify

class Habit:
    def __init__(self, name, description, weekly_time_commitment, goal_length, success_measurement):
        self.name = name
        self.description = description
        self.weekly_time_commitment = weekly_time_commitment
        self.goal_length = goal_length
        self.success_measurement = success_measurement

    def to_dict(self):
        return {
            'description': self.description,
            'weekly_time_commitment': self.weekly_time_commitment,
            'goal_length': self.goal_length,
            'success_measurement': self.success_measurement,
        }
    
app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/')
def hello():
    return 'Welcome to Eunoia'

@app_routes.route('/add-habit', methods = ['POST'])
def add_habit():
    try:
        db = current_app.config['FIRESTORE_DB']
        #get habit details from the request JSON
        habit_data = request.get_json()
        habit_name = habit_data.get('name')
        description = habit_data.get('description')
        weekly_time_commitment = habit_data.get('weekly_time_commitment')
        goal_length = habit_data.get('goal_length')
        success_measurement = habit_data.get('success_measurement')

        #only habit name required for no
        if not habit_name:
            return jsonify({"error": "Habit name is required"}), 400

        #creating a habit instance
        new_habit = Habit(
            name = habit_name,
            description = description,
            weekly_time_commitment = weekly_time_commitment,
            goal_length = goal_length,
            success_measurement = success_measurement
        )

        #save to Firestore using the habit name as the document ID
        doc_ref = db.collection('habits').document(habit_name)
        doc_ref.set(new_habit.to_dict())

        return jsonify({"message": "Habit added successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# @app_routes.route('/add-example', methods=['POST'])
# def add_example():
#     """Simple route to add a document to Firestore for testing."""
#     try:
#         db = current_app.config['FIRESTORE_DB']
#         doc_ref = db.collection('schedules').document('example_doc')
#         doc_ref.set({
#             'title': 'Finish Firestore Setup',
#             'due_date': '2024-10-11',
#             'status': 'In Progress'
#         })
#         return 'Document added to Firestore!', 200
#     except Exception as e:
#         return f"An Error Occurred: {e}", 500
