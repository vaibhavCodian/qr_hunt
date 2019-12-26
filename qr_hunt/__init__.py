from flask import Flask, url_for, redirect, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, LoginManager, login_user,current_user, logout_user, login_manager
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://gnhizxktomvtfp:8598e62682358aa9c073eba5d7b748d28d865f6ffdcc2a719636a1a4bf52028f@ec2-79-125-2-142.eu-west-1.compute.amazonaws.com:5432/danq3avmu0cv6r'
app.config['SECRET_KEY'] = 'randomSecret'

db = SQLAlchemy(app)

migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'


from qr_hunt import routes