from application import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    subject = db.Column(db.String(144), nullable=False)
    #body=db.Column(db.String(144), nullable=False)
    read = db.Column(db.Boolean, nullable=False)

    def __init__(self, subject):
        self.subject = subject
        #self.body=body
        self.read = False