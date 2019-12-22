from qr_hunt import db, login_manager
from flask_login import UserMixin 

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    passw = db.Column(db.String(255))
    defin = db.Column(db.String(255))
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    
    def __init__(self, name, passw, defin, is_admin):
        self.name = name
        self.passw = passw
        self.defin = defin
        self.is_admin = is_admin
    def __repr__(self):
        return f"User('{self.name}', '{self.passw}')"

class Clue(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key)
    c_text = db.Column(db.String)
    index 



