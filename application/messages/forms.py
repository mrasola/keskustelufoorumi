from flask_wtf import FlaskForm
from application.categories.models import Category
from wtforms import StringField, validators, widgets, SelectMultipleField, TextAreaField


class MessageForm(FlaskForm):
    subject = StringField("Subject", [validators.Length(min=3), validators.Length(max=40)])
    body = TextAreaField("Message", [validators.Length(min=3), validators.Length(max=10000)])

    categories = SelectMultipleField("Categories", coerce=int,
                                     widget=widgets.ListWidget(prefix_label=True),
                                     option_widget=widgets.CheckboxInput())

    def __init__(self):
        super(MessageForm, self).__init__()
        self.categories.choices = [(c.id, c.name) for c in Category.query.all()]

    # def set_choices(self):
    #     self.categories.choices=[(c.id, c.name) for c in Category.query.all()]

    class Meta:
        csrf = False



