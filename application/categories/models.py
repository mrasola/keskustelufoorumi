from sqlalchemy import text
from application.models import Base
from application import db


class Category(Base):
    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=False)

    def __init__(self, n, d):
        self.name = n
        self.description = d

    @staticmethod
    def category_message_number():
        stmt=text("SELECT Category.id, Category.name, COUNT(message_id) FROM Relation"
                  " INNER JOIN Category ON Category.id = Relation.category_id"
                  " GROUP BY Category.id ORDER BY COUNT(message_id) DESC")
        res=db.engine.execute(stmt)

        response=[]
        i=0
        for row in res:
            response.append({"cat": row[1], "ms": row[2]})
            i+=1
            if i==10: break

        return response