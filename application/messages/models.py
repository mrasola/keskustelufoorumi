from application import db
from application.models import Base

categories = db.Table("categories",
                      db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True),
                      db.Column('message_id', db.Integer, db.ForeignKey('message.id'), primary_key=True)
                      )


class Message(Base):
    subject = db.Column(db.String(144), nullable=False)
    body = db.Column(db.String(144), nullable=False)
    read = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    categories = db.relationship('Category', secondary=categories, lazy='subquery',
                                 backref=db.backref('messages', lazy=True))

    def __init__(self, subject, body):
        self.subject = subject
        self.body = body
        self.read = False


class Category(Base):
    category = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=False)

    def __init__(self, c, d):
        self.category = c
        self.description = d
