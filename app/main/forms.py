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


class queriesForm(FlaskForm):
      """
      Class to create a wtf form for adding a car defect
      """
      query = TextAreaField('Car Defect:')
      submit = SubmitField('SUBMIT')
