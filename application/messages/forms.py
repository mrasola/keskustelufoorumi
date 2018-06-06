from flask_wtf import FlaskForm
from wtforms import StringField, validators


class MessageForm(FlaskForm):
    subject = StringField("Subject", [validators.Length(min=3), validators.Length(max=40)])
    body=StringField("Message", [validators.Length(min=3), validators.Length(max=10000)])

    class Meta:
        csrf = False