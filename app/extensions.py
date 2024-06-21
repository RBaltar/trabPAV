"""
This module sets up the database configuration using SQLAlchemy and Flask-Migrate.
It provides functions to initialize the database and manage migrations.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the SQLAlchemy object
db = SQLAlchemy()

# Initialize the Flask-Migrate object
migrate = Migrate()

def init_db(app):
    """
    Initialize the database with the given Flask application.

    Args:
        app (Flask): The Flask application instance.

    This function initializes the SQLAlchemy and Flask-Migrate extensions with the given
    Flask application and creates all database tables defined in the application models.
    """
    db.init_app(app)
    with app.app_context():
        db.create_all()
