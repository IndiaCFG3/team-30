from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5
from datetime import datetime
from app import data



class teacher(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(1), default='t')

    def __repr__(self):
        return '<teacher {}>'.format(self.name)

    def get_id(self):
        return self.id

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class admin(UserMixin ,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(128), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(1), default='a')
    
    def __repr__(self):
        return '<admin {}>'.format(self.name)
    
    def get_id(self):
        return self.id

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class studentHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    phoneno = db.Column(db.Integer)
    message_option = db.Column(db.String(1), default='s')
    marks = db.Column(db.Integer)

    def __repr__(self):
        return '<teacherHistory {} {} {} {}>'.format(self.id, self.name, self.phoneno, self.marks)

class assignments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(10000))
    answer = db.Column(db.String(10))
        
@login.user_loader
def load_teacher(id):
    print("userloader called", data.check_type())
    if data.check_type() == 'admin':
        print("userloader: admin")
        return admin.query.get(int(id))
    
    elif data.check_type() == 'teacher':
        print("userloader: teacher")
        return teacher.query.get(int(id))


