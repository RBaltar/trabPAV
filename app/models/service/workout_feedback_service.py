from repository.workout_feedback_repository import WorkoutFeedbackRepository
from model.workout_feedback import WorkoutFeedback

class WorkoutFeedbackService:
    @staticmethod
    def get_all_feedbacks():
        return WorkoutFeedbackRepository.get_all()

    @staticmethod
    def get_feedback_by_id(feedback_id):
        return WorkoutFeedbackRepository.get_by_id(feedback_id)

    @staticmethod
    def create_feedback(data):
        new_feedback = WorkoutFeedback(**data)
        WorkoutFeedbackRepository.create(new_feedback)
        return new_feedback

    @staticmethod
    def update_feedback(feedback_id, data):
        feedback = WorkoutFeedbackRepository.get_by_id(feedback_id)
        for key, value in data.items():
            setattr(feedback, key, value)
        WorkoutFeedbackRepository.update()
        return feedback

    @staticmethod
    def delete_feedback(feedback_id):
        feedback = WorkoutFeedbackRepository.get_by_id(feedback_id)
        WorkoutFeedbackRepository.delete(feedback)
