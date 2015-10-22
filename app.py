from flask import Flask, request, jsonify, render_template, abort, make_response, g, session, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

app = Flask(__name__)
db = SQLAlchemy(app)
auth = HTTPBasicAuth()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ubflow:ubflow@localhost/ubflowdb'
app.config['SECRET_KEY'] = 'The arsonist had oddly shaped feet'
db.create_all()

'''-----------------------------------------------
        User Class
--------------------------------------------------'''
class User(db.Model):
    __tablename__ = 'user'

    ID = db.Column(db.Integer, primary_key=True)
    USERNAME = db.Column(db.String(50))
    PASS_HASH = db.Column(db.String(128))
    FIRST_NAME = db.Column(db.String(50))
    LAST_NAME = db.Column(db.String(50))
    DEGREE = db.Column(db.String(50))


    def hash_password(self, password):
        self.PASS_HASH = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.PASS_HASH)

    def generate_auth_token(self, expiration=600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.ID})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data['ID'])
        return user

    def __init__(self, username, pass_hash, first_name, last_name, degree):
        self.USERNAME = username
        self.PASS_HASH = pass_hash
        self.FIRST_NAME = first_name
        self.LAST_NAME = last_name
        self.DEGREE = degree

    def __repr__(self):
        return '<student {}'.format(self.USERNAME)


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
    TITLE = db.Column(db.String(50),nullable=False)
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
    SEMESTER = db.Column(db.String(50), nullable=True)
    PRE_REQ1 = db.Column(db.String(50), nullable=True)
    PRE_REQ2 = db.Column(db.String(50), nullable=True)
    PRE_REQ3 = db.Column(db.String(50), nullable=True)
    PRE_REQ4 = db.Column(db.String(50), nullable=True)
    PRE_REQ5 = db.Column(db.String(50), nullable=True)
    DEGREE = db.Column(db.String(50), nullable=True)

    def __init__(self, ubclass, title, department, section, type, days, time, building, room_number, location, professor, status, reserved, semester,pre1,pre2,pre3,pre4,pre5,degree):

        self.UBCLASS = ubclass
        self.TITLE = title
        self.DEPARTMENT = department
        self.SECTION = section
        self.TYPE = type
        self.DAYS = days
        self.TIME = time
        self.BUILDING = building
        self.ROOM_NUMBER = room_number
        self.LOCATION = location
        self.PROFESSOR = professor
        self.STATUS = status
        self.RESERVED = reserved
        self.SEMESTER = semester
        self.PRE_REQ1 = pre1
        self.PRE_REQ2 = pre2
        self.PRE_REQ3 = pre3
        self.PRE_REQ4 = pre4
        self.PRE_REQ5 = pre5
        self.DEGREE = degree

    def __repr__(self):
        return '<class {}'.format(self.UBCLASS)


'''-----------------------------------------------
        Recitations Class
-----------------------------------------------'''
class UBRecitation(db.Model):
    __tablename__ = "ubrecitations"

    ID = db.Column(db.Integer, primary_key=True)
    UBCLASS = db.Column(db.String(50), nullable=False)
    HUB_ID = db.Column(db.Integer,nullable=False)
    RECITATION_ID = db.Column(db.Integer, db.ForeignKey('ubclasses.ID'))
    SECTION = db.Column(db.String(50), nullable=False)
    TYPE = db.Column(db.String(50), nullable=False)
    DAYS = db.Column(db.String(50), nullable=False)
    TIME = db.Column(db.String(50), nullable=False)
    BUILDING = db.Column(db.String(50), nullable=False)
    ROOM_NUMBER = db.Column(db.String(50), nullable=False)
    LOCATION = db.Column(db.String(50), nullable=False)
    STATUS = db.Column(db.String(50), nullable=False)
    RESERVED = db.Column(db.String(50), nullable=False)


    def __init__(self, ubclass, hub_id, recitation, section, type, days, time, building, room_number, location, status, reserved, semester):
        self.UBCLASS = ubclass
        self.HUB_ID = hub_id
        self.RECITATION_ID = recitation
        self.SECTION = section
        self.TYPE = type
        self.DAYS = days
        self.TIME = time
        self.BUILDING = building
        self.ROOM_NUMBER = room_number
        self.LOCATION = location
        self.STATUS = status
        self.RESERVED = reserved
        self.SEMESTER = semester

    def __repr__(self):
        return '<recitation {}'.format(self.RECITATION_ID)


'''-----------------------------------------------
        Schedule Class
-----------------------------------------------'''
class UBSchedule(db.Model):
    __tablename__ = 'schedule'

    ID = db.Column(db.Integer, primary_key=True)
    USER_ID = db.Column(db.Integer, db.ForeignKey('user.ID'))




