from model.performance_goal import PerformanceGoal
from app import db

class PerformanceGoalRepository:
    @staticmethod
    def get_all():
        return PerformanceGoal.query.all()

    @staticmethod
    def get_by_id(goal_id):
        return PerformanceGoal.query.get(goal_id)

    @staticmethod
    def create(performance_goal):
        db.session.add(performance_goal)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(performance_goal):
        db.session.delete(performance_goal)
        db.session.commit()
