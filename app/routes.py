from flask import render_template, redirect, url_for, flash, jsonify, request
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db
from datetime import datetime, timedelta
from app.forms import LoginForm
from app.models import ShedulConfig
from app.models import Parallels
from app.models import Salutation
from app.models import Subjects
from app.models import Teachers
from app.models import Courses
from app.models import CourseSubjectTeacher
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


#-----------
#ADMIN ROUTES
#-----------
@app.route('/config-sheduls')
@login_required
def configSheduls():
    shedul_config = ShedulConfig.query.first()
    days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    rows = int(shedul_config.hours) + int(shedul_config.breaks)
    breaks = shedul_config.break_hours.split(';')
    print([str(shedul_config.start_time.hour)])
    start_time = str(shedul_config.start_time.hour) + ':' + str(shedul_config.start_time.minute)
        
    for i in range(len(breaks)):
        breaks[i] = int(breaks[i])
    
    times = [timedelta(hours=shedul_config.start_time.hour, minutes=shedul_config.start_time.minute)]
    for i in range(int(shedul_config.hours) + int(shedul_config.breaks)):
        if i not in breaks:   
            times.append(times[i] + timedelta(minutes=shedul_config.hours_duration))
        else:
            times.append(times[i] + timedelta(minutes=shedul_config.break_duration))
        times[i] = str(times[i]).split(':')[0] + ':' + str(times[i]).split(':')[1]
        
    times[-1] = str(times[-1]).split(':')[0] + ':' + str(times[-1]).split(':')[1]
    return render_template('config-sheduls.html', shedul_config=shedul_config, days=days[0:shedul_config.days], rows = rows, breaks=breaks, start_time=start_time, times=times)

@app.route('/preview-config-sheduls', methods=['POST'])
@login_required
def previewConfigSheduls():

    days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    rows = int(request.form.get('hours')) + int(request.form.get('breaks'))
    breaks = request.form.get('breakHours').split(';')
    print([str(request.form.get('startTime').split(':')[0])])
        
    for i in range(len(breaks)):
        breaks[i] = int(breaks[i])
    
    times = [timedelta(hours=int(request.form.get('startTime').split(':')[0]), minutes=int(request.form.get('startTime').split(':')[1]))]
    for i in range(rows):
        if i not in breaks:
            times.append(times[i] + timedelta(minutes=int(request.form.get('hoursDuration'))))
        else:
            times.append(times[i] + timedelta(minutes=int(request.form.get('breakDuration'))))
        times[i] = str(times[i]).split(':')[0] + ':' + str(times[i]).split(':')[1]
        
    times[-1] = str(times[-1]).split(':')[0] + ':' + str(times[-1]).split(':')[1]
    print(times)
    previewInfo = {
        'days': days[0:int(request.form.get('days'))],
        'breaks': breaks,
        'times': times
    }
    return jsonify(previewInfo)

@app.route('/admin-teachers')
@login_required
def adminTeachers():
    teachers = Teachers.query.order_by(Teachers.first_name, Teachers.first_lastname).all()
    return render_template('admin-teachers.html', teachers=teachers, salutations=get_salutations(), genders=get_genders())

@app.route('/admin-subjects')
@login_required
def adminSubjects():
    subjects = Subjects.query.order_by(Subjects.subject).all()
    courses = Courses.query.all()
    return render_template('admin-subjects.html', subjects=subjects, courses=courses)

@app.route('/admin-courses')
@login_required
def adminCourses():
    courses = Courses.query.order_by(Courses.course).all()
    return render_template('admin-courses.html', courses=courses, parallels=get_parallels(), teachers=get_teachers())

@app.route('/admin-parallels')
@login_required
def adminParallels():
    parallels = Parallels.query.order_by(Parallels.parallel).all()
    return render_template('admin-parallels.html', parallels=parallels)

@app.route('/admin-sheduls')
@login_required
def adminSheduls():
    sheduls = 'EMPTY FOR THE MOMENT :('
    return render_template('admin-sheduls.html', sheduls=sheduls)

@app.route('/admin-salutations')
@login_required
def adminSalutation():
    salutations = Salutation.query.order_by(Salutation.salutation).all()
    return render_template('admin-salutations.html', salutations=salutations)

@app.route('/admin-users')
@login_required
def adminUsers():
    teacher_ids_to_exclude = [result.teacher_id for result in Users.query.all()]
    teachers = Teachers.query.filter(~Teachers.teacher_id.in_(teacher_ids_to_exclude)).order_by(Teachers.first_name, Teachers.first_lastname).all()
    users = Users.query.all()
    return render_template('admin-users.html', users=users, teachers=teachers)