'''-----------------------------------------------
        DEGREE COURSE CLASS
-----------------------------------------------'''
class Degree(db.Model):
    __tablename__ = 'degree'

    ID = db.Column(db.Integer, primary_key=True)
    UBCLASS = db.Column(db.String(50), nullable=False)
    TITLE = db.Column(db.String(50), nullable=False)
    SEM_INDEX = db.Column(db.Integer, nullable=False)
    LINK = db.Column(db.String(100), nullable=True)
    PRE_REQ1 = db.Column(db.String(50), nullable=True)
    PRE_REQ2 = db.Column(db.String(50), nullable=True)
    PRE_REQ3 = db.Column(db.String(50), nullable=True)
    PRE_REQ4 = db.Column(db.String(50), nullable=True)
    PRE_REQ5 = db.Column(db.String(50), nullable=True)

    def __init__(self,ubclass,title,sem_index,link,pre1,pre2,pre3,pre4,pre5):
        self.UBCLASS = ubclass
        self.TITLE = title
        self.SEM_INDEX = sem_index
        self.LINK = link
        self.PRE_REQ1 = pre1
        self.PRE_REQ2 = pre2
        self.PRE_REQ3 = pre3
        self.PRE_REQ4 = pre4
        self.PRE_REQ5 = pre5

    def __repr__(self):
        return '<degree'.format(self.UBCLASS)



'''-----------------------------------------------
       Register a New User
-----------------------------------------------'''
@app.route('/register', methods=['GET','POST'])
def new_user():
    if request.method=='GET':
        return render_template("register.html")
    if request.method=='POST':
        username = request.form['USERNAME']
        password = request.form['PASSWORD']
        first_name = request.form['FIRST_NAME']
        last_name = request.form['LAST_NAME']
        degree = request.form['DEGREE']

        if username is None or password is None:
            abort(400)  # missing arguments
        if User.query.filter_by(USERNAME=username).first() is not None:
            abort(400)  # existing user

        temp_user = User(username,password,first_name,last_name,degree)
        temp_user.hash_password(password)
        db.session.add(temp_user)
        db.session.commit()
        profile()
        #return redirect(url_for('profile'))
        return render_template('profile.html', username=username)


'''-----------------------------------------------
      Login
-----------------------------------------------'''
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login_user():
    error = ""
    if request.method=='GET':
        return render_template("login.html",input_error=error)

    if request.method=='POST':
        username = request.form['USERNAME']
        password = request.form['PASSWORD']
        if username is None or password is None:
            abort(400)  # missing arguments
        user = User.query.filter_by(USERNAME=username).first()
        if not user or not user.verify_password(password):
            error = "Sorry, who are you again?"
            return render_template("login.html", input_error=error)
    return profile()


'''-----------------------------------------------
      ROUTE: Profile
-----------------------------------------------'''

@app.route('/profile', methods=['GET'])
def profile():
    result = UBClasses.query.filter_by(TYPE="LEC").all()

    return render_template("profile.html",username="sethkara")


@app.route('/getnextclassgroup/search', methods=['GET','POST'])
def getSearch():
    if request.method == 'POST':
        ubclass = request.json['course']
        dept = request.json['dept']
        results = UBClasses.query.filter_by(UBCLASS=ubclass).all()


    if request.method == 'GET':
        results = UBClasses.query.all()

    if len(results) == 0:
        data = []
        no_data = {'UBCLASS':"No Such Class"}
        data.append(no_data)
        return jsonify(classes=data)
    else:
        rec = {}
        json_results = []
        json_rec = []
        for result in results:
             recitations = UBRecitation.query.filter_by(RECITATION_ID=result.ID).all()
             for recitation in recitations:
                  rec = {'ID': recitation.ID,
                         'UBCLASS' : recitation.UBCLASS,
                         'REC_ID': recitation.RECITATION_ID,
                         'SECTION': recitation.SECTION,
                         'TYPE': recitation.TYPE,
                         'DAYS': recitation.DAYS,
                         'TIME': recitation.TIME,
                         'BUILDING': recitation.BUILDING,
                         'ROOM_NUMBER': recitation.ROOM_NUMBER,
                         'LOCATION': recitation.LOCATION,
                         'STATUS': recitation.STATUS,
                         'RESERVED': recitation.RESERVED,
                  }
                  json_rec.append(rec)
             d = {'ID': result.ID,
                  'UBCLASS': result.UBCLASS,
                  'TITLE' : result.TITLE,
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
                  'SEMESTER': result.SEMESTER,
                  'RECITATION': json_rec
                }
             json_rec = []
             json_results.append(d)
        return jsonify(classes=json_results)


