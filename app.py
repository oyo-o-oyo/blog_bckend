from flask import Flask
from flask import Flask,request
from flask import make_response
from flask_cors import CORS
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app,supports_credentials=True)

@app.after_request
def af_request(resp):
	resp = make_response(resp)
	resp.headers['Access-Control-Allow-Origin'] = '*'
	resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
	resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
	return resp

@app.route('/')
def index():
	return "200 OK"

@app.route('/login',methods=['POST'])
def login():
	json = request.get_json()
	print(json)
	return "200 OK POST"







class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64),unique=True)

	def __repr__(self):
		return '<Role %r>' % self.name

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64),unique=True,index=True)

	def __repr__(self):
		return '<User %r>' % self.username






if __name__ == '__main__':
	app.run()