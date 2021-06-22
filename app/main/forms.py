from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField,
                    SubmitField, SelectField)
from wtforms.validators import Required


class userForm(FlaskForm):
    first_name = StringField("First name")
    last_name = StringField("Last Name")
    queries = TextAreaField("Queries")
    email = StringField("Email")
    submit = SubmitField("submit")