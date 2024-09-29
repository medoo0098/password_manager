from flask import Flask, render_template, request, url_for, redirect, session, flash
from models import User
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
from datetime import datetime
from flask_bootstrap import Bootstrap5
from forms import RegisterForm, LoginForm, LeaveForm


def init_views(app):

    login_manager = LoginManager(app)
    login_manager.init_app(app)
    login_manager.login_view = "login"
    bootstrap5 = Bootstrap5(app)

    year=datetime.now().year

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.route("/", methods=("GET", "POST"))
    def home():
        form = LeaveForm()

        return render_template("index.html", title="Hire Intelligence Staff Portal", year=datetime.now().year, form=form)

    @app.route("/login", methods=("GET", "POST"))
    def login():
        form = LoginForm()
        username = form.username.data
        password = form.password.data
        return render_template("login.html", title="Login", year=year, form=form)

    @app.route("/register", methods=("GET", "POST"))
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            email = form.email.data
            admin = form.admin.data
            manager = form.manager.data
            department = form.department.data
            print(username, password, email, admin, manager, department)
        return render_template("register.html", title="Register", year=datetime.now().year, form=form)

    @app.route("/logout", methods=("GET", "POST"))
    def logout():
        return render_template("logout.html", title="Logout", year=datetime.now().year)

    @app.route("/about", methods=("GET", "POST"))
    def about():
        return render_template("about.html", title="About", year=datetime.now().year)

    @app.route("/accounts", methods=("GET", "POST"))
    def accounts():
        return render_template("accounts.html", title="Logins", year=datetime.now().year)

    @app.route("/share_notes", methods=("GET", "POST"))
    def share_notes():
        return render_template("share-notes.html", title="Share Notes", year=datetime.now().year)

    @app.route("/secure_notes", methods=("GET", "POST"))
    def secure_notes():
        return render_template("secure-notes.html", title="Secure Personal Notes", year=datetime.now().year)
