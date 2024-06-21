"""app.py"""

from flask import Flask
from flask_restful import Api, Resource
from config import Config
from app.extensions import db
from app.controller.user_controller import UserController
from app.controller.athlete_controller import AthleteController
from app.controller.performance_analysis_controller import PerformanceAnalysisController
from app.controller.calendar_controller import CalendarController
from app.controller.message_controller import MessageController
from app.controller.notification_controller import NotificationController
from app.controller.performance_goal_controller import PerformanceGoalController
from app.controller.performance_report_controller import PerformanceReportController
from app.controller.workout_feedback_controller import WorkoutFeedbackController
from app.controller.workout_session_controller import WorkoutSessionController

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

db.init_db(app)

class UserListResource(Resource):
    """
    Resource for handling requests related to the list of users.
    """
    def get(self):
        """Get all users."""
        return UserController.get_all_users()

    def post(self):
        """Create a new user."""
        return UserController.create_user(self)

class UserResource(Resource):
    """
    Resource for handling requests related to a single user.
    """
    def get(self, user_id):
        """Get user by ID."""
        return UserController.get_user_by_id(user_id)

    def put(self, user_id):
        """Update user by ID."""
        return UserController.update_user(self, user_id)

    def delete(self, user_id):
        """Delete user by ID."""
        return UserController.delete_user(user_id)

class AthleteListResource(Resource):
    """
    Resource for handling requests related to the list of athletes.
    """
    def get(self):
        """Get all athletes."""
        return AthleteController.get_all_athletes()

    def post(self):
        """Create a new athlete."""
        return AthleteController.create_athlete(self)

class AthleteResource(Resource):
    """
    Resource for handling requests related to a single athlete.
    """
    def get(self, athlete_id):
        """Get athlete by ID."""
        return AthleteController.get_athlete_by_id(athlete_id)

    def put(self, athlete_id):
        """Update athlete by ID."""
        return AthleteController.update_athlete(self, athlete_id)

    def delete(self, athlete_id):
        """Delete athlete by ID."""
        return AthleteController.delete_athlete(athlete_id)

class PerformanceAnalysisListResource(Resource):
    """
    Resource for handling requests related to the list of performance analyses.
    """
    def get(self):
        """Get all performance analyses."""
        return PerformanceAnalysisController.get_all_analyses()

    def post(self):
        """Create a new performance analysis."""
        return PerformanceAnalysisController.create_analysis(self)

class PerformanceAnalysisResource(Resource):
    """
    Resource for handling requests related to a single performance analysis.
    """
    def get(self, analysis_id):
        """Get performance analysis by ID."""
        return PerformanceAnalysisController.get_analysis_by_id(analysis_id)

    def put(self, analysis_id):
        """Update performance analysis by ID."""
        return PerformanceAnalysisController.update_analysis(self, analysis_id)

    def delete(self, analysis_id):
        """Delete performance analysis by ID."""
        return PerformanceAnalysisController.delete_analysis(analysis_id)

class CalendarListResource(Resource):
    """
    Resource for handling requests related to the list of calendars.
    """
    def get(self):
        """Get all calendars."""
        return CalendarController.get_all_calendars()

    def post(self):
        """Create a new calendar."""
        return CalendarController.create_calendar(self)

class CalendarResource(Resource):
    """
    Resource for handling requests related to a single calendar.
    """
    def get(self, calendar_id):
        """Get calendar by ID."""
        return CalendarController.get_calendar_by_id(calendar_id)

    def put(self, calendar_id):
        """Update calendar by ID."""
        return CalendarController.update_calendar(self, calendar_id)

    def delete(self, calendar_id):
        """Delete calendar by ID."""
        return CalendarController.delete_calendar(calendar_id)

class MessageListResource(Resource):
    """
    Resource for handling requests related to the list of messages.
    """
    def get(self):
        """Get all messages."""
        return MessageController.get_all_messages()

    def post(self):
        """Create a new message."""
        return MessageController.create_message(self)

class MessageResource(Resource):
    """
    Resource for handling requests related to a single message.
    """
    def get(self, message_id):
        """Get message by ID."""
        return MessageController.get_message_by_id(message_id)

    def put(self, message_id):
        """Update message by ID."""
        return MessageController.update_message(self, message_id)

    def delete(self, message_id):
        """Delete message by ID."""
        return MessageController.delete_message(message_id)

class NotificationListResource(Resource):
    """
    Resource for handling requests related to the list of notifications.
    """
    def get(self):
        """Get all notifications."""
        return NotificationController.get_all_notifications()

    def post(self):
        """Create a new notification."""
        return NotificationController.create_notification(self)

class NotificationResource(Resource):
    """
    Resource for handling requests related to a single notification.
    """
    def get(self, notification_id):
        """Get notification by ID."""
        return NotificationController.get_notification_by_id(notification_id)

    def put(self, notification_id):
        """Update notification by ID."""
        return NotificationController.update_notification(self, notification_id)

    def delete(self, notification_id):
        """Delete notification by ID."""
        return NotificationController.delete_notification(notification_id)

class PerformanceGoalListResource(Resource):
    """
    Resource for handling requests related to the list of performance goals.
    """
    def get(self):
        """Get all performance goals."""
        return PerformanceGoalController.get_all_goals()

    def post(self):
        """Create a new performance goal."""
        return PerformanceGoalController.create_goal(self)

