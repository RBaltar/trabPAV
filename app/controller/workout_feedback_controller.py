from app.models.service.workout_feedback_service import WorkoutFeedbackService

class WorkoutFeedbackController:
    @staticmethod
    def get_all_feedbacks():
        return WorkoutFeedbackService.get_all_feedbacks()

    @staticmethod
    def get_feedback_by_id(feedback_id):
        return WorkoutFeedbackService.get_feedback_by_id(feedback_id)

    @staticmethod
    def create_feedback(data):
        return WorkoutFeedbackService.create_feedback(data)

    @staticmethod
    def update_feedback(feedback_id, data):
        return WorkoutFeedbackService.update_feedback(feedback_id, data)

    @staticmethod
    def delete_feedback(feedback_id):
        return WorkoutFeedbackService.delete_feedback(feedback_id)
