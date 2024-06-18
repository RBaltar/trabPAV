from . import db

class PerformanceReport(db.Model):
    """Class representing a performance report in the system."""
    __tablename__ = 'performance_reports'
    report_id = db.Column(db.Integer, primary_key=True)
    athlete_id = db.Column(db.Integer, db.ForeignKey('athletes.athlete_id'))
    period = db.Column(db.String)
    performance = db.Column(db.String)
