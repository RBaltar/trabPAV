from app import db
from app.models.model import PerformanceGoal

class PerformanceGoalRepository:
    def create(self, description, start_date, end_date, status, athlete_id):
        goal = PerformanceGoal(description=description, start_date=start_date, end_date=end_date, status=status, athlete_id=athlete_id)
        db.session.add(goal)
        db.session.commit()
        return goal
    
    def update(self, goal_id, description, start_date, end_date, status, athlete_id):
        goal = self.find_by_id(goal_id)
        if goal:
            if description:
                goal.description = description
            if start_date:
                goal.start_date = start_date
            if end_date:
                goal.end_date = end_date
            if status:
                goal.status = status
            if athlete_id:
                goal.athlete_id = athlete_id
            db.session.commit()
        return goal
    
    def delete(self, goal_id):
        goal = self.find_by_id(goal_id)
        if goal:
            db.session.delete(goal)
            db.session.commit()
        return goal
    
    def find_by_id(self, goal_id):
        return PerformanceGoal.query.get(goal_id)
    
    def find_all(self):
        return PerformanceGoal.query.all()