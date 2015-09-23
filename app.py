from flask import Flask, request, jsonify, render_template
from flask_bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bootstrap(app)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ubflow@localhost/ubflowdb'



'''-----------------------------------------------
        Professor Class
-----------------------------------------------'''
class Professor(db.Model):
    __tablename__ = "professor"

    ID = db.Column(db.Integer, primary_key=True)
    FIRST_NAME = db.Column(db.String(50), nullable=False)
    LAST_NAME = db.Column(db.String(50), nullable=False)
    DEPARTMENT = db.Column(db.String(100), nullable=True)

    def __init__(self, username,):
        self.FIRST_NAME = username

    def __repr__(self):
        return '<title {}'.format(self.FIRST_NAME)



'''-----------------------------------------------
        Classes Class
-----------------------------------------------'''
class UBClasses(db.Model):
    __tablename__ = "ubclasses"

    ID = db.Column(db.Integer, primary_key=True)
    UBCLASS = db.Column(db.String(50), nullable=False)
    DEPARTMENT = db.Column(db.String(50), nullable=False)
    SECTION = db.Column(db.String(50), nullable=False)
    TYPE = db.Column(db.String(50), nullable=False)
    DAYS = db.Column(db.String(50), nullable=False)
    TIME = db.Column(db.String(50), nullable=False)
    BUILDING = db.Column(db.String(50), nullable=False)
    ROOM_NUMBER = db.Column(db.String(50), nullable=False)
    LOCATION = db.Column(db.String(50), nullable=False)
    PROFESSOR_ID = db.Column(db.Integer, db.ForeignKey('professor.ID'))
    PROFESSOR = db.Column(db.String(50), nullable=False)
    STATUS = db.Column(db.String(50), nullable=False)
    RESERVED = db.Column(db.String(50), nullable=False)
    SEMESTER = db.Column(db.String(50), nullable=False)

    def __init__(self, id, ubclass, department, section, type, days, time, building, room_number, location, professor_id, professor, status, reserved, semester):
        self.ID = id
        self.UBCLASS = ubclass
        self.DEPARTMENT = department
        self.SECTION = section
        self.TYPE = type
        self.DAYS = days
        self.TIME = time
        self.BUILDING = building
        self.ROOM_NUMBER = room_number
        self.LOCATION = location
        self.PROFESSOR_ID = professor_id
        self.PROFESSOR = professor
        self.STATUS = status
        self.RESERVED = reserved
        self.SEMESTER = semester

    def __repr__(self):
        return '<class {}'.format(self.UBCLASS)



'''-----------------------------------------------
        User Class
--------------------------------------------------'''
class User(db.Model):
    __tablename__ = 'user'

    ID = db.Column(db.Integer, primary_key=True)
    USERNAME = db.Column(db.String(50), nullable=False)
    FIRST_NAME = db.Column(db.String(50), nullable=False)
    LAST_NAME = db.Column(db.String(50), nullable=False)
    DEGREE = db.Column(db.String(50),nullable=True)

    def __init__(self, id, username, first_name, last_name, degree):
        self.ID = id
        self.USERNAME = username
        self.FIRST_NAME = first_name
        self.LAST_NAME = last_name
        self.DEGREE = degree

    def __repr__(self):
        return '<student {}'.format(self.USERNAME)


'''-----------------------------------------------
        Schedule Class
-----------------------------------------------'''
class Schedule(db.Model):
    __tablename__ = 'schedule'

    ID = db.Column(db.Integer, primary_key=True)
    USER_ID = db.Column(db.Integer, db.ForeignKey('user.ID'))





@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)



@app.route('/professor', methods=['GET'])
def getProfessors():
    if request.method == 'GET':
        results = Professor.query.limit(10).offset(0).all()

    json_results = []
    for result in results:
        d = {'ID': result.ID,
             'FIRST_NAME': result.FIRST_NAME,
             'LAST_NAME': result.LAST_NAME,
             'DEPARTMENT': result.DEPARTMENT}
        json_results.append(d)
    return jsonify(professors=json_results)


@app.route('/professor/<int:professor_id>', methods=['GET'])
def getProfessor(professor_id):
    if request.method == 'GET':
        result = Professor.query.filter_by(ID=professor_id).first()
        if result is None:
            return "false"

        d = {'ID': result.ID,
             'FIRST_NAME': result.FIRST_NAME}
    return jsonify(professor=d)
 #   return render_template('hello.html', name=result.FIRST_NAME)


@app.route('/classes', methods=['GET'])
def getClasses():
    if request.method == 'GET':
        results = UBClasses.query.limit(10).offset(0).all()

    json_results = []
    for result in results:
        d = {'ID': result.ID,
             'CLASS': result.UBCLASS,
             'DEPARTMENT': result.DEPARTMENT,
             'SECTION': result.SECTION,
             'TYPE': result.TYPE,
             'DAYS': result.DAYS,
             'TIME': result.TIME,
             'BUILDING': result.BUILDING,
             'ROOM_NUMBER': result.ROOM_NUMBER,
             'LOCATION': result.LOCATION,
             'PROFESSOR_ID': result.PROFESSOR_ID,
             'PROFESSOR': result.PROFESSOR,
             'STATUS': result.STATUS,
             'RESERVED': result.RESERVED,
             'SEMESTER': result.SEMESTER}
        json_results.append(d)
    return jsonify(classes=json_results)



if __name__ == '__main__':
    app.run()
