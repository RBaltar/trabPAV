from . import db

class WorkoutSession(db.Model):
    """Class representing a workout session in the system."""
    __tablename__ = 'workout_sessions'
    session_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    duration = db.Column(db.Integer)
    workout_type = db.Column(db.String)
    intensity = db.Column(db.String)
    athlete_id = db.Column(db.Integer, db.ForeignKey('athletes.athlete_id'))
    athlete = db.relationship('Athlete', back_populates='workout_sessions')
    feedbacks = db.relationship('workoutFeedback', back_populates='session')
    calendar_id = db.Column(db.Integer, db.ForeignKey('calendars.calendar_id'))
    calendar = db.relationship('Calendar', back_populates='events')
