from . import db

class Athlete(db.Model):
    """Class representing an athlete in the system."""
    __tablename__ = 'athletes'
    athlete_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birth_date = db.Column(db.Date)
    gender = db.Column(db.String)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    coach_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    coach = db.relationship('User', back_populates='athletes')
    workout_session = db.relationship('WorkoutSession', back_populates='athlete')
    performance_goals = db.relationship('PerformanceGoal', back_populates='athlete')
    calendar = db.relationship('Calendar', back_populates='athlete', uselist=False)
