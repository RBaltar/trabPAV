from repository.workout_session_repository import WorkoutSessionRepository
from model.workout_session import WorkoutSession

class WorkoutSessionService:
    @staticmethod
    def get_all_sessions():
        return WorkoutSessionRepository.get_all()

    @staticmethod
    def get_session_by_id(session_id):
        return WorkoutSessionRepository.get_by_id(session_id)

    @staticmethod
    def create_session(data):
        new_session = WorkoutSession(**data)
        WorkoutSessionRepository.create(new_session)
        return new_session

    @staticmethod
    def update_session(session_id, data):
        session = WorkoutSessionRepository.get_by_id(session_id)
        for key, value in data.items():
            setattr(session, key, value)
        WorkoutSessionRepository.update()
        return session

    @staticmethod
    def delete_session(session_id):
        session = WorkoutSessionRepository.get_by_id(session_id)
        WorkoutSessionRepository.delete(session)

    @staticmethod
    def get_sessions_by_athlete(athlete_id):
        return WorkoutSessionRepository.get_sessions_by_athlete_id(athlete_id)
    
    @staticmethod
    def get_workout_frequency(athlete_id):
        sessions = WorkoutSessionRepository.get_frequency_by_athlete_id(athlete_id)
        frequency = len(sessions)  # Assuming frequency is the count of sessions
        return {'athlete_id': athlete_id, 'workout_frequency': frequency}
