from app import db
from app.models.model import Athlete

class AthleteRepository:
    def create(self, name, birth_date, gender, height, weight, coach_id):
        athlete = Athlete(name=name, birth_date=birth_date, gender=gender,
                        height=height, weight=weight, coach_id=coach_id)
        db.session.add(athlete)
        db.session.commit()
        return athlete

    def update(self, athlete_id, name=None, birth_date=None, gender=None, height=None, weight=None, coach_id=None):
        athlete = self.find_by_id(athlete_id)
        if athlete:
            if name:
                athlete.name = name
            if birth_date:
                athlete.birth_date = birth_date
            if gender:
                athlete.gender = gender
            if height:
                athlete.height = height
            if weight:
                athlete.weight = weight
            if coach_id:
                athlete.coach_id = coach_id
            db.session.commit()
        return athlete

    def delete(self, athlete_id):
        athlete = self.find_by_id(athlete_id)
        if athlete:
            db.session.delete(athlete)
            db.session.commit()
        return athlete

    def find_by_id(self, athlete_id):
        return Athlete.query.get(athlete_id)

    def find_all(self):
        return Athlete.query.all()