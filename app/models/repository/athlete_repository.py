from model.athlete import Athlete
from app import db

class AthleteRepository:
    @staticmethod
    def get_all():
        return Athlete.query.all()

    @staticmethod
    def get_by_id(athlete_id):
        return Athlete.query.get(athlete_id)

    @staticmethod
    def create(athlete):
        db.session.add(athlete)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(athlete):
        db.session.delete(athlete)
        db.session.commit()