class PerformanceGoalResource(Resource):
    """
    Resource for handling requests related to a single performance goal.
    """
    def get(self, goal_id):
        """Get performance goal by ID."""
        return PerformanceGoalController.get_goal_by_id(goal_id)

    def put(self, goal_id):
        """Update performance goal by ID."""
        return PerformanceGoalController.update_goal(self, goal_id)

    def delete(self, goal_id):
        """Delete performance goal by ID."""
        return PerformanceGoalController.delete_goal(goal_id)

class PerformanceReportListResource(Resource):
    """
    Resource for handling requests related to the list of performance reports.
    """
    def get(self):
        """Get all performance reports."""
        return PerformanceReportController.get_all_reports()

    def post(self):
        """Create a new performance report."""
        return PerformanceReportController.create_report(self)

class PerformanceReportResource(Resource):
    """
    Resource for handling requests related to a single performance report.
    """
    def get(self, report_id):
        """Get performance report by ID."""
        return PerformanceReportController.get_report_by_id(report_id)

    def put(self, report_id):
        """Update performance report by ID."""
        return PerformanceReportController.update_report(self, report_id)

    def delete(self, report_id):
        """Delete performance report by ID."""
        return PerformanceReportController.delete_report(report_id)

class WorkoutFeedbackListResource(Resource):
    """
    Resource for handling requests related to the list of workout feedbacks.
    """
    def get(self):
        """Get all workout feedbacks."""
        return WorkoutFeedbackController.get_all_feedbacks()

    def post(self):
        """Create a new workout feedback."""
        return WorkoutFeedbackController.create_feedback(self)

class WorkoutFeedbackResource(Resource):
    """
    Resource for handling requests related to a single workout feedback.
    """
    def get(self, feedback_id):
        """Get workout feedback by ID."""
        return WorkoutFeedbackController.get_feedback_by_id(feedback_id)

    def put(self, feedback_id):
        """Update workout feedback by ID."""
        return WorkoutFeedbackController.update_feedback(self, feedback_id)

    def delete(self, feedback_id):
        """Delete workout feedback by ID."""
        return WorkoutFeedbackController.delete_feedback(feedback_id)

class WorkoutSessionListResource(Resource):
    """
    Resource for handling requests related to the list of workout sessions.
    """
    def get(self):
        """Get all workout sessions."""
        return WorkoutSessionController.get_all_sessions()

    def post(self):
        """Create a new workout session."""
        return WorkoutSessionController.create_session(self)

class WorkoutSessionResource(Resource):
    """
    Resource for handling requests related to a single workout session.
    """
    def get(self, session_id):
        """Get workout session by ID."""
        return WorkoutSessionController.get_session_by_id(session_id)

    def put(self, session_id):
        """Update workout session by ID."""
        return WorkoutSessionController.update_session(self, session_id)

    def delete(self, session_id):
        """Delete workout session by ID."""
        return WorkoutSessionController.delete_session(session_id)

class AthleteWorkoutSessionsResource(Resource):
    """
    Resource for handling requests related to the workout sessions of a specific athlete.
    """
    def get(self, athlete_id):
        """Get all workout sessions for a specific athlete."""
        return WorkoutSessionController.get_sessions_by_athlete(athlete_id)

class AthleteWorkoutFrequencyResource(Resource):
    """
    Resource for handling requests related to the workout frequency of a specific athlete.
    """
    def get(self, athlete_id):
        """Get workout frequency for a specific athlete."""
        return WorkoutSessionController.get_workout_frequency(athlete_id)

api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(AthleteListResource, '/athletes')
api.add_resource(AthleteResource, '/athletes/<int:athlete_id>')
api.add_resource(PerformanceAnalysisListResource, '/performance_analyses')
api.add_resource(PerformanceAnalysisResource, '/performance_analyses/<int:analysis_id>')
api.add_resource(CalendarListResource, '/calendars')
api.add_resource(CalendarResource, '/calendars/<int:calendar_id>')
api.add_resource(MessageListResource, '/messages')
api.add_resource(MessageResource, '/messages/<int:message_id>')
api.add_resource(NotificationListResource, '/notifications')
api.add_resource(NotificationResource, '/notifications/<int:notification_id>')
api.add_resource(PerformanceGoalListResource, '/performance_goals')
api.add_resource(PerformanceGoalResource, '/performance_goals/<int:goal_id>')
api.add_resource(PerformanceReportListResource, '/performance_reports')
api.add_resource(PerformanceReportResource, '/performance_reports/<int:report_id>')
api.add_resource(WorkoutFeedbackListResource, '/workout_feedbacks')
api.add_resource(WorkoutFeedbackResource, '/workout_feedbacks/<int:feedback_id>')
api.add_resource(WorkoutSessionListResource, '/workout_sessions')
api.add_resource(WorkoutSessionResource, '/workout_sessions/<int:session_id>')
api.add_resource(AthleteWorkoutSessionsResource, '/athletes/<int:athlete_id>/workout_sessions')
api.add_resource(AthleteWorkoutFrequencyResource, '/athletes/<int:athlete_id>/workout_frequency')

if __name__ == '__main__':
    app.run(debug=True)
