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
  
class send_lectures_form(FlaskForm):
        link = StringField('lecture_link',
                           validators=[DataRequired(), Length(min=2, max=1000)]) 
        transcript = StringField('transcript',
                           validators=[DataRequired(), Length(min=2, max=100000)])

class send_assignments_form(FlaskForm):
        link = StringField('question',
                           validators=[DataRequired(), Length(min=2, max=1000)]) 
        transcript = StringField('answer',
                           validators=[DataRequired(), Length(min=2, max=100000)])

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')


