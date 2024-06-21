from repository.athlete_repository import AthleteRepository
from model.athlete import Athlete

class AthleteService:
    @staticmethod
    def get_all_athletes():
        return AthleteRepository.get_all()

    @staticmethod
    def get_athlete_by_id(athlete_id):
        return AthleteRepository.get_by_id(athlete_id)

    @staticmethod
    def create_athlete(data):
        new_athlete = Athlete(**data)
        AthleteRepository.create(new_athlete)
        return new_athlete

    @staticmethod
    def update_athlete(athlete_id, data):
        athlete = AthleteRepository.get_by_id(athlete_id)
        for key, value in data.items():
            setattr(athlete, key, value)
        AthleteRepository.update()
        return athlete

    @staticmethod
    def delete_athlete(athlete_id):
        athlete = AthleteRepository.get_by_id(athlete_id)
        AthleteRepository.delete(athlete)
