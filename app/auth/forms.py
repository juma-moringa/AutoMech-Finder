from flask_wtf import FlaskForm
<<<<<<< HEAD
=======
from wtforms.fields.core import SelectField
>>>>>>> ee0fed771167e23d4f5d42c7c081928b082b0965
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError
from wtforms import StringField, PasswordField, BooleanField,SubmitField


# registering the users

class RegistrationForm(FlaskForm):
<<<<<<< HEAD
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
=======
   
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
    telephone = StringField('Telephone no:')
    location = StringField('Location')
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')

    #validators`
    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an existing account with that email')
    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError(' OOOPS!!!! That username is taken')


#creating the user-login form

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
    


# ################### registering the admin/mechanic

class RegistrationForm2(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
    location = SelectField(' Location', choices = [('Select your location','Select your location'),('busia','Busia'),('eldoret', 'Eldoret'), ('kisumu', 'Kisumu'),('nakuru','Nakuru'),('nairobi','Nairobi')], validators=[Required()])
    specialization= SelectField(' Service', choices = [('Select Area specialized in','Select Area specialized in'),('break','Break repairs'),('wheel', 'Wheel Alignment'), ('puncture', 'Puncture'),('exhaust','Exhaust repairs'),('engine','Engine diagnostics')], validators=[Required()])
>>>>>>> ee0fed771167e23d4f5d42c7c081928b082b0965
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')

    #validators
    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an existing account with that email')
    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError(' OOOPS!!!! That username is taken')


#creating the login form

<<<<<<< HEAD
class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
=======
class LoginForm2(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
    
>>>>>>> ee0fed771167e23d4f5d42c7c081928b082b0965
