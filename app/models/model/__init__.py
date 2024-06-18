from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .athlete import Athlete
from .workout_session import WorkoutSession
from .performance_goal import PerformanceGoal
from .workout_feedback import WorkoutFeedback
from .performance_report import PerformanceReport
from .notification import Notification
from .messenger import Messenger
from .calendar import Calendar
from .analyze_performance import AnalyzePerformance
