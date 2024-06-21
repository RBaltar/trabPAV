from repository.message_repository import MessageRepository
from model.message import Message

class MessageService:
    @staticmethod
    def get_all_messages():
        return MessageRepository.get_all()

    @staticmethod
    def get_message_by_id(message_id):
        return MessageRepository.get_by_id(message_id)

    @staticmethod
    def create_message(data):
        new_message = Message(**data)
        MessageRepository.create(new_message)
        return new_message

    @staticmethod
    def update_message(message_id, data):
        message = MessageRepository.get_by_id(message_id)
        for key, value in data.items():
            setattr(message, key, value)
        MessageRepository.update()
        return message

    @staticmethod
    def delete_message(message_id):
        message = MessageRepository.get_by_id(message_id)
        MessageRepository.delete(message)
