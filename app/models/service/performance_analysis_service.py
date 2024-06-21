from repository.performance_analysis_repository import PerformanceAnalysisRepository
from model.performance_analysis import PerformanceAnalysis

class PerformanceAnalysisService:
    @staticmethod
    def get_all_analyses():
        return PerformanceAnalysisRepository.get_all()

    @staticmethod
    def get_analysis_by_id(analysis_id):
        return PerformanceAnalysisRepository.get_by_id(analysis_id)

    @staticmethod
    def create_analysis(data):
        new_analysis = PerformanceAnalysis(**data)
        PerformanceAnalysisRepository.create(new_analysis)
        return new_analysis

    @staticmethod
    def update_analysis(analysis_id, data):
        analysis = PerformanceAnalysisRepository.get_by_id(analysis_id)
        for key, value in data.items():
            setattr(analysis, key, value)
        PerformanceAnalysisRepository.update()
        return analysis

    @staticmethod
    def delete_analysis(analysis_id):
        analysis = PerformanceAnalysisRepository.get_by_id(analysis_id)
        PerformanceAnalysisRepository.delete(analysis)
