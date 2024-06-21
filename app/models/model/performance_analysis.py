from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class PerformanceAnalysis(db.Model):
    __tablename__ = 'performance_analyses'
    analysis_id = Column(Integer, primary_key=True)
    athlete_id = Column(Integer, ForeignKey('athletes.athlete_id'))
    charts = Column(String)
    statistics = Column(String)
    athlete = relationship('Athlete', back_populates='performance_analyses')
