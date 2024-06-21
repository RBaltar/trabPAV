from app import db
from app.models.model import PerformanceReport

class PerformanceReportRepository:
    def create(self, athlete_id, period, performance):
        report = PerformanceReport(athlete_id=athlete_id, period=period, performance=performance)
        db.session.add(report)
        db.session.commit()
        return report
    
    def update(self, report_id, athlete_id, period, performance):
        report = self.find_by_id(report_id)
        if report:
            if athlete_id:
                report.athlete_id = athlete_id
            if period:
                report.period = period
            if performance:
                report.performance = performance
            db.session.commit()
        return report
    
    def delete(self, report_id):
        report = self.find_by_id(report_id)
        if report:
            db.session.delete(report)
            db.session.commit()
        return report
    
    def find_by_id(self, report_id):
        return PerformanceReport.query.get(report_id)
    
    def find_all(self):
        return PerformanceReport.query.all()