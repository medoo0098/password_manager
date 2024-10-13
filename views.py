from flask import (Flask, render_template, request, url_for, redirect, 
    session, flash)
from models import (User, Licence, Accounts, PersonalDay, MedicalDay, 
                    ShareNotes, SecureNote, ExpenceClaim, Overtime)
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
from forms import (RegisterForm, LoginForm, 
    PersonalDay, LicenceForm, MedicalDay, NoteForm)


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
        form = PersonalDay()

        return render_template("index.html", 
            title="Hire Intelligence Staff Portal", 
            year=datetime.now().year, form=form)



    # route to view login



    @app.route("/login", methods=("GET", "POST"))
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data

            user = User.query.filter_by(username=username).first()
            if user and check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for("home"))

        return render_template("login.html", title="Login", 
            year=year, form=form)



    # route to view register



    @app.route("/register", methods=("GET", "POST"))
    def register():
        form = RegisterForm()
        errors=None
        if form.validate_on_submit():
            new_user = User(
            username = form.username.data,
            password = generate_password_hash(f'{form.password.data}', 
                method="pbkdf2:sha256", salt_length=8),
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


        return render_template("register.html", title="Register", 
            year=datetime.now().year, form=form, errors=errors)



    # route to view logout



    @app.route("/logout", methods=("GET", "POST"))
    def logout():
        user = current_user.username
        logout_user()
        flash(f"user {user.capitalize()} is logged out.", "warning")
        return redirect(url_for("login"))


    # route to view about



    @app.route("/about", methods=("GET", "POST"))
    def about():
        return render_template("about.html", title="About", 
            year=datetime.now().year)



    # route to view accounts



    @app.route("/accounts", methods=("GET", "POST"))
    def accounts():
        return render_template("accounts.html", title="Logins", 
            year=datetime.now().year)




    # route to view  add accounts



    @app.route("/add_account", methods=("GET", "POST"))
    def add_account():
        return render_template("add-account.html", title="Adding new account", 
            year=datetime.now().year)
    



    # router to view licences



    @app.route("/licences", methods=("GET", "POST"))
    def licences():
        licence_list = list(Licence.query.all())

        return render_template("licences.html", title="Licences",
            year=datetime.now().year, licence_list=licence_list)
    


        # router to view add licences



    @app.route("/add_licence", methods=("GET", "POST"))
    def add_licence():
        form = LicenceForm()
        if form.validate_on_submit():
            new_licence = Licence(
                date = datetime.now(),
                product_name = form.product_name.data,
                product_detail = form.product_detail.data,
                expiration_date = form.expiration_date.data

            )
            db.session.add(new_licence)
            db.session.commit()
            return redirect(url_for('licences'))
        return render_template("add-licence.html", title="Add New Licence",
            year=datetime.now().year, form=form)



    # router to view note




    @app.route("/notes", methods=("GET", "POST"))
    def notes():
        return render_template("notes.html", title="Notes", 
            year=datetime.now().year)



    # router to view share note



    @app.route("/share_notes", methods=("GET", "POST"))
    def share_notes():
        notes_list = list(ShareNotes.query.all())
        notes_list = sorted(notes_list, key=lambda x: x.date)
        return render_template("share-notes.html", title="Share Notes", 
            year=datetime.now().year, notes_list=notes_list)
    


        # router to view add share note



    @app.route("/add_notes", methods=("GET", "POST"))
    def add_notes():
        form = NoteForm()

        if form.validate_on_submit():
            add_note = ShareNotes(
                title = form.title.data,
                date = datetime.now(),
                note = form.body.data,
                author = current_user.username
            )
            db.session.add(add_note)
            db.session.commit()
            return redirect(url_for("share_notes"))
        return render_template("add-notes.html", title="Add Notes", 
            year=datetime.now().year, form=form)
    



    # route to view secure note




    @app.route("/secure_notes", methods=("GET", "POST"))
    def secure_notes():
        return render_template("secure-notes.html", 
            title="Secure Personal Notes", year=datetime.now().year)
    


    
        # router to view add secure note



    @app.route("/add_secure_notes", methods=("GET", "POST"))
    def add_secure_notes():
        form = NoteForm()
        return render_template("add-secure-notes.html", 
                               title="Add Secure Notes", 
            year=datetime.now().year, form=form)



    # route to view leave


    @app.route("/leave", methods=("GET", "POST"))
    def leave():
        
        return render_template("leave.html", 
            title="Anual/Medical Leave", year=datetime.now().year)
    

    # route to view anual leave


    @app.route("/anual_leave", methods=("GET", "POST"))
    def anual_leave():

        form = PersonalDay()
        return render_template("anual-leave.html", 
            title="Anual Leave", year=datetime.now().year, form=form)
    


    # route to view medial leave


    @app.route("/Medical_leave", methods=("GET", "POST"))
    def medical_leave():
        form = MedicalDay()
        return render_template("medical-leave.html", 
            title="Medical Leave", year=datetime.now().year,
            form=form)
    



    # route to view compensation


    @app.route("/compensation", methods=("GET", "POST"))
    def compensation():
        return render_template("compensation.html", 
            title="Compensations", year=datetime.now().year)
    


    # route to view expence


    @app.route("/expence", methods=("GET", "POST"))
    def expence():
        return render_template("expence.html", 
            title="Expence Claim", year=datetime.now().year)
    

    # route to view overtime


    @app.route("/overtime", methods=("GET", "POST"))
    def overtime():
        return render_template("overtime.html", title="Overtime", 
            year=datetime.now().year)