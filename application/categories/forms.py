from flask_wtf import FlaskForm
from wtforms import StringField, validators, TextAreaField


class CategoryForm(FlaskForm):
    name=StringField("Category name", [validators.Length(min=3), validators.Length(max=40)])
    description=TextAreaField("Description", [validators.Length(min=3), validators.Length(max=40)])

    class Meta:
        csrf=False