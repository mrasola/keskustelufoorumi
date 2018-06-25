from sqlalchemy import text
from application import db
from application.models import Base


class User(Base):
    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    messages = db.relationship("Message", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def users_messages_number():
        stmt=text("SELECT Account.id, Account.username, COUNT(Message.id) FROM Account"
                  " LEFT JOIN Message ON Message.account_id = Account.id"
                  " GROUP BY Account.id ORDER BY COUNT(Message.id) DESC")
        res=db.engine.execute(stmt)

        response=[]
        i=0
        for row in res:
            response.append({"un": row[1], "ms": row[2]})
            i+=1
            if i==10: break

        return response