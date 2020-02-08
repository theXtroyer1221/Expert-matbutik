from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField


class SignUpForm(FlaskForm):
    name = StringField("name")
    mail = StringField("mail")
    message = TextAreaField("message")
    submit = SubmitField("submit")