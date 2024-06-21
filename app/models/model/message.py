from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app import db

class Message(db.Model):
    __tablename__ = 'messages'
    message_id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('users.user_id'))
    recipient_id = Column(Integer, ForeignKey('users.user_id'))
    content = Column(String)
    date = Column(Date)
    sender = relationship('User', foreign_keys=[sender_id], back_populates='sent_messages')
    recipient = relationship('User', foreign_keys=[recipient_id], back_populates='received_messages')