@app.route('/getnextclassgroup', methods=['GET'])
def getClassGroup():
    if request.method == 'GET':
        results = UBClasses.query.filter_by(DEPARTMENT="CSE").all()
    rec = {}
    json_results = []
    json_rec = []
    for result in results:
         recitations = UBRecitation.query.filter_by(RECITATION_ID=result.ID).all()
         for recitation in recitations:
              rec = {'ID': recitation.ID,
                     'UBCLASS' : recitation.UBCLASS,
                     'REC_ID': recitation.RECITATION_ID,
                     'SECTION': recitation.SECTION,
                     'TYPE': recitation.TYPE,
                     'DAYS': recitation.DAYS,
                     'TIME': recitation.TIME,
                     'BUILDING': recitation.BUILDING,
                     'ROOM_NUMBER': recitation.ROOM_NUMBER,
                     'LOCATION': recitation.LOCATION,
                     'STATUS': recitation.STATUS,
                     'RESERVED': recitation.RESERVED,
              }
              json_rec.append(rec)
         d = {'ID': result.ID,
              'UBCLASS': result.UBCLASS,
              'TITLE' : result.TITLE,
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
              'SEMESTER': result.SEMESTER,
              'RECITATION': json_rec
            }
         json_rec = []
         json_results.append(d)

    return jsonify(classes=json_results)




@app.route('/getfirstclassgroup', methods=['GET'])
def getFirstClassGroup():
    if request.method == 'GET':
        results = UBClasses.query.limit(10).offset(0).all()
    rec = {}
    json_results = []
    json_rec = []
    for result in results:
        recitations = UBRecitation.query.filter_by(RECITATION_ID=result.ID).all()
        for recitation in recitations:
            rec = {'ID': recitation.ID,
                   'REC_ID': recitation.RECITATION_ID,
                   'UBCLASS' : recitation.UBCLASS,
                   'SECTION': recitation.SECTION,
                   'TYPE': recitation.TYPE,
                   'DAYS': recitation.DAYS,
                   'TIME': recitation.TIME,
                   'BUILDING': recitation.BUILDING,
                   'ROOM_NUMBER': recitation.ROOM_NUMBER,
                   'LOCATION': recitation.LOCATION,
                   'STATUS': recitation.STATUS,
                   'RESERVED': recitation.RESERVED,
            }
            json_rec.append(rec)
        d = {'ID': result.ID,
             'UBCLASS': result.UBCLASS,
             'TITLE' : result.TITLE,
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
             'SEMESTER': result.SEMESTER,
             'RECITATION': json_rec
            }
        json_rec = []
        json_results.append(d)
    return jsonify(classes=json_results)


@app.route('/degreeinfo', methods=['GET'])
def degree_info():
    if request.method == 'GET':
        courses = Degree.query.all()
    json_results = []
    for course in courses:
        d = {'ID': course.ID,
             'UBCLASS': course.UBCLASS,
             'SEM_INDEX': course.SEM_INDEX,
             'LINK': course.LINK}
        json_results.append(d)
    return jsonify(classes=json_results)



'''-----------------------------------------------
      Error Handling Page
-----------------------------------------------'''
@app.route('/flowsheet')
def flowsheet():
    return render_template("flowsheet.html")


'''-----------------------------------------------
      ROUTE: All Professors
-----------------------------------------------'''
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


'''-----------------------------------------------
      ROUTE: Single Professor
-----------------------------------------------'''
@app.route('/professor/<int:professor_id>', methods=['GET'])
def getProfessor(professor_id):
    if request.method == 'GET':
        result = Professor.query.filter_by(ID=professor_id).first()
        if result is None:
            return "false"

        d = {'ID': result.ID,
             'FIRST_NAME': result.FIRST_NAME}
    return jsonify(professor=d)


'''-----------------------------------------------
      ROUTE: All Classes
-----------------------------------------------'''
@app.route('/classes', methods=['GET'])
def get_classes():
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


'''-----------------------------------------------
      Token Generator
-----------------------------------------------'''
@app.route('/api/token')
@auth.login_required
def get_auth_token():
    """Generate Authentication Token to send instead of username and password"""
    token = g.user.generate_auth_token()
    return jsonify({'token': token.decode('ascii')})


'''-----------------------------------------------
      Auth Testing
-----------------------------------------------'''
@app.route('/api/resource')
@auth.login_required
def get_resource():
    """FOR AUTHENTICATION TESTING"""
    print "I made it here"
    return jsonify({'data': 'Hello, %s!' % g.user.username})


'''-----------------------------------------------
      Verify Password/Username
-----------------------------------------------'''
@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(USERNAME=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


'''-----------------------------------------------
      Error Handling Page
-----------------------------------------------'''
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'BAD REQUEST:Invalid format.'}), 400)




if __name__ == '__main__':
    app.run(debug=True)
