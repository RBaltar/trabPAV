from model.notification import Notification
from app import db

class NotificationRepository:
    @staticmethod
    def get_all():
        return Notification.query.all()

    @staticmethod
    def get_by_id(notification_id):
        return Notification.query.get(notification_id)

    @staticmethod
    def create(notification):
        db.session.add(notification)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(notification):
        db.session.delete(notification)
        db.session.commit()
