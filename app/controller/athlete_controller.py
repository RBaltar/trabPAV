from app.models.service.athlete_service import AthleteService

class AthleteController:
    @staticmethod
    def get_all_athletes():
        return AthleteService.get_all_athletes()

    @staticmethod
    def get_athlete_by_id(athlete_id):
        return AthleteService.get_athlete_by_id(athlete_id)

    @staticmethod
    def create_athlete(data):
        return AthleteService.create_athlete(data)

    @staticmethod
    def update_athlete(athlete_id, data):
        return AthleteService.update_athlete(athlete_id, data)

    @staticmethod
    def delete_athlete(athlete_id):
        return AthleteService.delete_athlete(athlete_id)
