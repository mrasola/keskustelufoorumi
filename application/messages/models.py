from application import db
from application.models import Base

class Message(Base):
    subject = db.Column(db.String(144), nullable=False)
    body=db.Column(db.String(144), nullable=False)
    read = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, subject, body):
        self.subject = subject
        self.body = body
        self.read = False

#uusi liokka
class Category(Base):
    category=db.Column(db.String(144), nullable=False)
    description=db.Column(db.String(144), nullable=False)

    def __init__(self, c, d):
        self.category=c
        self.category=d