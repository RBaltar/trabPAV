from repository.user_repository import UserRepository
from model.user import User

class UserService:
    @staticmethod
    def get_all_users():
        return UserRepository.get_all()

    @staticmethod
    def get_user_by_id(user_id):
        return UserRepository.get_by_id(user_id)

    @staticmethod
    def create_user(data):
        new_user = User(**data)
        UserRepository.create(new_user)
        return new_user

    @staticmethod
    def update_user(user_id, data):
        user = UserRepository.get_by_id(user_id)
        for key, value in data.items():
            setattr(user, key, value)
        UserRepository.update()
        return user

    @staticmethod
    def delete_user(user_id):
        user = UserRepository.get_by_id(user_id)
        UserRepository.delete(user)
