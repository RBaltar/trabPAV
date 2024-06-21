from repository.notification_repository import NotificationRepository
from model.notification import Notification

class NotificationService:
    @staticmethod
    def get_all_notifications():
        return NotificationRepository.get_all()

    @staticmethod
    def get_notification_by_id(notification_id):
        return NotificationRepository.get_by_id(notification_id)

    @staticmethod
    def create_notification(data):
        new_notification = Notification(**data)
        NotificationRepository.create(new_notification)
        return new_notification

    @staticmethod
    def update_notification(notification_id, data):
        notification = NotificationRepository.get_by_id(notification_id)
        for key, value in data.items():
            setattr(notification, key, value)
        NotificationRepository.update()
        return notification

    @staticmethod
    def delete_notification(notification_id):
        notification = NotificationRepository.get_by_id(notification_id)
        NotificationRepository.delete(notification)
