from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class Athlete(db.Model):
    __tablename__ = 'athletes'
    athlete_id = Column(Integer, primary_key=True)
    name = Column(String)
    birth_date = Column(Date)
    gender = Column(String)
    height = Column(Float)
    weight = Column(Float)
    trainer_id = Column(Integer, ForeignKey('users.user_id'))
    trainer = relationship('User', back_populates='athletes')
    training_sessions = relationship('TrainingSession', back_populates='athlete')
    performance_goals = relationship('PerformanceGoal', back_populates='athlete')
    calendar = relationship('Calendar', back_populates='athlete', uselist=False)
