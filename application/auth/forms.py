from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False


class RegistrationForm(FlaskForm):
    name=StringField("Name")
    username = StringField("Username", [validators.Length(min=4), validators.Length(max=15)])
    password = PasswordField("Password", [validators.Length(min=6), validators.Length(max=20)])
    pw2 = PasswordField("Repeat password", [validators.equal_to("password",
                        message="Passwords did not match! Try again!")])

    class Meta:
        csrf = False
