from flask import render_template
from app import app, db
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

@app.route('/')
def index():
    user = "Miguel Gómez"
    return render_template('index.html', user=user)
    
@app.route('/admin-teachers')
def adminTeachers():
    teachers = Teachers.query.all()
    return render_template('admin-teachers.html', teachers=teachers)

@app.route('/admin-subjects')
def adminSubjects():
    subjects = Subjects.query.all()
    return render_template('admin-subjects.html', subjects=subjects)

@app.route('/admin-courses')
def adminCourses():
    courses = Courses.query.all()
    return render_template('admin-courses.html', courses=courses)

@app.route('/admin-sheduls')
def adminSheduls():
    sheduls = 'EMPTY FOR THE MOMENT :('
    return render_template('admin-sheduls.html', sheduls=sheduls)

@app.route('/admin-salutation')
def adminSalutation():
    salutations = Salutation.query.all()
    print(salutations)
    return render_template('admin-salutation.html', salutations=salutations)