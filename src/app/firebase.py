import firebase_admin
from firebase_admin import credentials, firestore

def init_firebase():
    # Initialize Firebase if it hasn't been initialized already
    if not firebase_admin._apps:
        cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred)
    
    return firestore.client()