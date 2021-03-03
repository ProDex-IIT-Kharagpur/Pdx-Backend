from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email
from wtforms import ValidationError


from flask_login import current_user
from website.models import User


class LoginForm(FlaskForm):
    email = StringField('Email: ', validators=[Email(), DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):

    name = StringField(label=None,validators=[DataRequired()])
    email = StringField(label=None, validators=[DataRequired(), Email()])
    username = StringField(label=None, validators=[DataRequired()])
    password = PasswordField(label=None, validators=[DataRequired(), EqualTo(
        'pass_confirm', message="Passwords must match!")])
    pass_confirm = PasswordField(
        'Confirm Password: ', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('Email has been already registered!')

    def validate_username(self, username):
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError('Username has been taken!')
