from app.models.service.user_service import UserService

class UserController:
    @staticmethod
    def get_all_users():
        return UserService.get_all_users()

    @staticmethod
    def get_user_by_id(user_id):
        return UserService.get_user_by_id(user_id)

    @staticmethod
    def create_user(data):
        return UserService.create_user(data)

    @staticmethod
    def update_user(user_id, data):
        return UserService.update_user(user_id, data)

    @staticmethod
    def delete_user(user_id):
        return UserService.delete_user(user_id)
