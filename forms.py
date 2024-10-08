from wtforms import (StringField, PasswordField, SubmitField, TextAreaField, 
                     BooleanField, SelectMultipleField, EmailField,SelectField, 
                     DateTimeField, DateField, TimeField, URLField, 
                     IntegerField, FloatField)
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, ValidationError
from models import User



class RegisterForm(FlaskForm):

    username = StringField("Username :", 
        validators = [InputRequired(message:="username must be entered") ], 
        render_kw={"class":"form-control"})
    email = EmailField("Email : ", 
        validators=[InputRequired(message="Email is required")], 
        render_kw={"class":"form-control"})
    password = PasswordField("Password : ", 
        validators= [InputRequired(message:="password must be provided")], 
        render_kw={"class":"form-control"})
    admin = BooleanField("Admin",default=False)
    manager = BooleanField("Manager", default=False)
    department = SelectField("Department", 
        choices=["Sales", "Administration", "Technical", "General Manager"])
    submit = SubmitField("Register", render_kw={"class":"btn btn-warning"})


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user != None:
            raise ValidationError("Username Exist")
        


class LoginForm(FlaskForm):

    username = StringField("Username", 
        validators=[InputRequired(message="Username must be entered")])
    password = PasswordField("Password", 
        validators=[InputRequired(message="Password must be provided")])
    submit = SubmitField("Log in", render_kw={"class":"btn btn-warning"})
    


class PersonalDay(FlaskForm):

    start_date = DateField("Starting Time")
    start_time = TimeField("Starting Time")
    return_date = DateField("Return Time")
    return_time = TimeField("Return Time")
    number_of_days = FloatField("Number of days :")
    out_of_country = BooleanField("Out of country")
    submit = SubmitField("Submit for approval", 
        render_kw={"class":"btn btn-warning"})



class MedicalDay(FlaskForm):
     
    appointment = StringField("Appointment to see:")
    reason = StringField("Reason for appointment:")
    location = StringField("Location of the appointment:")
    appointment_date = DateField("Appointment Date:")
    appointment_time = TimeField("Appointment Time:")
    arrive = TimeField("Time to get to work:")
    leave = TimeField("Time to leave work:")
    submit = SubmitField("Submit for approval", 
        render_kw={"class":"btn btn-warning"})
    


class LicenceForm(FlaskForm):
        product_name = StringField("Product Name: ")
        agreement = StringField("Agreement / Project name:")
        product_detail = TextAreaField(" Product Brief")
        usage = SelectField(choices=["Internal Use", "Customer"])
        mac = BooleanField("Mac", default=False)
        windows = BooleanField("Windows", default=False)
        android = BooleanField("Android", default=False)
        ios = BooleanField("iOS", default=False)
        unix = BooleanField("Unix Base OS", default=False)
        portal_url = URLField("Portal URL Address: ")
        avtication_key = StringField("Activation Key: ")
        username = StringField("Username / Email: ")
        password = StringField("Password: ")
        purchased_by = StringField("Purchased By (name) :")
        purchase_method = SelectField(choices=["Direct Debit", 
            "Credit Card", "Paypal", "Cash"])
        purchase_date = DateField("Purchase Date")
        expiration_date = DateField("Expiration Date")
        auto_renew = BooleanField("Auto Renewable", default=False)
        cost = FloatField("Cost")
        currency = SelectField(choices=["GBP £", "USD $", "EUR €"])
        
        submit = SubmitField("Finish", render_kw={"class":"btn btn-warning"})

