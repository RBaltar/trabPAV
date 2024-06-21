from repository.performance_goal_repository import PerformanceGoalRepository
from model.performance_goal import PerformanceGoal

class PerformanceGoalService:
    @staticmethod
    def get_all_goals():
        return PerformanceGoalRepository.get_all()

    @staticmethod
    def get_goal_by_id(goal_id):
        return PerformanceGoalRepository.get_by_id(goal_id)

    @staticmethod
    def create_goal(data):
        new_goal = PerformanceGoal(**data)
        PerformanceGoalRepository.create(new_goal)
        return new_goal

    @staticmethod
    def update_goal(goal_id, data):
        goal = PerformanceGoalRepository.get_by_id(goal_id)
        for key, value in data.items():
            setattr(goal, key, value)
        PerformanceGoalRepository.update()
        return goal

    @staticmethod
    def delete_goal(goal_id):
        goal = PerformanceGoalRepository.get_by_id(goal_id)
        PerformanceGoalRepository.delete(goal)
