from . import db

class Calendar(db.Model):
    """Class representing a calendar in the system."""
    __tablename__ = 'calendars'
    calendar_id = db.Column(db.Integer, primary_key=True)
    athlete_id = db.Column(db.Integer, db.ForeignKey('athletes.athlete_id'))
    athlete = db.relationship('Athlete', back_populates='calendar')
    events = db.relationship('TrainingSession', back_populates='calendar')
