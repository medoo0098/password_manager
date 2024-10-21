from flask import (Flask, render_template, request, url_for, redirect, 
    session, flash, g)
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
from datetime import datetime, date, time
from flask_bootstrap import Bootstrap5
from forms import (RegisterForm, LoginForm, LicenceEditForm, PersonalDayForm, 
                   LicenceForm, MedicalDayForm, NoteForm, AccountsForm)

year=datetime.now().year






#  start of the views

def init_views(app):

    login_manager = LoginManager(app)
    login_manager.init_app(app)
    login_manager.login_view = "login"

    @app.before_request
    def set_global_variable():
        user_len = list(User.query.all())
        no_user = len(user_len)
        g.user_length = no_user


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    bootstrap5 = Bootstrap5(app)
    year=datetime.now().year



    # route to view home



    @app.route("/", methods=("GET", "POST"))
    def home():

        return render_template("index.html", 
                               title="Hire Intelligence Staff Portal", 
            year=datetime.now().year)



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
        accounts_list = list(Accounts.query.all())
        return render_template("accounts.html", title="Logins", 
            year=datetime.now().year, accounts_list=accounts_list)




    # route to view  add accounts



    @app.route("/add_account", methods=("GET", "POST"))
    def add_account():
        form = AccountsForm()
        if form.validate_on_submit():
            new_login = Accounts(
                date = datetime.now(),
                name = form.name.data,
                website = form.website.data,
                username = form.username.data,
                password = form.password.data,
                creator = form.creator.data,
                note = form.note.data,
                cost = form.cost.data,
                expiry = form.expiry.data
            )
            db.session.add(new_login)
            db.session.commit()
            return redirect(url_for("accounts"))

        return render_template("add-account.html", title="Add new account", 
            year=datetime.now().year, form=form)
    


     # router to view account detasils



    @app.route("/account_detail/<int:account_id>", methods=("GET", "POST"))
    def account_detail(account_id):
        account = db.get_or_404(Accounts, account_id )
        form = AccountsForm(
                name = account.name,
                website = account.website,
                username = account.username,
                password = account.password,
                creator = account.creator,
                note = account.note,
                cost = account.cost,
                expiry = account.expiry,
                date = account.date
            )
        if form.validate_on_submit():
            
            account.date = datetime.now()
            account.name = form.name.data
            account.website = form.website.data
            account.username = form.username.data
            account.password = form.password.data
            account.creator = form.creator.data
            account.note = form.note.data
            account.cost = form.cost.data
            account.expiry = form.expiry.data
            
            db.session.commit()
            return redirect(url_for('accounts'))

        return render_template("account-details.html", title="Account Details",
            year=datetime.now().year, form = form)
    



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
                agreement = form.agreement.data,
                product_detail = form.product_detail.data,
                usage = form.usage.data,
                mac = form.mac.data,
                windows = form.windows.data,
                android = form.android.data,
                ios =  form.ios.data,
                unix = form.unix.data,
                portal_url = form.portal_url.data,
                activation_key = form.activation_key.data,
                username = form.username.data,
                password = form.password.data,
                purchased_by = form.purchased_by.data,
                purchase_method = form.purchase_method.data, 
                purchased_date = form.purchase_date.data,
                expiration_date = form.expiration_date.data,
                auto_renew = form.auto_renew.data,
                cost = form.cost.data,
                currency = form.currency.data
            )
            db.session.add(new_licence)
            db.session.commit()
            return redirect(url_for('licences'))
        return render_template("add-licence.html", title="Add New Licence",
            year=datetime.now().year, form=form)



        # router to view detailed licences



    @app.route("/licence_detail/<int:licence_id>", methods=("GET", "POST"))
    def licence_detail(licence_id):
        licence = db.get_or_404(Licence, licence_id )
        form = LicenceEditForm(
                product_name = licence.product_name,
                agreement = licence.agreement,
                product_detail = licence.product_detail,
                usage = licence.usage,
                mac = licence.mac,
                windows = licence.windows,
                android = licence.android,
                ios =  licence.ios,
                unix = licence.unix,
                portal_url = licence.portal_url,
                activation_key = licence.activation_key,
                username = licence.username,
                password = licence.password,
                purchased_by = licence.purchased_by,
                purchase_method = licence.purchase_method, 
                purchased_date = licence.purchased_date,
                expiration_date = licence.expiration_date,
                auto_renew = licence.auto_renew,
                cost = licence.cost,
                currency = licence.currency
            )
        if form.validate_on_submit():
            
            licence.date = datetime.now()
            licence.product_name = form.product_name.data
            licence.agreement = form.agreement.data
            licence.product_detail = form.product_detail.data
            licence.usage = form.usage.data
            licence.mac = form.mac.data
            licence.windows = form.windows.data
            licence.android = form.android.data
            licence.ios =  form.ios.data
            licence.unix = form.unix.data
            licence.portal_url = form.portal_url.data
            licence.activation_key = form.activation_key.data
            licence.username = form.username.data
            licence.password = form.password.data
            licence.purchased_by = form.purchased_by.data
            licence.purchase_method = form.purchase_method.data
            licence.purchased_date = form.purchased_date.data
            licence.expiration_date = form.expiration_date.data
            licence.auto_renew = form.auto_renew.data
            licence.cost = form.cost.data
            licence.currency = form.currency.data
            
            db.session.commit()
            return redirect(url_for('licences'))

        return render_template("licence-details.html", title="Licence Details",
            year=datetime.now().year, form = form)



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
        anual_leave_list = list(PersonalDay.query.all())

        return render_template("anual-leave.html", 
            title="Anual Leave", year=datetime.now().year, list=anual_leave_list)



    # route to view add anual leave


    @app.route("/add_anual_leave", methods=("GET", "POST"))
    def add_anual_leave():
        form = PersonalDayForm()
        if form.validate_on_submit():
            new_leave_form = PersonalDay(
                date = datetime.now(),
                start_date = form.start_date.data,
                # start_date=datetime.combine(form.start_date.data, time.min) 
                # if form.start_date.data else None,
                start_time=datetime.combine(
                    date.min, form.start_time.data
                    ) if form.start_time.data else None,
                return_date = form.return_date,
                # return_date=datetime.combine(form.return_date.data, time.min) 
                # if form.return_date.data else None,
                return_time=datetime.combine(
                    date.min, form.return_time.data
                    ) if form.return_time.data else None,
                number_of_days = form.number_of_days.data,
                out_of_country = form.out_of_country.data
            )
            db.session.add(new_leave_form)
            db.session.commit()

            return redirect(url_for("anual_leave"))

        return render_template("add-anual-leave.html", 
            title="Add Anual Leave", year=datetime.now().year, form=form)




    # route to view anual leave details


    @app.route("/anual_leave_details/<int:leave_id>", methods=("GET", "POST"))
    def anual_leave_details(leave_id):
        
        anual_leave = db.get_or_404(PersonalDay, leave_id )
        form = PersonalDayForm(
            start_date = anual_leave.start_date,
            start_time = anual_leave.start_time,
            return_date = anual_leave.return_date,
            return_time = anual_leave.return_time,
            number_of_days = anual_leave.number_of_days,
            out_of_country = anual_leave.out_of_country,

        )
        if form.validate_on_submit():
            anual_leave.start_date = form.start_date.data
            anual_leave.start_time = datetime.combine(
                date.min, form.start_time.data
                ) if form.start_time.data else None
            anual_leave.return_date = form.return_date.data
            anual_leave.start_time = datetime.combine(
                date.min, form.return_time.data
                ) if form.return_time.data else None
            anual_leave.number_of_days = form.number_of_days.data
            anual_leave.out_of_country = form.out_of_country.data

            db.session.commit()
            return redirect(url_for("anual_leave"))


        return render_template("anual_leave_details.html", 
            title="Anual Leave Details", year=datetime.now().year, form=form)



    # route to view medial leave


    @app.route("/Medical_leave", methods=("GET", "POST"))
    def medical_leave():
        form = MedicalDayForm()
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