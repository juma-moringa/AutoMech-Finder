from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    specialization =  TextAreaField('add your area of specialization.',validators = [Required()])
    location = SelectField(' Location', choices = [('Select your location','Select your location'),('busia','Busia'),('eldoret', 'Eldoret'), ('kisumu', 'Kisumu'),('nakuru','Nakuru'),('nairobi','Nairobi')], validators=[Required()])
    submit = SubmitField('Submit')

