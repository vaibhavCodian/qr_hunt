from flask import Flask, send_file, send_from_directory,url_for, redirect, request, render_template, flash, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_qrcode import QRcode
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, LoginManager, login_user,logout_user, login_manager, login_required, logout_user
from qr_hunt.models import User, Cluestack, Clue
from qr_hunt import db, app, login, current_user
import os

blueprint = Blueprint('site', __name__, static_url_path='/static/site', static_folder='qr_hunt/static')
app.register_blueprint(blueprint)

qrcode = QRcode(app)
class Controller(ModelView):
    def is_accessible(self):
        return current_user.is_admin
        
    def not_auth(self):
        return "You Are Not Authorized to Use Admin Pannel"

admin = Admin(app, name='Control Panel')
admin.add_view(Controller(User, db.session))
admin.add_view(Controller(Cluestack, db.session))
admin.add_view(Controller(Clue, db.session))

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@app.route('/home')
def home():
    # generate urls and display only the once done
    if current_user.is_authenticated:
        urls = []
        if current_user.stack_i == 0:
            urls = url_gen(1)
        return render_template("index.html", urls=urls, s_i=current_user.stack_i)
        # return "logged"
    else:
        print("...................................////")
        return render_template("index.html")
        
@app.route('/base/<path:filename>')
def base_static(filename):
    return send_from_directory(app.root_path + '/static/', filename)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #GET FORM FIELD's
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(name= username).first()
        if user and user.passw == password:
            login_user(user, remember=True)
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. please check the username and password', 'danger')

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return "LOgged Out"

@app.route('/clue/<int:cls>/<int:cl_i>')
@login_required
def clue(cls, cl_i):
# !! note : will add a code so no one can change the url directly
    c = Cluestack.query.get_or_404(cls)
    stack_i = current_user.stack_i
    l = c.clue.count() - 1
    if cl_i > stack_i:
        return render_template("clue.html", msg_e="Wrong😔 Place. Wrong Time, Better Luck Next Time.👍🏼 ")
    elif cl_i == current_user.stack_i:
        print("updating.................................................>>>>")
        current_user.stack_i = stack_i + 1
        db.session.commit()
        print(current_user.stack_i)
    
    c_i = c.clue[cl_i].clue_txt
    return render_template("clue.html", clue=c_i)

# qr_gen => 
@app.route('/qr/<int:cls>')
@login_required
def qr_gen(cls):
    urls = url_gen(cls)
    return render_template("qr_list.html",urls=urls)

# url_gen=>
def url_gen(cls):
    urls = []
    url = "https://qr-hu.herokuapp.com/"
    #->get the stack
    l = len(Cluestack.query.get_or_404(cls).clue.all())
    i=0
    while i < l:
        u = url+"clue/"+str(cls)+"/"+str(i)
        i = i + 1 
        urls.append(u)
    return urls




