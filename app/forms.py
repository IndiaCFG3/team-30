from flask_wtf import *
from flask_wtf.file import *
from flask_login import current_user
from wtforms import *
from wtforms.validators import *
from app.models import teacher, admin

class teacherRegistrationForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    
class adminRegistrationForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
  
# class AddteacherHistory(FlaskForm):
#     symptoms = StringField('Symptoms',
#                            validators=[DataRequired(), Length(min=2, max=200)]) 
#     diagnosis = StringField('Diagnosis',
#                            validators=[DataRequired(), Length(min=2, max=200)])
#     treatment = StringField('Treatment',
#                            validators=[DataRequired(), Length(min=2, max=200)])
#     otp_add = StringField('OTP', validators=[DataRequired])

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')


