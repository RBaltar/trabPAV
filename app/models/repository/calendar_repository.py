from model.calendar import Calendar
from app import db

class CalendarRepository:
    @staticmethod
    def get_all():
        return Calendar.query.all()

    @staticmethod
    def get_by_id(calendar_id):
        return Calendar.query.get(calendar_id)

    @staticmethod
    def create(calendar):
        db.session.add(calendar)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(calendar):
        db.session.delete(calendar)
        db.session.commit()
