from repository.calendar_repository import CalendarRepository
from model.calendar import Calendar

class CalendarService:
    @staticmethod
    def get_all_calendars():
        return CalendarRepository.get_all()

    @staticmethod
    def get_calendar_by_id(calendar_id):
        return CalendarRepository.get_by_id(calendar_id)

    @staticmethod
    def create_calendar(data):
        new_calendar = Calendar(**data)
        CalendarRepository.create(new_calendar)
        return new_calendar

    @staticmethod
    def update_calendar(calendar_id, data):
        calendar = CalendarRepository.get_by_id(calendar_id)
        for key, value in data.items():
            setattr(calendar, key, value)
        CalendarRepository.update()
        return calendar

    @staticmethod
    def delete_calendar(calendar_id):
        calendar = CalendarRepository.get_by_id(calendar_id)
        CalendarRepository.delete(calendar)
