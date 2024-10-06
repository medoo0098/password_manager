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
    admin = BooleanField("Admin",default="")
    manager = BooleanField("Manager", default="")
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
    password = StringField("Password", 
        validators=[InputRequired(message="Password must be provided")])
    submit = SubmitField("Log in", render_kw={"class":"btn btn-warning"})
    


class PersonalDay(FlaskForm):

    start_date = DateField("Starting Time")
    start_time = TimeField("Starting Time")
    return_date = DateField("Return Time")
    return_time = TimeField("Return Time")
    submit = SubmitField("Submit for approval", 
        render_kw={"class":"btn btn-warning"})


class AddLicence(FlaskForm):

    class ProductDetails(FlaskForm):
        product_name = StringField("Product Name: ")
        usage = SelectField(choices=["Internal Use", "Customer"])
        mac = BooleanField("Mac", default="")
        windows = BooleanField("Windows", default="")
        android = BooleanField("Android", default="")
        ios = BooleanField("iOS", default="")
        unix = BooleanField("Unix Base OS", default="")


    
    class ProductManagement(FlaskForm):
        portal_url = URLField("Portal URL Address: ")
        avtication_key = StringField("Activation Key: ")
        username = StringField("Username / Email: ")
        password = StringField("Password: ")
        purchased_by = StringField("Purchased By (name) :")
        purchase_method = SelectField(choices=["Direct Debit", 
            "Credit Card", "Paypal", "Cash"])
        purchase_date = DateField("Purchase Date")
        experation_date = DateField("Expiration Date")
        purchase_duration = IntegerField("Duration")
        month_year = SelectField(choices=["Month", "Year"])
        cost = FloatField("Cost")
        currency = SelectField(choices=["GBP £", "USD $", "EUR €"])

    class ProductUsage(FlaskForm):
        usecase = SelectField(choices=["Customer", "Internal"])
        agreement = StringField("Agreement / Project:")
        usage_starting = DateField("Starting to use from:")
        usage_end = DateField("End usage on:")