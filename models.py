from config import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(512), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean)
    is_manager = db.Column(db.Boolean)
    department = db.Column(db.String)



class Accounts(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    website = db.Column(db.String, nullable=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    creator = db.Column(db.String)
    note = db.Column(db.String(500))
    time = db.Column(db.DateTime(timezone=True))
    cost = db.column(db.Float)
    expiry = db.Column(db.DateTime(timezone=True))



class PersonalDay(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime(timezone=True))
    start_date = db.Column(db.DateTime(timezone=True))
    start_time = db.Column(db.DateTime(timezone=True))
    return_date = db.Column(db.DateTime(timezone=True))
    return_time = db.Column(db.DateTime(timezone=True))
    number_of_days = db.Column(db.Float)
    out_of_country = db.Column(db.Boolean)



class MedicalDay(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime(timezone=True))
    appointment = db.Column(db.String)
    reason = db.Column(db.String)
    location = db.Column(db.String)
    appointment_date = db.Column(db.DateTime(timezone=True))
    appointment_time = db.Column(db.DateTime(timezone=True))
    arrive = db.Column(db.DateTime(timezone=True))
    leave = db.Column(db.DateTime(timezone=True))



class Licence(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime(timezone=True))
    product_name = db.Column(db.String)
    agreement = db.Column(db.String)
    product_detail = db.Column(db.String)
    usage = db.Column(db.String)
    mac = db.Column(db.Boolean)
    windows = db.Column(db.Boolean)
    android = db.Column(db.Boolean)
    ios = db.Column(db.Boolean)
    unix = db.Column(db.Boolean)
    portal_url = db.Column(db.String)
    activation_key = db.Column(db.String)
    username = db.Column(db.String)
    password = db.Column(db.String)
    purchased_by = db.Column(db.String)
    purchased_date = db.Column(db.DateTime(timezone=True))
    purchase_method = db.Column(db.String)
    expiration_date = db.Column(db.DateTime(timezone=True))
    auto_renew = db.Column(db.Boolean)
    cost = db.Column(db.Float)
    currency = db.Column(db.String)




class ShareNotes(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    date = db.Column(db.DateTime(timezone=True))
    title = db.Column(db.String, nullable=False)
    note = db.Column(db.String, nullable=False)
    author = db.Column(db.String)



class SecureNote(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime(timezone=True))
    secure_note = db.Column(db.String)
    secure_author = db.Column(db.String)



class ExpenceClaim(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime(timezone=True))
    



class Overtime(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime(timezone=True))




