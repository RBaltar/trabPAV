from app.models.service.calendar_service import CalendarService

class CalendarController:
    @staticmethod
    def get_all_calendars():
        return CalendarService.get_all_calendars()

    @staticmethod
    def get_calendar_by_id(calendar_id):
        return CalendarService.get_calendar_by_id(calendar_id)

    @staticmethod
    def create_calendar(data):
        return CalendarService.create_calendar(data)

    @staticmethod
    def update_calendar(calendar_id, data):
        return CalendarService.update_calendar(calendar_id, data)

    @staticmethod
    def delete_calendar(calendar_id):
        return CalendarService.delete_calendar(calendar_id)
