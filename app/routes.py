from flask import render_template, redirect, url_for, flash, jsonify, request
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
    return render_template('admin-teachers.html', teachers=teachers, salutations=get_salutations(), genders=get_genders())

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

@app.route('/getSalutations')
@login_required
def get_salutations():
    if current_user.admin:
        return Salutation.query.all()
  
    
@app.route('/getGenders')
@login_required
def get_genders():
    if current_user.admin:
        return Genders.query.all()
    
    
@app.route('/get_teacher/<int:teacher_id>')
@login_required
def get_teacher(teacher_id):
    print(teacher_id)
    try:
        teacher = Teachers.query.get(teacher_id)
        if teacher:
            teacher_info = {
                'first_name': teacher.first_name,
                'second_name': teacher.second_name,
                'first_lastname': teacher.first_lastname,
                'second_lastname': teacher.second_lastname,
                'work_hours': teacher.work_hours,
                'gender_id': teacher.gender_id,
                'salutation_id': teacher.salutation_id
            }
            return jsonify(teacher_info)
        else:
            return jsonify({'error': 'Profesor no encontrado'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/add_teacher', methods=['POST'])
@login_required
def add_teacher():
    if current_user.admin:
        try:
            first_name = request.form.get('firstName')
            second_name = request.form.get('secondName')
            first_lastname = request.form.get('firstLastName')
            second_lastname = request.form.get('secondLastName')
            gender_id = request.form.get('gender')
            salutation_id = request.form.get('salutation')
            hours = request.form.get('hours')
            
            new_teacher = Teachers(first_name=first_name, second_name=second_name, first_lastname=first_lastname, second_lastname=second_lastname, work_hours=hours, gender_id=gender_id, salutation_id=salutation_id)

            # Agregar el profesor a la base de datos
            db.session.add(new_teacher)
            db.session.commit()
            return jsonify({'message': 'Docente agregado exitosamente! :D'})
        except Exception as e:
            return jsonify({'error': str(e)})

@app.route('/edit_teacher/<int:teacher_id>', methods=['PUT'])
@login_required
def edit_teacher(teacher_id):
    if (current_user.admin):
        try:
            teacher = Teachers.query.get(teacher_id)
            teacher.first_name = request.form.get('firstName')
            teacher.second_name = request.form.get('secondName')
            teacher.first_lastname = request.form.get('firstLastName')
            teacher.second_lastname = request.form.get('secondLastName')
            teacher.gender_id = request.form.get('gender')
            teacher.salutation_id = request.form.get('salutation')
            teacher.work_hours = request.form.get('hours')

            # Actualizar info del profesor a la base de datos
            db.session.commit()
            return jsonify({'message': 'Docente actualizado exitosamente! :D'})
        except Exception as e:
            return jsonify({'error': str(e)})
        
@app.route('/delete_teacher/<int:teacher_id>', methods=['DELETE'])
@login_required
def delete_teacher(teacher_id):
    if(current_user.admin):
        try:
            teacher = Teachers.query.get(teacher_id)
            if teacher:
                db.session.delete(teacher)
                db.session.commit()
                return jsonify({'message': 'Docente eliminado correctamente! :P'})
            else:
                return jsonify({'error': 'Docente no encontrado'})
        except Exception as e:
            return jsonify({'error': str(e)})