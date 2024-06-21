from app.models.service.message_service import MessageService

class MessageController:
    @staticmethod
    def get_all_messages():
        return MessageService.get_all_messages()

    @staticmethod
    def get_message_by_id(message_id):
        return MessageService.get_message_by_id(message_id)

    @staticmethod
    def create_message(data):
        return MessageService.create_message(data)

    @staticmethod
    def update_message(message_id, data):
        return MessageService.update_message(message_id, data)

    @staticmethod
    def delete_message(message_id):
        return MessageService.delete_message(message_id)
