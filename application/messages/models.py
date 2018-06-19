from application import db
from application.models import Base

relation = db.Table("relation", db.Column('id', db.Integer, primary_key=True),
                    db.Column('category_id', db.Integer, db.ForeignKey('category.id', ondelete="cascade")),
                    db.Column('message_id', db.Integer, db.ForeignKey('message.id', ondelete="cascade")))


class Message(Base):
    subject = db.Column(db.String(144), nullable=False)
    body = db.Column(db.String(144), nullable=False)
    read = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    categories = db.relationship('Category', secondary=relation, lazy='subquery',
                                 backref=db.backref('message', lazy=True))

    def __init__(self, subject, body):
        self.subject = subject
        self.body = body
        self.read = False

