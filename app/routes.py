from flask import render_template, redirect, url_for, flash, jsonify, request
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db
from app.forms import LoginForm
from app.models import Parallels
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
            return redirect(url_for('home'))  # Cambia 'index' con la ruta a la que deseas redirigir después del inicio de sesión.

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

#-----------
#ADMIN ROUTES
#-----------
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
    return render_template('admin-courses.html', courses=courses, parallels=get_parallels(), teachers=get_teachers())

@app.route('/admin-parallels')
@login_required
def adminParallels():
    parallels = Parallels.query.all()
    return render_template('admin-parallels.html', parallels=parallels)

@app.route('/admin-sheduls')
@login_required
def adminSheduls():
    sheduls = 'EMPTY FOR THE MOMENT :('
    return render_template('admin-sheduls.html', sheduls=sheduls)

@app.route('/admin-salutations')
@login_required
def adminSalutation():
    salutations = Salutation.query.all()
    return render_template('admin-salutations.html', salutations=salutations)

#------------------
#<-----ADMIN ROUTES
#------------------

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

@app.route('/getParalles')
@login_required
def get_parallels():
    if current_user.admin:
        return Parallels.query.all()
    
@app.route('/getTeachers')
@login_required
def get_teachers():
    if current_user.admin:
        return Teachers.query.all()

#-------------   
#CRUD DOCENTES
#-------------
@app.route('/get_teacher/<int:teacher_id>')
@login_required
def get_teacher(teacher_id):
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
                return jsonify({'error': 'Docente no encontrado :('})
        except Exception as e:
            return jsonify({'error': str(e)})
    
