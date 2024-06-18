from app.models.repository.user_repository import UserRepository

class UsuarioService:
    def __init__(self):
        self.repository = UserRepository()

    def create_user(self, name, email, password, role):
        return self.repository.create(name, email, password, role)

    def update_user(self, user_id, name=None, email=None, password=None, role=None):
        return self.repository.update(user_id, name, email, password, role)

    def delete_user(self, user_id):
        return self.repository.delete(user_id)

    def get_user_by_id(self, user_id):
        return self.repository.find_by_id(user_id)

    def get_all_user(self):
        return self.repository.find_all()
