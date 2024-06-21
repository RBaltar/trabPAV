from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class PerformanceReport(db.Model):
    __tablename__ = 'performance_reports'
    report_id = Column(Integer, primary_key=True)
    athlete_id = Column(Integer, ForeignKey('athletes.athlete_id'))
    period = Column(String)
    performance = Column(String)
    athlete = relationship('Athlete', back_populates='performance_reports')
