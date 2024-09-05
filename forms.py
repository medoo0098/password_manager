from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, ValidationError
from models import User, SiteEntry



class RegisterForm(FlaskForm):

    username = StringField("Username :", validators = [InputRequired(message:="username must be entered") ], render_kw={"class":"form-control"})
    password = PasswordField("Password : ", validators= [InputRequired(message:="password must be provided")], render_kw={"class":"form-control"})
    submit = SubmitField("Register", render_kw={"class":"btn btn-primary"})

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user != None:
            raise ValidationError("Username Exist")