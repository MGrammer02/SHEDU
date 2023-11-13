from datetime import datetime
from app import db

    
# Modelo para la tabla `courses`
class Courses(db.Model):
    course_id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(50), nullable=False)
    paralel_id = db.Column(db.Integer, db.ForeignKey('paralels.paralel_id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.teacher_id'), nullable=False)

# Modelo para la tabla `course_subject`
class CourseSubject(db.Model):
    course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'), primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.subject_id'), primary_key=True)
    hours = db.Column(db.Integer, nullable=False)

# Modelo para la tabla `course_subject_teacher`
class CourseSubjectTeacher(db.Model):
    course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'), primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.subject_id'), primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.teacher_id'), primary_key=True)

# Modelo para la tabla `course_teacher`
class CourseTeacher(db.Model):
    course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'), primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.teacher_id'), primary_key=True)

# Modelo para la tabla `genders`
class Genders(db.Model):
    gender_id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(11), nullable=False)

# Modelo para la tabla `paralels`
class Paralels(db.Model):
    paralel_id = db.Column(db.Integer, primary_key=True)
    paralel = db.Column(db.String(50), nullable=False)

# Modelo para la tabla `salutation`
class Salutation(db.Model):
    salutation_id = db.Column(db.Integer, primary_key=True)
    salutation = db.Column(db.String(25), nullable=False)

# Modelo para la tabla `subjects`
class Subjects(db.Model):
    subject_id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(11), nullable=False)

# Modelo para la tabla `subject_teacher`
class SubjectTeacher(db.Model):
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.subject_id'), primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.teacher_id'), primary_key=True)

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