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
    lectures = db.relationship('lectureHistory')

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
    marks = db.relationship('scores')

    def __repr__(self):
        return '<studentHistory {} {} {}>'.format(self.id, self.name, self.phoneno)

class lectureHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(100), index=True, unique=True, nullable=False)
    transcript = db.Column(db.String(100000), index=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))

    def __repr__(self):
        return '<lectureHistory {}>'.format(self.id)

class assignments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(10000))
    option1 = db.Column(db.String(100))
    option2 = db.Column(db.String(100))
    option3 = db.Column(db.String(100))
    option4 = db.Column(db.String(100))
    answer = db.Column(db.Integer)

    scores = db.Column(db.Integer, db.ForeignKey('scores.id'))

class scores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marks = db.Column(db.Integer)
    student_id = db.Column(db.Integer, db.ForeignKey('studentHistory.id'))
    assignments_id = db.relationship('assignments')

@login.user_loader
def load_teacher(id):
    print("userloader called", data.check_type())
    if data.check_type() == 'admin':
        print("userloader: admin")
        return admin.query.get(int(id))
    
    elif data.check_type() == 'teacher':
        print("userloader: teacher")
        return teacher.query.get(int(id))


