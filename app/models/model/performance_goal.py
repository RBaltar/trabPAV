from . import db

class PerformanceGoal(db.Model):
    """Class representing a performance goal in the system."""
    __tablename__ = 'performance_goals'
    goal_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    status = db.Column(db.String)
    athlete_id = db.Column(db.Integer, db.ForeignKey('athletes.athlete_id'))
    athlete = db.relationship('Athlete', back_populates='performance_goals')
