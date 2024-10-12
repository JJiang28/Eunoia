from flask import Blueprint, current_app

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/')
def hello():
    return 'Welcome to Eunoia'

@app_routes.route('/add-example', methods=['GET'])
def add_example():
    """Simple route to add a document to Firestore for testing."""
    try:
        db = current_app.config['FIRESTORE_DB']
        doc_ref = db.collection('schedules').document('example_doc')
        doc_ref.set({
            'title': 'Finish Firestore Setup',
            'due_date': '2024-10-11',
            'status': 'In Progress'
        })
        return 'Document added to Firestore!', 200
    except Exception as e:
        return f"An Error Occurred: {e}", 500
