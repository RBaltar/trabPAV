from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class PerformanceGoal(db.Model):
    __tablename__ = 'performance_goals'
    goal_id = Column(Integer, primary_key=True)
    description = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String)
    athlete_id = Column(Integer, ForeignKey('athletes.athlete_id'))
    athlete = relationship('Athlete', back_populates='performance_goals')
