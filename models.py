from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from app import db ,login
import datetime


class UserModels(UserMixin,db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True, unique=True)
    pwd = db.Column(db.String(128))

    first_name = db.Column(db.String, default="")
    last_name = db.Column(db.String, default="")

    create_date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, email): #
        self.email = email

    def set_user_password(self, pwd): #transformer le mdp en mdp cripté
        self.pwd = generate_password_hash(pwd)

    def get_user_password(self, pwd): #récupérer le mdp cripté
        return generate_password_hash(pwd)

    def verify_user_password(self, pwd):
        if self.pwd is None:
            return False
        return check_password_hash(self.pwd, pwd)


class FoodModels(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pic = db.Column(db.String, default="")
    name = db.Column(db.String, default="")
    price = db.Column(db.String, default="")
    desc = db.Column(db.Text, default="")
    comm = db.Column(db.Text, default="")


class CollectModels(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(UserModels.id))
    food_id = db.Column(db.Integer, db.ForeignKey(FoodModels.id))
    sock_status = db.Column(db.Boolean, default=True)

class NoteModels(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(UserModels.id))
    prenoom = db.Column(db.String, default="")
    email = db.Column(db.String, default="")
    subject = db.Column(db.String, default="")
    message = db.Column(db.Text, default="")

class EntreeModels(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, default="")
    desc = db.Column(db.Text, default="")

class PlatModels(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, default="")
    desc = db.Column(db.Text, default="")

class DessertModels(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, default="")
    desc = db.Column(db.Text, default="")