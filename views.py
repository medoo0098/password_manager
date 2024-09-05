from flask import Flask, render_template, request, url_for, redirect, session, flash
from models import User, SiteEntry
from config import db
from werkzeug.security import generate_password_hash, check_password_hash 
from datetime import datetime
from flask_login import LoginManager, login_user, current_user, logout_user, login_required



def init_views(app):

    login_manager = LoginManager(app)
    login_manager.login_view = "login"



    
    @app.route("/")
    def Home():
        return "it works"