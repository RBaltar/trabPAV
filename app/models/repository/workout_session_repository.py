from model.workout_session import WorkoutSession
from app import db

class WorkoutSessionRepository:
    @staticmethod
    def get_all():
        return WorkoutSession.query.all()

    @staticmethod
    def get_by_id(session_id):
        return WorkoutSession.query.get(session_id)

    @staticmethod
    def create(workout_session):
        db.session.add(workout_session)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(workout_session):
        db.session.delete(workout_session)
        db.session.commit()

    @staticmethod
    def get_sessions_by_athlete_id(athlete_id):
        return WorkoutSession.query.filter_by(athlete_id=athlete_id).all()
    
    @staticmethod
    def get_frequency_by_athlete_id(athlete_id):
        return WorkoutSession.query.filter_by(athlete_id=athlete_id).all()