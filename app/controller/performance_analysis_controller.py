from app.models.service.performance_analysis_service import PerformanceAnalysisService

class PerformanceAnalysisController:
    @staticmethod
    def get_all_analyses():
        return PerformanceAnalysisService.get_all_analyses()

    @staticmethod
    def get_analysis_by_id(analysis_id):
        return PerformanceAnalysisService.get_analysis_by_id(analysis_id)

    @staticmethod
    def create_analysis(data):
        return PerformanceAnalysisService.create_analysis(data)

    @staticmethod
    def update_analysis(analysis_id, data):
        return PerformanceAnalysisService.update_analysis(analysis_id, data)

    @staticmethod
    def delete_analysis(analysis_id):
        return PerformanceAnalysisService.delete_analysis(analysis_id)
