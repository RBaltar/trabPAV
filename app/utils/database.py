"""
This module defines the database structure and data model classes for an athlete training management
application using SQLAlchemy and PostgreSQL.
"""

from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

class User(Base):
    """Class representing a user in the system."""
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    type = Column(String)  # Trainer, Athlete
    athletes = relationship('Athlete', back_populates='trainer')

class Athlete(Base):
    """Class representing an athlete in the system."""
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

class TrainingSession(Base):
    """Class representing a training session in the system."""
    __tablename__ = 'training_sessions'
    session_id = Column(Integer, primary_key=True)
    date = Column(Date)
    duration = Column(Integer)
    training_type = Column(String)
    intensity = Column(String)
    athlete_id = Column(Integer, ForeignKey('athletes.athlete_id'))
    athlete = relationship('Athlete', back_populates='training_sessions')
    feedbacks = relationship('TrainingFeedback', back_populates='session')
    calendar_id = Column(Integer, ForeignKey('calendars.calendar_id'))
    calendar = relationship('Calendar', back_populates='events')

class PerformanceGoal(Base):
    """Class representing a performance goal in the system."""
    __tablename__ = 'performance_goals'
    goal_id = Column(Integer, primary_key=True)
    description = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String)
    athlete_id = Column(Integer, ForeignKey('athletes.athlete_id'))
    athlete = relationship('Athlete', back_populates='performance_goals')

class TrainingFeedback(Base):
    """Class representing a training feedback in the system."""
    __tablename__ = 'training_feedbacks'
    feedback_id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey('training_sessions.session_id'))
    evaluation = Column(String)
    comment = Column(String)
    session = relationship('TrainingSession', back_populates='feedbacks')

class PerformanceReport(Base):
    """Class representing a performance report in the system."""
    __tablename__ = 'performance_reports'
    report_id = Column(Integer, primary_key=True)
    athlete_id = Column(Integer, ForeignKey('athletes.athlete_id'))
    period = Column(String)
    performance = Column(String)

class Notification(Base):
    """Class representing a notification in the system."""
    __tablename__ = 'notifications'
    notification_id = Column(Integer, primary_key=True)
    athlete_id = Column(Integer, ForeignKey('athletes.athlete_id'))
    type = Column(String)
    message = Column(String)
    date = Column(Date)

class Message(Base):
    """Class representing a message in the system."""
    __tablename__ = 'messages'
    message_id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('users.user_id'))
    recipient_id = Column(Integer, ForeignKey('users.user_id'))
    content = Column(String)
    date = Column(Date)

class Calendar(Base):
    """Class representing a calendar in the system."""
    __tablename__ = 'calendars'
    calendar_id = Column(Integer, primary_key=True)
    athlete_id = Column(Integer, ForeignKey('athletes.athlete_id'))
    athlete = relationship('Athlete', back_populates='calendar')
    events = relationship('TrainingSession', back_populates='calendar')

class PerformanceAnalysis(Base):
    """Class representing a performance analysis in the system."""
    __tablename__ = 'performance_analyses'
    analysis_id = Column(Integer, primary_key=True)
    athlete_id = Column(Integer, ForeignKey('athletes.athlete_id'))
    charts = Column(String)
    statistics = Column(String)

# Configure the SQLAlchemy engine for PostgreSQL
engine = create_engine('postgresql://your_user:password@localhost/database_name', echo=True)

# Create all tables
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Example of inserting data
new_user = User(name='João', email='joao@example.com', password='1234', type='Trainer')
session.add(new_user)
session.commit()
