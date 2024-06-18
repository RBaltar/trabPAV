from app import db
from app.models.model import WorkoutSession

class WorkoutSessionRepository:
    def create(self, date, duration, workout_type, intensity, athlete_id, calendar_id):
        workout_session = WorkoutSession(date=date, duration=duration, workout_type=workout_type,
                                     intensity=intensity, athlete_id=athlete_id, calendar_id=calendar_id)
        db.session.add(workout_session)
        db.session.commit()
        return workout_session

    def update(self, session_id, date=None, duration=None, workout_type=None, intensity=None, athlete_id=None, calendar_id=None):
        workout_session = self.find_by_id(session_id)
        if workout_session:
            if date:
                workout_session.date = date
            if duration:
                workout_session.duration = duration
            if workout_type:
                workout_session.workout_type = workout_type
            if intensity:
                workout_session.intensity = intensity
            if athlete_id:
                workout_session.athlete_id = athlete_id
            if calendar_id:
                workout_session.calendar_id = calendar_id
            db.session.commit()
        return workout_session

    def delete(self, session_id):
        workout_session = self.find_by_id(session_id)
        if workout_session:
            db.session.delete(workout_session)
            db.session.commit()
        return workout_session

    def find_by_id(self, session_id):
        return WorkoutSession.query.get(session_id)

    def find_all(self):
        return WorkoutSession.query.all()
