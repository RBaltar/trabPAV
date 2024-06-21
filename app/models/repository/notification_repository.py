from app import db
from app.models.model import Notification

class NotificationRepository:
    def create(self, athlete_id, type, message, date):
        notification = Notification(athlete_id=athlete_id, type=type, message=message, date=date)
        db.session.add(notification)
        db.session.commit()
        return notification
    
    def update(self, notification_id, athlete_id, type, message, date):
        notification = self.find_by_id(notification_id)
        if notification:
            if athlete_id:
                notification.athlete_id = athlete_id
            if type:
                notification.type = type
            if message:
                notification.message = message
            if date:
                notification.date = date
            db.session.commit(notification)
        return notification
    
    def delete(self, notification_id):
        notification = self.find_by_id(notification_id)
        if notification:
            db.session.delete(notification)
            db.session.commit()
        return notification

    def find_by_id(self, notification_id):
        return Notification.query.get(notification_id)
    
    def find_all(self):
        return Notification.query .all()