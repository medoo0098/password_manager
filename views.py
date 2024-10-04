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

    

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    bootstrap5 = Bootstrap5(app)
    year=datetime.now().year



    # route to view home



    @app.route("/", methods=("GET", "POST"))
    def home():
        form = LeaveForm()

        return render_template("index.html", title="Hire Intelligence Staff Portal", year=datetime.now().year, form=form)



    # route to view login



    @app.route("/login", methods=("GET", "POST"))
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data

        return render_template("login.html", title="Login", year=year, form=form)



    # route to view register



    @app.route("/register", methods=("GET", "POST"))
    def register():
        form = RegisterForm()
        errors=None
        if form.validate_on_submit():
            new_user = User(
            username = form.username.data,
            password = generate_password_hash(f'{form.password.data}', method="pbkdf2:sha256", salt_length=8),
            email = form.email.data,
            is_admin = form.admin.data,
            is_manager = form.manager.data,
            department = form.department.data
            )
            db.session.add(new_user)
            db.session.commit()
            flash("User created successfully", "success")
            return redirect(url_for("login"))
        else:
            if form.errors:
                error = list(form.errors.value())
                flash(f"Registeration failed: {errors[0][0]}", "danger")


        return render_template("register.html", title="Register", year=datetime.now().year, form=form, errors=errors)



    # route to view logout



    @app.route("/logout", methods=("GET", "POST"))
    def logout():
        return render_template("logout.html", title="Logout", year=datetime.now().year)



    # route to view about



    @app.route("/about", methods=("GET", "POST"))
    def about():
        return render_template("about.html", title="About", year=datetime.now().year)



    # route to view accounts



    @app.route("/accounts", methods=("GET", "POST"))
    def accounts():
        return render_template("accounts.html", title="Logins", year=datetime.now().year)



    # router to view licences



    @app.route("/licences", methods=("GET", "POST"))
    def licences():
        return render_template("licences.html", title="Licences", year=datetime.now().year)



    # router to view note




    @app.route("/notes", methods=("GET", "POST"))
    def notes():
        return render_template("notes.html", title="Notes", year=datetime.now().year)



    # router to view share note



    @app.route("/share_notes", methods=("GET", "POST"))
    def share_notes():
        return render_template("share-notes.html", title="Share Notes", year=datetime.now().year)


    # route to view secure note




    @app.route("/secure_notes", methods=("GET", "POST"))
    def secure_notes():
        return render_template("secure-notes.html", title="Secure Personal Notes", year=datetime.now().year)



    # route to view leave


    @app.route("/leave", methods=("GET", "POST"))
    def leave():
        return render_template("leave.html", title="Anual/Medical Leave", year=datetime.now().year)
    

    # route to view anual leave


    @app.route("/anual_leave", methods=("GET", "POST"))
    def anual_leave():
        return render_template("anual-leave.html", title="Anual Leave", year=datetime.now().year)
    


    # route to view medial leave


    @app.route("/Medical_leave", methods=("GET", "POST"))
    def medical_leave():
        return render_template("medical-leave.html", title="Medical Leave", year=datetime.now().year)
    



    # route to view compensation


    @app.route("/compensation", methods=("GET", "POST"))
    def compensation():
        return render_template("compensation.html", title="Compensations", year=datetime.now().year)
    


    # route to view expence


    @app.route("/expence", methods=("GET", "POST"))
    def expence():
        return render_template("expence.html", title="Expence Claim", year=datetime.now().year)
    

    # route to view overtime


    @app.route("/overtime", methods=("GET", "POST"))
    def overtime():
        return render_template("overtime.html", title="Overtime", year=datetime.now().year)