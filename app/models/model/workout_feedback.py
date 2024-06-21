from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class WorkoutFeedback(db.Model):
    __tablename__ = 'workout_feedbacks'
    feedback_id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey('training_sessions.session_id'))
    evaluation = Column(String)
    comment = Column(String)
    session = relationship('TrainingSession', back_populates='feedbacks')
