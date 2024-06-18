from . import db

class User(db.Model):
    """Class representing a user in the system."""
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String, unique=True)
    role = db.Column(db.String)  # Coach, Athlete
    athletes = db.relationship('Athlete', back_populates='coach')
