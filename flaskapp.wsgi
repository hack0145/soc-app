# flaskapp.wsgi
import sys
import os

# Set the path to your Flask app directory
sys.path.insert(0, '/home/karty/App')

from app import app as application  # Import your Flask app (ensure the app object is named `app` in app.py)
