from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from FlaskBlog.models import User

class RegistrstionForm(FlaskForm):
    username=StringField("Username", validators=[DataRequired(), Length(min=2, max=30)])
    email=StringField("Email", validators=[DataRequired(), Email()])
    password=PasswordField("Password", validators=[DataRequired()])
    confirmpassword=PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit=SubmitField("Sign up")

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username already exists')


    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email already exists')

class LoginForm(FlaskForm):
    email=StringField("Email", validators=[DataRequired(), Email()])
    password=PasswordField("Password", validators=[DataRequired()])
    submit=SubmitField("Sign in")

class PostForm(FlaskForm):
    title=StringField("Title", validators=[DataRequired()])
    description=TextAreaField("description", validators=[DataRequired()])
    submit=SubmitField("Post")



