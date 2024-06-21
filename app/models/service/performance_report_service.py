from repository.performance_report_repository import PerformanceReportRepository
from model.performance_report import PerformanceReport

class PerformanceReportService:
    @staticmethod
    def get_all_reports():
        return PerformanceReportRepository.get_all()

    @staticmethod
    def get_report_by_id(report_id):
        return PerformanceReportRepository.get_by_id(report_id)

    @staticmethod
    def create_report(data):
        new_report = PerformanceReport(**data)
        PerformanceReportRepository.create(new_report)
        return new_report

    @staticmethod
    def update_report(report_id, data):
        report = PerformanceReportRepository.get_by_id(report_id)
        for key, value in data.items():
            setattr(report, key, value)
        PerformanceReportRepository.update()
        return report

    @staticmethod
    def delete_report(report_id):
        report = PerformanceReportRepository.get_by_id(report_id)
        PerformanceReportRepository.delete(report)
