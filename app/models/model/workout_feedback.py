from . import db

class WorkoutFeedback(db.Model):
    """Class representing a workout feedback in the system."""
    __tablename__ = 'workout_feedbacks'
    feedback_id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey('workout_sessions.session_id'))
    rating = db.Column(db.String)
    comment = db.Column(db.String)
    session = db.relationship('workoutSession', back_populates='feedbacks')
