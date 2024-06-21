from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class WorkoutSession(db.Model):
    __tablename__ = 'workout_sessions'
    session_id = Column(Integer, primary_key=True)
    date = Column(Date)
    duration = Column(Integer)
    training_type = Column(String)
    intensity = Column(String)
    athlete_id = Column(Integer, ForeignKey('athletes.athlete_id'))
    athlete = relationship('Athlete', back_populates='training_sessions')
    feedbacks = relationship('WorkoutFeedback', back_populates='session')
    calendar_id = Column(Integer, ForeignKey('calendars.calendar_id'))
    calendar = relationship('Calendar', back_populates='events')
