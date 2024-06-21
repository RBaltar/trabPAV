from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class Calendar(db.Model):
    __tablename__ = 'calendars'
    calendar_id = Column(Integer, primary_key=True)
    athlete_id = Column(Integer, ForeignKey('athletes.athlete_id'))
    athlete = relationship('Athlete', back_populates='calendar')
    events = relationship('TrainingSession', back_populates='calendar')
