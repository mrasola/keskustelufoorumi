from application.models import Base
from application import db


class Category(Base):
    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=False)

    def __init__(self, n, d):
        self.name = n
        self.description = d