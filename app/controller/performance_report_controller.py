from app.models.service.performance_report_service import PerformanceReportService

class PerformanceReportController:
    @staticmethod
    def get_all_reports():
        return PerformanceReportService.get_all_reports()

    @staticmethod
    def get_report_by_id(report_id):
        return PerformanceReportService.get_report_by_id(report_id)

    @staticmethod
    def create_report(data):
        return PerformanceReportService.create_report(data)

    @staticmethod
    def update_report(report_id, data):
        return PerformanceReportService.update_report(report_id, data)

    @staticmethod
    def delete_report(report_id):
        return PerformanceReportService.delete_report(report_id)
