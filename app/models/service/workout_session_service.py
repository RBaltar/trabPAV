from app.models.repository.workout_session_repository import WorkoutSessionRepository

class SessaoTreinoService:
    def __init__(self):
        self.repository = WorkoutSessionRepository()

    def create_sessao_treino(self, date, duration, workout_type, intensity, athlete_id, calendar_id):
        return self.repository.create(date, duration, workout_type, intensity, athlete_id, calendar_id)

    def update_sessao_treino(self, session_id, date=None, duration=None, workout_type=None, intensity=None, athlete_id=None, calendar_id=None):
        return self.repository.update(session_id, date, duration, workout_type, intensity, athlete_id, calendar_id)

    def delete_sessao_treino(self, session_id):
        return self.repository.delete(session_id)

    def get_sessao_treino_by_id(self, session_id):
        return self.repository.find_by_id(session_id)

    def get_all_sessoes_treino(self):
        return self.repository.find_all()
