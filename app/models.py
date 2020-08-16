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
    role = db.Column(db.String(1), default='d')
    
    def __repr__(self):
        return '<admin {}>'.format(self.name)
    
    def get_id(self):
        return self.id

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# class teacherHistory(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     time_stamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     teacher_id = db.Column(db.Integer, nullable=False)
#     # admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
#     symptoms = db.Column(db.String(200))
#     diagnosis = db.Column(db.String(200))
#     treatment = db.Column(db.String(200))
    
#     def __repr__(self):
#         return '<teacherHistory {} {} {} {}>'.format(self.id, self.symptoms, self.diagnosis, self.treatment)

@login.user_loader
def load_teacher(id):
    print("userloader called", data.check_type())
    if data.check_type() == 'admin':
        print("userloader: admin")
        return admin.query.get(int(id))
    
    elif data.check_type() == 'teacher':
        print("userloader: teacher")
        return teacher.query.get(int(id))


