from app import db
from app.models.model import Messenger

class MessengerRepository:
    def create(self, sender_id, receiver_id, content, date):
        messenger = Messenger(sender_id=sender_id, receiver_id=receiver_id, content=content, date=date)
        db.session.add(messenger)
        db.session.commit()
        return messenger
    
    def update(self, messenger_id, sender_id=None, receiver_id=None, content=None, date=None):
        messenger = self.find_by_id(messenger_id)
        if messenger:
            if sender_id:
                messenger.sender_id = sender_id
            if receiver_id:
                messenger.receiver_id = receiver_id
            if content:
                messenger.content = content
            if date:
                messenger.date = date
            db.session.commit()
        return messenger
    
    def delete(self, messenger_id):
        messenger = self.find_by_id(messenger_id)
        if messenger:
            db.session.delete(messenger) 
            db.session.commit()
        return messenger
    
    def find_by_id(self, messenger_id):
        return Messenger.query.get(messenger_id)
    
    def find_all(self):
        return Messenger.query.all()