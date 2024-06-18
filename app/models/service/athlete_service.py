from app.models.repository.athlete_repository import AthleteRepository

class AtletaService:
    def __init__(self):
        self.repository = AthleteRepository()

    def create_atleta(self, name, birth_date, gender, height, weight, coach_id):
        return self.repository.create(name, birth_date, gender, height, weight, coach_id)

    def update_atleta(self, athlete_id, name=None, birth_date=None, gender=None, height=None, weight=None, coach_id=None):
        return self.repository.update(athlete_id, name, birth_date, gender, height, weight, coach_id)

    def delete_atleta(self, athlete_id):
        return self.repository.delete(athlete_id)

    def get_atleta_by_id(self, athlete_id):
        return self.repository.find_by_id(athlete_id)

    def get_all_atletas(self):
        return self.repository.find_all()
