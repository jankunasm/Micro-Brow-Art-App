from enum import unique
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
from flask_login import LoginManager, UserMixin
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String, nullable = True, default = '')
    last_name = db.Column(db.String, nullable = True, default = '')
    email = db.Column(db.String, nullable = False)
    password = db.Column(db.String, nullable = False, default = '') # nullable can be True here with linking other accounts
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    customer = db.relationship('Customer', backref = "owner", lazy = True)

    def __init__(self, email, first_name = '', last_name = '', id = '', password = '', token = ''):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(20)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def set_token(self, length):
        return secrets.token_hex(length)

    def __repr__(self):
        return f'User {self.email} has been added to the Database.'


class Customer(db.Model):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(100), nullable = False)
    last_name = db.Column(db.String(100), nullable = False)
    needle = db.Column(db.String(100), nullable = True)
    machine = db.Column(db.String(100), nullable = True)
    pigment = db.Column(db.String(100), nullable = True)
    brow_type = db.Column(db.String(100), nullable = True)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, first_name, last_name, needle, machine, pigment, brow_type, user_token, id = ''):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.needle = needle
        self.machine = machine
        self.pigment = pigment
        self.brow_type = brow_type
        self.user_token = user_token

    def set_id(self):
        return secrets.token_urlsafe()

    def __repr__(self):
        return f'The following Customer has been added: {self.first_name} {self.last_name}'

class CustomerSchema(ma.Schema):
    class Meta:
        fields = ['id','first_name','last_name','needle','machine','pigment','brow_type']

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many = True)