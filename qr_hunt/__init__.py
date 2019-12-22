from flask import Flask, url_for, redirect, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, LoginManager, login_user,current_user, logout_user, login_manager

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'randomSecret'

db = SQLAlchemy(app)

login = LoginManager(app)
login.login_view = 'login'

from qr_hunt import routes