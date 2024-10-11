import os
from flask import Flask
from .db import db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
        
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello():
        return 'Welcome to Eunoia'
    
    @app.route('/add-example', methods=['GET'])
    def add_example():
        """Simple route to add a document to Firestore for testing."""
        try:
            doc_ref = db.collection('schedules').document('example_doc')
            doc_ref.set({
                'title': 'Finish Firestore Setup',
                'due_date': '2024-10-11',
                'status': 'In Progress'
            })
            return 'Document added to Firestore!', 200
        except Exception as e:
            return f"An Error Occurred: {e}", 500
    
    return app