from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField, EmailField,SelectField, DateTimeField, DateField, TimeField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, ValidationError
from models import User



class RegisterForm(FlaskForm):

    username = StringField("Username :", validators = [InputRequired(message:="username must be entered") ], render_kw={"class":"form-control"})
    email = EmailField("Email : ", validators=[InputRequired(message="Email is required")], render_kw={"class":"form-control"})
    password = PasswordField("Password : ", validators= [InputRequired(message:="password must be provided")], render_kw={"class":"form-control"})
    admin = BooleanField("Admin",default="")
    manager = BooleanField("Manager", default="")
    department = SelectField("Department", choices=["Sales", "Administration", "Technical", "General Manager"])
    submit = SubmitField("Register", render_kw={"class":"btn btn-warning"})


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user != None:
            raise ValidationError("Username Exist")
        


class LoginForm(FlaskForm):

    username = StringField("Username", validators=[InputRequired(message="Username must be entered")])
    password = StringField("Password", validators=[InputRequired(message="Password must be provided")])
    submit = SubmitField("Log in", render_kw={"class":"btn btn-warning"})
    


class LeaveForm(FlaskForm):

    start_date = DateField("Starting Time")
    start_time = TimeField("What Time")
    return_date = DateField("Return Time")
    reason = SelectField("Reason", choices=["Personal Day", "Medical"])
    submit = SubmitField("Submit for approval", render_kw={"class":"btn btn-warning"})
