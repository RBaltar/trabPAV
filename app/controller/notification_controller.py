from app.models.service.notification_service import NotificationService

class NotificationController:
    @staticmethod
    def get_all_notifications():
        return NotificationService.get_all_notifications()

    @staticmethod
    def get_notification_by_id(notification_id):
        return NotificationService.get_notification_by_id(notification_id)

    @staticmethod
    def create_notification(data):
        return NotificationService.create_notification(data)

    @staticmethod
    def update_notification(notification_id, data):
        return NotificationService.update_notification(notification_id, data)

    @staticmethod
    def delete_notification(notification_id):
        return NotificationService.delete_notification(notification_id)