@app.route('/admin-courses-subjects')
@login_required
def adminCoursesSubjects():
    courses = Courses.query.order_by(Courses.course).all()
    return render_template('admin-courses-subjects.html', courses=courses)

@app.route('/workloads/<int:course_id>')
@login_required
def workloads(course_id):
    subject_ids_to_exclude = [result.subject_id for result in CourseSubjectTeacher.query.filter_by(course_id=course_id).all()]
    subjects = Subjects.query.filter(~Subjects.subject_id.in_(subject_ids_to_exclude)).order_by(Subjects.subject).all()
    teachers = Teachers.query.order_by(Teachers.first_name, Teachers.first_lastname).all()
    course = Courses.query.get(course_id)
    workloads = CourseSubjectTeacher.query.filter_by(course_id=course_id).join(Subjects).order_by(Subjects.subject).all()
    return render_template('workloads.html', course=course, workloads=workloads, subjects=subjects, teachers=teachers)

#------------------
#<-----ADMIN ROUTES
#------------------

@app.route('/getSalutations')
@login_required
def get_salutations():
    if current_user.admin:
        return Salutation.query.order_by(Salutation.salutation).all()
  
    
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
        return Teachers.query.order_by(Teachers.first_name, Teachers.first_lastname).all()

#--------------------
#CRUD CONFIG HORARIOS
#--------------------



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
                'salutation_id': teacher.salutation_id,
                'salutation': teacher.salutation.salutation
            }
            return jsonify(teacher_info)
        else:
            raise Exception({'error': 'Profesor no encontrado'})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/get_teacher-info/<int:teacher_id>')
@login_required
def get_teacher_info(teacher_id):
    try:
        info = CourseSubjectTeacher.query.filter_by(teacher_id=teacher_id).all()
        if info:
            teacher_info = {
                'teacher_info': [[result.course.course + ' ' + result.course.parallel.parallel, result.subject.subject] for result in info]
            }
            return jsonify(teacher_info)
        else:
            print("ssssss")
            return ({'error': 'No se le asignaron cargas horarias'})
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
                raise Exception({'error': 'Docente no encontrado :('})
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
                'parallel': course.parallel.parallel,
                'tutor': course.teacher_id
            }
            return jsonify(course_info)
        else:
            raise Exception({'error': 'Curso no encontrado'})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/get_course-info/<int:course_id>')
@login_required
def get_course_info(course_id):
    try:
        info = CourseSubjectTeacher.query.filter_by(course_id=course_id).all()
        if info:
            course_info = {
                'course_info': [[result.subject.subject, result.teacher.salutation.salutation + ' ' + result.teacher.first_name + ' ' + result.teacher.first_lastname] for result in info]
            }
            return jsonify(course_info)
        else:
            print("ssssss")
            return ({'error': 'No se le asignaron cargas horarias'})
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
                raise Exception({'error': 'Curso no encontrado :('})
        except Exception as e:
            print(e)
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
            raise Exception({'error': 'Materia no encontrada :('})
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
            subject = Subjects.query.filter_by(subject_id=subject_id).first()
            if subject:
                db.session.delete(subject)
                db.session.commit()
                return jsonify({'message': 'Materia eliminada correctamente! :P'})
            else:
                raise Exception({'error': 'Materia no encontrada :('})
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
            raise Exception({'error': 'Salutación no encontrada :('})
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
                raise Exception({'error': 'Salutación no encontrada :('})
        except Exception as e:
            print(e)
            return jsonify({'error': str(e)})

#--------------   
#CRUD PARALELOS
#--------------
@app.route('/get_parallel/<int:parallel_id>')
@login_required
def get_parallel(parallel_id):
    try:
        parallel = Parallels.query.get(parallel_id)
        if parallel:
            parallel_info = {
                'parallel': parallel.parallel
            }
            return jsonify(parallel_info)
        else:
            raise Exception({'error': 'Paralelo no encontrado :('})
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
                raise Exception({'error': 'Paralelo no encontrado :('})
        except Exception as e:
            return jsonify({'error': str(e)})
        

