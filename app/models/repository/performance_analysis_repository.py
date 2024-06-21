from app.models.model.performance_analysis import PerformanceAnalysis
from app import db

class PerformanceAnalysisRepository:
    @staticmethod
    def get_all():
        return PerformanceAnalysis.query.all()

    @staticmethod
    def get_by_id(analysis_id):
        return PerformanceAnalysis.query.get(analysis_id)

    @staticmethod
    def create(performance_analysis):
        db.session.add(performance_analysis)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(performance_analysis):
        db.session.delete(performance_analysis)
        db.session.commit()
