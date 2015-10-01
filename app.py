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
        self.RECITATION_ID = id
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
    populate_session(result)
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
                           Class_Option_1_Days=result[1].DAYS,Class_Option_1_Time=result[1].TIME,
                           Class_Option_2_Days=result[2].DAYS,Class_Option_2_Time=result[2].TIME,
                           Class_Option_3_Days=result[3].DAYS,Class_Option_3_Time=result[3].TIME)

@app.route('/getnextclassgroup', methods=['GET'])
def getClassGroup():
    if request.method == 'GET':
        results = UBClasses.query.filter_by(DEPARTMENT="EAS").all()
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
        session[0] = result.UBCLASS
        #populate_session(result)
    return jsonify(classes=json_results)

    #results = []
    #if request.method == 'GET':
    #    results = UBClasses.query.filter_by(DEPARTMENT='CSE').all()

        #populate_session(results)
    #return jsonify(classes=results)


def populate_session(array):
    x=0
    for result in array:
        slots = gen_time_slots(result.DAYS, result.TIME)
        session[x]=result.UBCLASS
        session[x+1]=result.DAYS
        session[x+2]=result.TIME
        session[x+3]=result.TYPE
        session[x+4]=result.DEPARTMENT
        session[x+5]=result.SECTION
        session[x+6]=result.LOCATION
        session[x+7]=result.BUILDING
        session[x+8]=result.ROOM_NUMBER
        session[x+9]=result.PROFESSOR
        session[x+10]=result.STATUS
        session[x+11]=result.RESERVED
        session[x+12]=' '
        session[x+13]=' '
        session[x+14]=slots[0]
        session[x+15]=slots[1]
        session[x+16]=slots[2]
        session[x+17]=slots[3]
        session[x+18]=slots[4]
        session[x+19]=slots[5]
        x+=20
    return None


def gen_time_slots(days, times):
    slots = [' ', ' ', ' ', ' ', ' ', ' ']
    if days == 'M W F':
        slots[0] = 'Mon'
        slots[1] = 'Wed'
        slots[2] = 'Fri'
    elif days == 'T R':
        slots[0] = 'Tue'
        slots[1] = 'Thu'
    elif days == "M":
        slots[0] = "Mon"
    elif days == "T":
        slots[0] = "Tue"
    elif days == "R":
        slots[0] = "Thu"
    slots[0] = slots[0] + '_' + times
    slots[1] = slots[1] + '_' + times
    slots[2] = slots[2] + '_' + times
    slots[3] = slots[3] + '_' + times
    slots[4] = slots[4] + '_' + times
    slots[5] = slots[5] + '_' + times
    return slots


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
