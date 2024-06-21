from app import db
from app.models.model import Calendar

class CalendarRepository:
    def create(self, athlete_id, events):
        calendar = Calendar(athlete_id=athlete_id, events=events)
        db.session.add(calendar)
        db.session.commit()
        return calendar
    
    def update(self, calendar_id, athlete_id=None, events=None):
        calendar = self.find_by_id(calendar_id)
        if calendar:
            if athlete_id:
                calendar.athlete_id = athlete_id
            if events:
                calendar.events = events
            db.session.commit()
        return calendar
    
    def delete(self, calendar_id):
        calendar = self.find_by_id(calendar_id)
        if calendar:
            db.sessions.delete(calendar)
            db.sessions.commit()
        return calendar
    
    def find_by_id(self, calendar_id):
        return Calendar.query.get(calendar_id)
        
    def find_all(self):
        return Calendar.query.all()
        