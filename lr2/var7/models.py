from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True) 
    login = db.Column(db.TEXT)
    email = db.Column(db.TEXT)
    md5_password = db.Column(db.TEXT)
    TTL = db.Column(db.TEXT)