from flask import Flask, request, jsonify, render_template
from flask_bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bootstrap(app)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ubflow@localhost/ubflowdb'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    result = Professor.query.filter_by(FIRST_NAME=name).first()
    return render_template('boot1.html', name=result.FIRST_NAME)



@app.route('/professor', methods=['GET'])
def getProfessors():
    if request.method == 'GET':
        results = Professor.query.limit(10).offset(0).all()

    json_results = []
    for result in results:
        d = {'ID': result.ID,
             'FIRST_NAME': result.FIRST_NAME}
        json_results.append(d)

    return jsonify(items=json_results)


@app.route('/professor/<int:professor_id>', methods=['GET'])
def getProfessor(professor_id):
    if request.method == 'GET':
        result = Professor.query.filter_by(ID=professor_id).first()
        if result is None:
            return "false"

        d = {'ID': result.ID,
             'FIRST_NAME': result.FIRST_NAME}
    return render_template('hello.html', name=result.FIRST_NAME)


@app.route('/classes', methods=['GET'])
def getClasses():
    if request.method == 'GET':
        results = UBClasses.query.limit(10).offset(0).all()

    json_results = []
    for result in results:
        d = {'ID': result.ID,
             'CLASS': result.UBCLASS,
             'LOCATION': result.LOCATION,
             'PROFESSOR': result.PROFESSOR}
        json_results.append(d)

    return jsonify(items=json_results)


'''
This sets up the table for professors
'''
class Professor(db.Model):
  __tablename__ = "professor"

  ID = db.Column(db.Integer, primary_key=True)
  FIRST_NAME = db.Column(db.String(50), nullable=False)

  def __init__(self, username,):
    self.FIRST_NAME = username

  def __repr__(self):
    return '<title {}'.format(self.FIRST_NAME)


'''
This sets up the table for classes
'''
class UBClasses(db.Model):
  __tablename__ = "ubclasses"

  ID = db.Column(db.Integer, primary_key=True)
  UBCLASS = db.Column(db.String(50), nullable=False)
  LOCATION = db.Column(db.String(50), nullable=False)
  PROFESSOR = db.Column(db.String(50), nullable=False)

  def __init__(self, ubclass, location, professor):
    self.UBCLASS = ubclass
    self.LOCATION = location
    self.PROFESSOR = professor

  def __repr__(self):
    return '<class {}'.format(self.UBCLASS)


if __name__ == '__main__':
    app.run()
