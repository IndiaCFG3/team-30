from flask import render_template, flash, redirect, url_for, request
from app import app, db, data
from flask_login import login_required, current_user, login_user, logout_user
from datetime import datetime
from app.forms import LoginForm, teacherRegistrationForm, adminRegistrationForm
from app.models import teacher, admin
from functools import wraps
from sqlalchemy.exc import IntegrityError

@app.route('/', methods=['GET'])
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/login', methods=['GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form_teacher = LoginForm()
    form_admin = LoginForm()

    return render_template('login.html', form_teacher=form_teacher, form_admin=form_admin, title='Login')

@app.route('/login_admin', methods=['POST'])
def login_admin():
    if current_user.is_authenticated:
        print("redirected from login admin")
        return redirect(url_for('home'))

    form_admin = LoginForm()

    if 1 or form_admin.validate_on_submit():
        admin = admin.query.filter_by(email=form_admin.email.data).first()
        # print(admin.role)
        if admin and admin.check_password(password=form_admin.password.data):
            print("before admin login")
            login_user(admin)
            print("user logged in as admin")
            data.set_type('admin')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            print('Login unsuccessful. Please check mail and password')
            flash('Login unsuccessful. Please check mail and password')
            return redirect(url_for('login'))

    return redirect(url_for('login'))
    # if form.validate_on_submit():
    #     user = User.query.filter_by(email=form.email.data).first()
    #     if user and bcrypt.check_password_hash(user.password, form.password.data):
    #         login_user(user, remember=form.remember.data)
    #         next_page = request.args.get('next')
    #         return redirect(next_page) if next_page else redirect(url_for('home'))
    #     else:
    #         flash('Login Unsuccessful. Please check email and password', 'danger')

@app.route('/login_teacher', methods=['POST'])
def login_teacher():
    if current_user.is_authenticated:
        print("redirected from login teacher")
        return redirect(url_for('home'))

    form_teacher = LoginForm()
    
    if  1 or form_teacher.validate_on_submit():
        teacher = teacher.query.filter_by(email=form_teacher.email.data).first()
        
        if teacher and teacher.check_password(password=form_teacher.password.data):
            print("before teacher login")
            login_user(teacher)
            print("user logged in as teacher")
            data.set_type('teacher')
            next_page = request.args.get('next')
            
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            print('Login unsuccessful. Please check mail and password')
            flash('Login unsuccessful. Please check mail and password')
            return redirect(url_for('login'))

    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    data.set_type('nil')
    logout_user()
    return redirect(url_for('home'))

@app.route('/register',methods=['GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form_teacher = teacherRegistrationForm()
    form_admin = adminRegistrationForm()

    return render_template('register_teacher.html', form_teacher=form_teacher, form_admin=form_admin, title="Sign Up")

@app.route('/register_teacher', methods = ['POST'])
def register_teacher():
    form_teacher = teacherRegistrationForm()

    if 1 or form_teacher.validate_on_submit():
        teacher_ = teacher(name = form_teacher.name.data, email = form_teacher.email.data)
        teacher_.set_password(form_teacher.password.data)

        db.session.add(teacher_)
        db.session.commit()
    
    else:
        flash("error in signing up")

    return redirect(url_for('home'))    

@app.route('/register_admin', methods = ['POST'])
def register_admin():
    form_admin = adminRegistrationForm()
     
    if 1 or form_admin.validate_on_submit():
        admin = admin(name = form_admin.name.data, email = form_admin.email.data)
        admin.set_password(form_admin.password.data)

        db.session.add(admin)
        db.session.commit()
    
    else:
        flash("error in signing up")

    return redirect(url_for('home'))

# @app.route('/add_teacher_data', methods=['GET', 'POST'])
# @login_required
# # @admin_required
# def add_teacher_data():
#     teacher_history = AddteacherHistory()

#     if request.method == 'GET':
#         return render_template('analysis.html', teacher_history=teacher_history, title="Add teacher Data")

#     teacher_t = teacher.query.filter_by(otp = teacher_history.otp_add.data).first()
#     print(teacher_t)
#     if teacher_t:
#         p_history = teacherHistory(teacher_id=teacher_t.id,
#                                    symptoms=teacher_history.symptoms.data, 
#                                    diagnosis=teacher_history.diagnosis.data,
#                                    treatment=teacher_history.treatment.data)
#         db.session.add(p_history)
#         db.session.commit()
#         print('validated')
#         return redirect('view_teacher_history')
#     else:
#         print("error, try again")
#         flash("Error, Try again")

