from app import db
from app.models.model import WorkoutFeedback

class WorkoutFeedbackRepository:
    def create(self, session_id, rating, comment):
        feedback = WorkoutFeedback(session_id=session_id, rating=rating, comment=comment)
        db.session.add(feedback)
        db.session.commit()
        return feedback
    
    def update(self, feedback_id, session_id, rating, comment):
        feedback = self.find_by_id(feedback_id)
        if feedback:
            if session_id:
                feedback.session_id = session_id
            if rating:
                feedback.rating = rating
            if comment:
                feedback.comment = comment
            db.session.commit()
        return feedback
    
    def delete(self, feedback_id):
        feedback = self.find_by_id(feedback_id)
        if feedback:
            db.session.delete(feedback)
            db.session.commit()
        return feedback
    
    def find_by_id(self, feedback_id):
        return WorkoutFeedback.query.get(feedback_id)
    
    def find_all(self):
        return WorkoutFeedback.query.all()