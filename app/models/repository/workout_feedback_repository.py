from model.workout_feedback import WorkoutFeedback
from app import db

class WorkoutFeedbackRepository:
    @staticmethod
    def get_all():
        return WorkoutFeedback.query.all()

    @staticmethod
    def get_by_id(feedback_id):
        return WorkoutFeedback.query.get(feedback_id)

    @staticmethod
    def create(workout_feedback):
        db.session.add(workout_feedback)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(workout_feedback):
        db.session.delete(workout_feedback)
        db.session.commit()
