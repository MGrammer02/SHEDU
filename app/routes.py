from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db
from app.forms import LoginForm
from app.models import Paralels
from app.models import Salutation
from app.models import Subjects
from app.models import Teachers
from app.models import Courses
from app.models import CourseSubject
from app.models import CourseSubjectTeacher
from app.models import SubjectTeacher
from app.models import CourseTeacher
from app.models import Genders
from app.models import Users

@app.route('/')
@login_required
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = Users.query.filter_by(user=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Inicio de sesión exitoso!', 'success')
            return redirect(url_for('index'))  # Cambia 'index' con la ruta a la que deseas redirigir después del inicio de sesión.

        flash('Usuario o contraseña incorrectos. Inténtalo de nuevo.', 'error')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('¡Ha cerrado sesión!', 'succes')
    return redirect(url_for('login'))

@app.route('/add')
def addUser():
    new_user = Users(teacher_id=2, user='juanaquevedo', password=Users.create_password('juanita2023'), admin=True)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('index'))
    
@app.route('/admin-teachers')
@login_required
def adminTeachers():
    teachers = Teachers.query.all()
    return render_template('admin-teachers.html', teachers=teachers)

@app.route('/admin-subjects')
@login_required
def adminSubjects():
    subjects = Subjects.query.all()
    return render_template('admin-subjects.html', subjects=subjects)

@app.route('/admin-courses')
@login_required
def adminCourses():
    courses = Courses.query.all()
    return render_template('admin-courses.html', courses=courses)

@app.route('/admin-sheduls')
@login_required
def adminSheduls():
    sheduls = 'EMPTY FOR THE MOMENT :('
    return render_template('admin-sheduls.html', sheduls=sheduls)

@app.route('/admin-salutation')
@login_required
def adminSalutation():
    salutations = Salutation.query.all()
    return render_template('admin-salutation.html', salutations=salutations)