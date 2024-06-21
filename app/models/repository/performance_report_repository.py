from model.performance_report import PerformanceReport
from app import db

class PerformanceReportRepository:
    @staticmethod
    def get_all():
        return PerformanceReport.query.all()

    @staticmethod
    def get_by_id(report_id):
        return PerformanceReport.query.get(report_id)

    @staticmethod
    def create(performance_report):
        db.session.add(performance_report)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(performance_report):
        db.session.delete(performance_report)
        db.session.commit()
