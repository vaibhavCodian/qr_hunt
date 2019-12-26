from flask import Flask, url_for, redirect, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, LoginManager, login_user,current_user, logout_user, login_manager
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://vmpjgckmtjwgxr:2d14a8c7090990980490e1b43eb9d1e3bb27dda5a17405d3f5b2a917d0fc5bc0@ec2-174-129-254-218.compute-1.amazonaws.com:5432/dsqnofkns97f'
app.config['SECRET_KEY'] = 'randomSecret'

db = SQLAlchemy(app)

migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'


from qr_hunt import routes