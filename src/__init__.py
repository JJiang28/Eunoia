import os
from flask import Flask
from .db import db
from dotenv import load_dotenv

def create_app(test_config=None):
    load_dotenv()

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev'),
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
                'title': 'Finish Firestore Setup3',
                'due_date': '2024-10-13',
                'status': 'In Progress3'
            })
            return 'Document added to Firestore!', 200
        except Exception as e:
            return f"An Error Occurred: {e}", 500
    
    return app