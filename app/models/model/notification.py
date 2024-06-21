from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app import db

class Notification(db.Model):
    __tablename__ = 'notifications'
    notification_id = Column(Integer, primary_key=True)
    athlete_id = Column(Integer, ForeignKey('athletes.athlete_id'))
    type = Column(String)
    message = Column(String)
    date = Column(Date)
    athlete = relationship('Athlete', back_populates='notifications')
