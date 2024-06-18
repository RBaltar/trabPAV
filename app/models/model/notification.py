from . import db

class Notification(db.Model):
    """Class representing a notification in the system."""
    __tablename__ = 'notifications'
    notification_id = db.Column(db.Integer, primary_key=True)
    athlete_id = db.Column(db.Integer, db.ForeignKey('athletes.athlete_id'))
    type = db.Column(db.String)
    message = db.Column(db.String)
    date = db.Column(db.Date)