#----------- 
#CRUD CURSOS
#-----------
@app.route('/get_course/<int:course_id>')
@login_required
def get_course(course_id):
    try:
        course = Courses.query.get(course_id)
        if course:
            course_info = {
                'course': course.course,
                'contraction': course.contraction,
                'parallel_id': course.parallel_id,
                'tutor': course.teacher_id
            }
            return jsonify(course_info)
        else:
            return jsonify({'error': 'Curso no encontrado'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/add_course', methods=['POST'])
@login_required
def add_course():
    if current_user.admin:
        try:
            course = request.form.get('course')
            contraction = request.form.get('contraction')
            parallel = request.form.get('parallel')
            tutor = request.form.get('tutor')
            
            new_course = Courses(course=course, contraction=contraction, parallel_id=parallel, teacher_id=tutor)

            # Agregar el curso a la base de datos
            db.session.add(new_course)
            db.session.commit()
            return jsonify({'message': 'Curso agregado exitosamente! :D'})
        except Exception as e:
            return jsonify({'error': str(e)})

@app.route('/edit_course/<int:course_id>', methods=['PUT'])
@login_required
def edit_course(course_id):
    if (current_user.admin):
        try:
            course = Courses.query.get(course_id)
            course.course = request.form.get('course')
            course.contraction = request.form.get('contraction')
            course.parallel_id = request.form.get('parallel')
            course.teacher_id = request.form.get('tutor')

            # Actualizar info del curso a la base de datos
            db.session.commit()
            return jsonify({'message': 'Curso actualizado exitosamente! :D'})
        except Exception as e:
            return jsonify({'error': str(e)})
        
@app.route('/delete_course/<int:course_id>', methods=['DELETE'])
@login_required
def delete_course(course_id):
    if(current_user.admin):
        try:
            course = Courses.query.get(course_id)
            if course:
                db.session.delete(course)
                db.session.commit()
                return jsonify({'message': 'Curso eliminado correctamente! :P'})
            else:
                return jsonify({'error': 'Curso no encontrado :('})
        except Exception as e:
            return jsonify({'error': str(e)})

#-------------   
#CRUD MATERIAS
#-------------
@app.route('/get_subject/<int:subject_id>')
@login_required
def get_subject(subject_id):
    print(subject_id)
    try:
        subject = Subjects.query.get(subject_id)
        if subject:
            subject_info = {
                'subject': subject.subject
            }
            return jsonify(subject_info)
        else:
            return jsonify({'error': 'Materia no encontrada :('})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/add_subject', methods=['POST'])
@login_required
def add_subject():
    if current_user.admin:
        try:
            subject = request.form.get('subject')
            new_subject = Subjects(subject=subject)

            # Agregar el profesor a la base de datos
            db.session.add(new_subject)
            db.session.commit()
            return jsonify({'message': 'Materia agregada exitosamente! :D'})
        except Exception as e:
            return jsonify({'error': str(e)})

@app.route('/edit_subject/<int:subject_id>', methods=['PUT'])
@login_required
def edit_subject(subject_id):
    if (current_user.admin):
        try:
            subject = Subjects.query.get(subject_id)
            subject.subject = request.form.get('subject')
            
            # Actualizar info del profesor a la base de datos
            db.session.commit()
            return jsonify({'message': 'Docente actualizado exitosamente! :D'})
        except Exception as e:
            return jsonify({'error': str(e)})
        
@app.route('/delete_subject/<int:subject_id>', methods=['DELETE'])
@login_required
def delete_subject(subject_id):
    if(current_user.admin):
        try:
            subject = Subjects.query.get(subject_id)
            if subject:
                db.session.delete(subject)
                db.session.commit()
                return jsonify({'message': 'Materia eliminada correctamente! :P'})
            else:
                return jsonify({'error': 'Materia no encontrada :('})
        except Exception as e:
            return jsonify({'error': str(e)})
        
#-----------------
#CRUD SALUTACIONES
#-----------------
@app.route('/get_salutation/<int:salutation_id>')
@login_required
def get_salutation(salutation_id):
    print(salutation_id)
    try:
        salutation = Salutation.query.get(salutation_id)
        if salutation:
            salutation_info = {
                'salutation': salutation.salutation
            }
            return jsonify(salutation_info)
        else:
            return jsonify({'error': 'Salutación no encontrada :('})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/add_salutation', methods=['POST'])
@login_required
def add_salutation():
    if current_user.admin:
        try:
            salutation = request.form.get('salutation')
            new_salutation = Salutation(salutation=salutation)

            # Agregar el profesor a la base de datos
            db.session.add(new_salutation)
            db.session.commit()
            return jsonify({'message': 'Salutación agregada exitosamente! :D'})
        except Exception as e:
            return jsonify({'error': str(e)})

@app.route('/edit_salutation/<int:salutation_id>', methods=['PUT'])
@login_required
def edit_salutation(salutation_id):
    if (current_user.admin):
        try:
            salutation = Salutation.query.get(salutation_id)
            salutation.salutation = request.form.get('salutation')
            
            # Actualizar info del profesor a la base de datos
            db.session.commit()
            return jsonify({'message': 'Salutación actualizado exitosamente! :D'})
        except Exception as e:
            return jsonify({'error': str(e)})
        
@app.route('/delete_salutation/<int:salutation_id>', methods=['DELETE'])
@login_required
def delete_salutation(salutation_id):
    if(current_user.admin):
        try:
            salutation = Salutation.query.get(salutation_id)
            if salutation:
                db.session.delete(salutation)
                db.session.commit()
                return jsonify({'message': 'Salutación eliminada correctamente! :P'})
            else:
                return jsonify({'error': 'Salutación no encontrada :('})
        except Exception as e:
            return jsonify({'error': str(e)})

#--------------   
#CRUD PARALELOS
#--------------
@app.route('/get_parallel/<int:parallel_id>')
@login_required
def get_parallel(parallel_id):
    print(parallel_id)
    try:
        parallel = Parallels.query.get(parallel_id)
        if parallel:
            parallel_info = {
                'parallel': parallel.parallel
            }
            return jsonify(parallel_info)
        else:
            return jsonify({'error': 'Paralelo no encontrada :('})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/add_parallel', methods=['POST'])
@login_required
def add_parallel():
    if current_user.admin:
        try:
            parallel = request.form.get('parallel')
            new_parallel = Parallels(parallel=parallel)

            # Agregar el profesor a la base de datos
            db.session.add(new_parallel)
            db.session.commit()
            return jsonify({'message': 'Paralelo agregado exitosamente! :D'})
        except Exception as e:
            return jsonify({'error': str(e)})

@app.route('/edit_parallel/<int:parallel_id>', methods=['PUT'])
@login_required
def edit_parallel(parallel_id):
    if (current_user.admin):
        try:
            parallel = Parallels.query.get(parallel_id)
            parallel.parallel = request.form.get('parallel')
            
            # Actualizar info del profesor a la base de datos
            db.session.commit()
            return jsonify({'message': 'Paralelo actualizado exitosamente! :D'})
        except Exception as e:
            return jsonify({'error': str(e)})
        
@app.route('/delete_parallel/<int:parallel_id>', methods=['DELETE'])
@login_required
def delete_parallel(parallel_id):
    if(current_user.admin):
        try:
            parallel = Parallels.query.get(parallel_id)
            if parallel:
                db.session.delete(parallel)
                db.session.commit()
                return jsonify({'message': 'Paralelo eliminado correctamente! :P'})
            else:
                return jsonify({'error': 'Paralelo no encontrado :('})
        except Exception as e:
            return jsonify({'error': str(e)})