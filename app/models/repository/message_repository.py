from model.message import Message
from app import db

class MessageRepository:
    @staticmethod
    def get_all():
        return Message.query.all()

    @staticmethod
    def get_by_id(message_id):
        return Message.query.get(message_id)

    @staticmethod
    def create(message):
        db.session.add(message)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(message):
        db.session.delete(message)
        db.session.commit()
