from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app import db

class User(db.Model):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    type = Column(String)  # Trainer, Athlete
    athletes = relationship('Athlete', back_populates='trainer')