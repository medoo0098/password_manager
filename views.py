from flask import Flask, render_template, request, url_for, redirect, session, flash
from models import User, SiteEntry
from config import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import (
    LoginManager,
    login_user,
    current_user,
    logout_user,
    login_required,
)


def init_views(app):

    login_manager = LoginManager(app)
    login_manager.init_app(app)
    login_manager.login_view = "login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.route("/")
    def home():
        return render_template("index.html", title="Home")

    @app.route("/login", methods=("GET", "POST"))
    def login():
        return render_template("login.html", title="Login")

    @app.route("/register", methods=("GET", "POST"))
    def register():
        return render_template("register.html", title="Register")

    @app.route("/logout", methods=("GET", "POST"))
    def logout():
        return render_template("logout.html", title="Logout")

    @app.route("/about", methods=("GET", "POST"))
    def about():
        return render_template("about.html", title="About")

    @app.route("/logins", methods=("GET", "POST"))
    def logins():
        return render_template("logins.html", title="Logins")

    @app.route("/share_notes", methods=("GET", "POST"))
    def share_notes():
        return render_template("share-notes.html", title="Share Notes")

    @app.route("/secure_notes", methods=("GET", "POST"))
    def secure_notes():
        return render_template("secure-notes.html", title="Secure Personal Notes")
