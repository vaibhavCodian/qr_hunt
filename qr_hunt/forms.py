from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from shitnet.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired()])
     submit = SubmitField('Login')

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from shitnet.models import User

