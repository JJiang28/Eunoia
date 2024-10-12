import os
from flask import Flask
from dotenv import load_dotenv
from .firebase import init_firebase
from .routes import app_routes

def create_app(test_config = None):
    load_dotenv() #load envionment variables from .env. Flask doesn't support this, so install pip install python-dotenv   

    app = Flask(__name__, instance_relative_config=True)

    secret_key = os.environ.get('SECRET_KEY') 
    if not secret_key:
        raise ValueError("No SECRET_KEY set for Flask application")
    
    app.config.from_mapping(
        SECRET_KEY=secret_key
    )

    app.register_blueprint(app_routes)

    db = init_firebase()

    app.config['FIRESTORE_DB'] = db
    return app