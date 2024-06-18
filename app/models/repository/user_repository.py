from app import db
from app.models.model import User

class UserRepository:
    def create(self, name, email, password, role):
        user = User(name=name, email=email, password=password, role=role)
        db.session.add(user)
        db.session.commit()
        return user
    
    def update(self, user_id, name=None, email=None, password=None, role=None):
        user=self.find_by_id(user_id)
        if user:
            if name:
                user.name = name
            if email:
                user.email = email
            if password:
                user.password = password
            if role:
                user.type = role
            db.session.commit()
        return user
    
    def delete(self, user_id):
        user = self.find_by_id(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
        return user
    
    def find_by_id(self, user_id):
        return User.query.get(user_id)
    
    def find_by_repository(self, password):
        return User.query.get(password)
    
    def find_all(self):
        return User.query.all()
    