from app import db
from app.models.model import AnalyzePerformance

class AnalyzePerformanceRepository:
    def create(self, athelte_id, charts, statistics):
        analysis = AnalyzePerformance(athelte_id=athelte_id, charts=charts, statistics=statistics)
        db.session.add(analysis)
        db.session.commit()
        return analysis
    
    def update(self, analysis_id, athelte_id, charts, statistics):
        analysis = self.find_by_id(analysis_id)
        if analysis:
            if athelte_id:
                analysis.athlete_id = athelte_id
            if charts:
                analysis.charts = charts
            if statistics:
                analysis.statistics = statistics
            db.session.commit()
        return analysis
    
    def delete(self, analysis_id):
        analysis = self.find_by_id(analysis_id)
        if analysis:
            db.session.delete(analysis_id)
            db.session.commit()
        return analysis
    
    def find_by_id(self, analysis_id):
        return AnalyzePerformance.query.get(analysis_id)
    
    def find_all(self):
        return AnalyzePerformance.query.all()