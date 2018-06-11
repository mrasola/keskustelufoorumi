from flask_wtf import FlaskForm
from application.messages.models import Category
from wtforms import StringField, validators, widgets
from wtforms import SelectMultipleField


class MessageForm(FlaskForm):
    subject = StringField("Subject", [validators.Length(min=3), validators.Length(max=40)])
    body = StringField("Message", [validators.Length(min=3), validators.Length(max=10000)])

    categories = SelectMultipleField("Categories", widget=widgets.ListWidget(prefix_label=True),
                                     option_widget=widgets.CheckboxInput())

    def set_choices(self):
        self.departments.choices = [(c.id, c.name) for c in Category.query.all()]

    class Meta:
        csrf = False
