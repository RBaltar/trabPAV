from . import db

class AnalyzePerformance(db.Model):
    """Class representing a performance analysis in the system."""
    __tablename__ = 'analyze_performance'
    analysis_id = db.Column(db.Integer, primary_key=True)
    athlete_id = db.Column(db.Integer, db.ForeignKey('athletes.athlete_id'))
    charts = db.Column(db.String)
    statistics = db.Column(db.String)
