from config import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    Password = db.Column(db.String(512), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean)



class SiteEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    website = db.Column(db.String, nullable=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    creator = db.Column(db.String)
    note = db.Column(db.String(500))
    time = db.Column(db.DateTime(timezone=True))
