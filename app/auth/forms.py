from flask_wtf import FlaskForm
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError
from wtforms import StringField, PasswordField, BooleanField,SubmitField


# registering the users

class RegistrationForm(FlaskForm):
   

    username = StringField('Enter your username',validators = [Required()])
    email = StringField('Your Email Address',validators=[Required(),Email()])
    telephone = StringField('Telephone no:')
    location = StringField('Location')
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

class LoginForm2(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
    