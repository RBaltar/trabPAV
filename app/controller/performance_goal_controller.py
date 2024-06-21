from app.models.service.performance_goal_service import PerformanceGoalService

class PerformanceGoalController:
    @staticmethod
    def get_all_goals():
        return PerformanceGoalService.get_all_goals()

    @staticmethod
    def get_goal_by_id(goal_id):
        return PerformanceGoalService.get_goal_by_id(goal_id)

    @staticmethod
    def create_goal(data):
        return PerformanceGoalService.create_goal(data)

    @staticmethod
    def update_goal(goal_id, data):
        return PerformanceGoalService.update_goal(goal_id, data)

    @staticmethod
    def delete_goal(goal_id):
        return PerformanceGoalService.delete_goal(goal_id)
