from flask import Flask, request, jsonify, render_template, abort, make_response, g, session
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
        Classes Class
-----------------------------------------------'''
class UBRecitation(db.Model):
    __tablename__ = "ubrecitations"

    ID = db.Column(db.Integer, primary_key=True)
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


    def __init__(self, id, recitation, section, type, days, time, building, room_number, location, status, reserved, semester):
        self.ID = id
        self.RECITATION_ID = ubclass
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
class Schedule(db.Model):
    __tablename__ = 'schedule'

    ID = db.Column(db.Integer, primary_key=True)
    USER_ID = db.Column(db.Integer, db.ForeignKey('user.ID'))



'''-----------------------------------------------
      ROUTE: Index Page
-----------------------------------------------'''
@app.route('/index.html', methods=['POST'])
@app.route('/index', methods=['POST'])
@app.route('/index/<name>', methods=['POST'])
def index(name=None):
    return render_template('index.html', name=name)



'''-----------------------------------------------
      ROUTE: Register
-----------------------------------------------'''
@app.route('/')
@app.route('/register')
def register():
    return render_template('register.html')

'''-----------------------------------------------
       Register a New User
-----------------------------------------------'''
@app.route('/api/users/register', methods=['POST'])
def new_user():
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
        return render_template('profile.html', username=username)


'''-----------------------------------------------
      ROUTE: Login
-----------------------------------------------'''
@app.route('/login')
def login():
    return render_template('login.html')

'''-----------------------------------------------
      Login
-----------------------------------------------'''
@app.route('/api/users/login', methods=['GET', 'POST'])
def login_user():
    if request.method=='POST':
        username = request.form['USERNAME']
        password = request.form['PASSWORD']
        if username is None or password is None:
            abort(400)  # missing arguments
        #if User.query.filter_by(USERNAME=username).first() is not None:
        #    abort(400)  # not a user
        return render_template("profile.html", name=username)


'''-----------------------------------------------
      ROUTE: Profile
-----------------------------------------------'''
@app.route('/profile')
def profile():
    class1_slot_1 = 'empty'
    class1_slot_2 = 'empty'
    class1_slot_3 = 'empty'
    result = UBClasses.query.filter_by(TYPE="LEC").all()



    if result[0].DAYS == 'MWF':
        class1_slot_1 = 'Mon'
        class1_slot_2 = 'Wed'
        class1_slot_3 = 'Fri'
    elif result[0].DAYS == 'TR':
        class1_slot_1 = 'Tue'
        class1_slot_2 = 'Thu'
    elif result[0].DAYS == "M":
        class1_slot_1 = "Mon"
    elif result[0].DAYS == "T":
        class1_slot_1 = "Tue"
    elif result[0].DAYS == "R":
        class1_slot_1 = "Thu"


    session[0] = class1_slot_1 + '_' + result[0].TIME
    session[1] = class1_slot_2 + '_' + result[0].TIME
    session[2] = class1_slot_3 + '_' + result[0].TIME

    class1_slot_1 = 'empty'
    class1_slot_2 = 'empty'
    class1_slot_3 = 'empty'


    if result[1].DAYS == 'MWF':
        class1_slot_1 = 'Mon'
        class1_slot_2 = 'Wed'
        class1_slot_3 = 'Fri'
    elif result[1].DAYS == 'TR':
        class1_slot_1 = 'Tue'
        class1_slot_2 = 'Thu'
    elif result[1].DAYS == "M":
        class1_slot_1 = "Mon"
    elif result[1].DAYS == "T":
        class1_slot_1 = "Tue"
    elif result[1].DAYS == "R":
        class1_slot_1 = "Thu"
    session[3] = class1_slot_1 + '_' + result[1].TIME
    session[4] = class1_slot_2 + '_' + result[1].TIME
    session[5] = class1_slot_3 + '_' + result[1].TIME
#TODO:   Turn into a loop and check for first null entry.  This is a proof of concept


    ClassOps = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    x = len(result)
    for i in range(0,x):
        ClassOps[i] = result[i].UBCLASS

    return render_template("profile.html",username="sethkara",
                           Class_Option_0=ClassOps[0],Class_Option_1=ClassOps[1],Class_Option_2=ClassOps[2],
                           Class_Option_3=ClassOps[3],Class_Option_4=ClassOps[4],Class_Option_5=ClassOps[5],
                           Class_Option_6=ClassOps[6],Class_Option_7=ClassOps[7],Class_Option_8=ClassOps[8],
                           Class_Option_9=ClassOps[9],Class_Option_10=ClassOps[10],Class_Option_11=ClassOps[11],

                           Class_Option_0_Days=result[0].DAYS,Class_Option_0_Time=result[0].TIME,
                           Class_Option_1_Days=result[1].DAYS,Class_Option_1_Time=result[1].TIME)





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