#-------------   
#CRUD USUARIOS
#-------------
@app.route('/get_user/<int:user_id>')
@login_required
def get_user(user_id):
    try:
        user = Users.query.get(user_id)
        if user:
            user_info = {
                'teacher_id': user.teacher_id,
                'teacher': user.teacher.salutation.salutation + ' ' + user.teacher.first_name + ' ' + user.teacher.first_lastname,
                'user': user.user,
                'password': "",
                'admin': user.admin
            }
            print(user_info["teacher"])
            return jsonify(user_info)
        else:
            raise Exception(jsonify({'error': 'Usuario no encontrado :('}))
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/add_user', methods=['POST'])
@login_required
def add_user():
    if current_user.admin:
        try:
            user = request.form.get('user')
            if Users.user_exists(user):
                raise Exception("userexists")
            teacher = request.form.get('teacher')
            password = request.form.get('password')
            
            if request.form.get('admin') == 'on': admin = True
            else: admin = False
            
            new_user = Users(teacher_id=teacher, user=user, password=Users.create_password(password), admin=admin)

            # Agregar el profesor a la base de datos
            db.session.add(new_user)
            db.session.commit()
            return jsonify({'message': 'Usuario agregado exitosamente! :D'})
        except Exception as e:
            print(e)
            return jsonify({'error': str(e)})

@app.route('/edit_user/<int:user_id>', methods=['PUT'])
@login_required
def edit_user(user_id):
    if (current_user.admin):
        try:
            user = Users.query.get(user_id)
            pwd_hashed = Users.create_password(request.form.get('password'))
            user.user = request.form.get('user')
            user.password = pwd_hashed
            if request.form.get('admin') == 'on': user.admin = True
            else: user.admin = False
            
            # Actualizar info del usuario a la base de datos
            db.session.commit()
            return jsonify({'message': 'Usuario actualizado exitosamente! :D'})
        except Exception as e:
            
            return jsonify({'error': str(e)})
        
@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
@login_required
def delete_user(user_id):
    if(current_user.admin):
        try:
            user = Users.query.get(user_id)
            if user:
                db.session.delete(user)
                db.session.commit()
                return jsonify({'message': 'Usuario eliminado correctamente! :P'})
            else:
                return jsonify({'error': 'Usuario no encontrado :('})
        except Exception as e:
            return jsonify({'error': str(e)})
        
#--------------------
#CRUD CARGAS HORARIAS 
#--------------------
@app.route('/get_workload/<int:course_id>&<int:subject_id>')
@login_required
def get_workload(course_id, subject_id):
    try:
        workload = CourseSubjectTeacher.query.get([course_id, subject_id])
        if workload:
            info = {
                'subject': workload.subject.subject,
                'teacher': workload.teacher_id,
                'hours': workload.hours
            }
            return jsonify(info)
        else:
            raise Exception(jsonify({'error': 'Carga Horaria no encontrada :('}))
    except Exception as e:
        return jsonify({'error': str(e)})
 
@app.route('/add_workload', methods=['POST'])
@login_required
def add_workload():
    if current_user.admin:
        try:
            subject_id = request.form.get('subject')
            course_id = request.form.get('course')
            teacher_id = request.form.get('teacher')
            hours = request.form.get('hours')
            
            new_course_subject = CourseSubjectTeacher(course_id =course_id, subject_id=subject_id, teacher_id=teacher_id, hours=hours)

            # Agregar el profesor a la base de datos
            db.session.add(new_course_subject)
            db.session.commit()
            return jsonify({'message': 'Carga horaria agregada exitosamente! :D'})
        except Exception as e:
            print(e)
            return jsonify({'error': str(e)})

@app.route('/edit_workload/<int:course_id>&<int:subject_id>', methods=['PUT'])
@login_required
def edit_workload(course_id, subject_id):
    if (current_user.admin):
        try:
            workload = CourseSubjectTeacher.query.get([course_id, subject_id])
            workload.hours = request.form.get('hours')
            workload.teacher_id = request.form.get('teacher')
            
            # Actualizar info del usuario a la base de datos
            db.session.commit()
            return jsonify({'message': 'Carga horaria actualizada exitosamente! :D'})
        except Exception as e:
            
            return jsonify({'error': str(e)})
        
@app.route('/delete_workload/<int:course_id>&<int:subject_id>', methods=['DELETE'])
@login_required
def delete_workload(course_id, subject_id):
    if(current_user.admin):
        try:
            workload = CourseSubjectTeacher.query.get([course_id, subject_id])
            if workload:
                db.session.delete(workload)
                db.session.commit()
                return jsonify({'message': 'Carga horaria eliminada correctamente! :P'})
            else:
                return jsonify({'error': 'Usuario no encontrado :('})
        except Exception as e:
            return jsonify({'error': str(e)})