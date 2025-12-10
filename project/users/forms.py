# project/users/forms.py 
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf.file import FileField, FileAllowed  

from flask_login import current_user
from project.models import User


# login form --------------------------------
class LoginForm(FlaskForm):
    email = StringField('Email *', validators=[DataRequired(), Email(message='Please enter a valid email address')])
    password = PasswordField('Password *', validators=[DataRequired()])
    submit = SubmitField('Login')



# registration form --------------------------------
class RegistrationForm(FlaskForm):
    first_name = StringField('First Name *', validators=[DataRequired()])
    last_name = StringField('Last Name *', validators=[DataRequired()])
    role = StringField('Profession/Role *', validators=[DataRequired()])
    location = StringField('Location *', validators=[DataRequired()])
    email = StringField('Email *', validators=[DataRequired(), Email(message='Please enter a valid email address')])
    username = StringField('Username *', validators=[DataRequired()])
    password = PasswordField('Password *', validators=[DataRequired(), EqualTo('conf_password', message='Passwords must match!')])
    conf_password = PasswordField('Confirm Password *', validators=[DataRequired()])
    submit = SubmitField('Sign Up')


# edit form --------------------------------
class EditAccountForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    role = StringField('Profession/Role', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    # email = StringField('Email', validators=[DataRequired(), Email(message='Please enter a valid email address')])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('New Password')
    bio = TextAreaField('About You', validators=[], render_kw={"rows": 4})
    picture = FileField('New Profile Image (JPG, JPEG, or PNG only)', validators=[FileAllowed(['jpg','png','jpeg'])])
    submit = SubmitField('Save')


    # def check_email(self, email):  # function to check if the email already exists in the db
    #    if User.query.filter_by(email=self.email.data).first():
    #        raise ValidationError('Email already has been registered')

    # def check_username(self, username):  # function to check if the username already exists in the db
    #    if User.query.filter_by(username=self.username.data).first():
    #        raise ValidationError('Username already has been registered')