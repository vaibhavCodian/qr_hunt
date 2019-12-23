from flask import Flask, send_file,url_for, redirect, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
import qrcode
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, LoginManager, login_user,logout_user, login_manager, login_required, logout_user
from qr_hunt.models import User, Cluestack, Clue
from qr_hunt import db, app, login, current_user


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

@app.route('/clue/<int:cls>/<int:cl_i>')
@login_required
def clue(cls, cl_i):
# !! note : will add a code so no one can change the url directly
    c = Cluestack.query.get_or_404(cls)
    stack_i = current_user.stack_i
    if cl_i > stack_i:
        return "please request errror"
    elif cl_i == current_user.stack_i:
        print("updating.................................................>>>>")
        current_user.stack_i = stack_i + 1
        db.session.commit()
        print(current_user.stack_i)
        
    c_i = c.clue[cl_i].clue_txt

    return c_i

# stack_index = 
@app.route('/qr/<int:cls>')
@login_required
def qr_gen(cls):
    #->get the stack
    l = len(Cluestack.query.get_or_404(cls).clue.all())
    i=0
    while i < l:
        print("_____________url_______")
        print("url"+"/clue/"+str(cls)+"/"+str(i)+"/")
        i = i + 1
    return str(l)

# GeneratE LinkS with [StAck_naMe]
# ---->
# ---->
# @ #-> get the Links And and [Create QRcOdE] 

    # qr = qrcode.QRCode(
    #     version=1, box_size=35, border=5
    # )
    # data = "http://google.com"
    # qr.add_data(data)
    # qr.make(fit=True)
    # img = qr.make_image(fill="black", black_color="white")
    # img.save("qr/qr11.png")
    # # return "Hello"
    # return send_file('../qr/qr11.png', mimetype='image/png')
    