from datetime import datetime
from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
    

# Modelo para la tabla `parallels`
class Parallels(db.Model):
    parallel_id = db.Column(db.Integer, primary_key=True)
    parallel = db.Column(db.String(50), nullable=False)

# Modelo para la tabla `genders`
class Genders(db.Model):
    gender_id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(15), nullable=False)

# Modelo para la tabla `salutation`
class Salutation(db.Model):
    salutation_id = db.Column(db.Integer, primary_key=True)
    salutation = db.Column(db.String(25), nullable=False)

# Modelo para la tabla `teachers`
class Teachers(db.Model):
    teacher_id = db.Column(db.Integer, primary_key=True)
    salutation_id = db.Column(db.Integer, db.ForeignKey('salutation.salutation_id'), nullable=False)
    first_name = db.Column(db.String(25), nullable=False)
    second_name = db.Column(db.String(25), nullable=False)
    first_lastname = db.Column(db.String(25), nullable=False)
    second_lastname = db.Column(db.String(25), nullable=False)
    work_hours = db.Column(db.Integer, nullable=False)
    gender_id = db.Column(db.Integer, db.ForeignKey('genders.gender_id'), nullable=False)
    
    salutation = db.relationship('Salutation', backref='teachers', lazy=True)
    gender = db.relationship('Genders', backref='teachers', lazy=True)
    
# Modelo para la tabla `subjects`
class Subjects(db.Model):
    subject_id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(25), nullable=False)
    
class SubjectTeacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.subject_id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.teacher_id'), nullable=False)
    
# Modelo para la tabla `courses`
class Courses(db.Model):
    course_id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(50), nullable=False)
    contraction = db.Column(db.String(15), nullable=False)
    parallel_id = db.Column(db.Integer, db.ForeignKey('parallels.parallel_id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.teacher_id'), nullable=False)
    
    parallel = db.relationship('Parallels', backref='courses', lazy=True)
    tutor = db.relationship('Teachers', backref='courses', lazy=True)

# Modelo para la tabla `course_teacher`
class CourseTeacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.teacher_id'), nullable=False)

# Modelo para la tabla `course_subject`
class CourseSubject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.subject_id'), nullable=False)
    hours = db.Column(db.Integer, nullable=False)

# Modelo para la tabla `course_subject_teacher`
class CourseSubjectTeacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.subject_id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.teacher_id'), nullable=False)

# Modelo para la tabla `users`
class Users(db.Model, UserMixin):
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.teacher_id'), primary_key=True)
    user = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.LargeBinary, nullable=False)
    admin = db.Column(db.Boolean, default=False, nullable=False)
    teacher = db.relationship('Teachers', backref='users', lazy=True)
    
    def create_password(password):
        return generate_password_hash(password).encode('utf-8')
    
    def set_password(self, password, salt=None):
        self.password = generate_password_hash(password).encode('utf-8')
        
    def check_password(self, password):
        return check_password_hash(self.password.decode('utf-8'), password)
    
    def user_exists(username):
        # Consulta para verificar si el usuario existe
        existing_user = Users.query.filter_by(user=username).first()
        # Si existing_user no es None, significa que el usuario ya existe
        return existing_user is not None
    
    def get_id(self):
        return str(self.teacher_id)  # Convierte el ID a cadena si no lo es