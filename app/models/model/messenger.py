from . import db

class Messenger(db.Model):
    """Class representing a messenger in the system."""
    __tablename__ = 'messengers'
    messenger_id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    content = db.Column(db.String)
    date = db.Column(db.Date)
