from app.models.service.workout_session_service import WorkoutSessionService

class WorkoutSessionController:
    @staticmethod
    def get_all_sessions():
        return WorkoutSessionService.get_all_sessions()

    @staticmethod
    def get_session_by_id(session_id):
        return WorkoutSessionService.get_session_by_id(session_id)

    @staticmethod
    def create_session(data):
        return WorkoutSessionService.create_session(data)

    @staticmethod
    def update_session(session_id, data):
        return WorkoutSessionService.update_session(session_id, data)

    @staticmethod
    def delete_session(session_id):
        return WorkoutSessionService.delete_session(session_id)

    @staticmethod
    def get_sessions_by_athlete(athlete_id):
        return WorkoutSessionService.get_sessions_by_athlete(athlete_id)
    
    @staticmethod
    def get_workout_frequency(athlete_id):
        return WorkoutSessionService.get_workout_frequency(athlete_id)