from flask import Flask, url_for, redirect, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, LoginManager, login_user,current_user, logout_user, login_manager, login_required, logout_user
from qr_hunt.models import User
from qr_hunt import db, app, login


class Controller(ModelView):
    def is_accessible(self):
        return current_user.is_admin
    def not_auth(self):
        return "You Are Not Authorized to Use Admin Pannel"

admin = Admin(app, name='Control Panel')
admin.add_view(Controller(User, db.session))

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return 'index.html!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #GET FORM FIELD's
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(name= username).first()
        if user and user.passw == password:
            login_user(user, remember=True)
            return render_template('index.html')
        else:
            flash(f'Login Unsuccessful. please check the username and password', 'danger')

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()

    return render_template("index.html")

