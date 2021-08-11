from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# personal use database for techniques
class Technique(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    technique_name = db.Column(db.String(50), index = True, unique = False)
    user_name = db.Column(db.String(50), index = True, unique = False)


class LogInForm(FlaskForm):
    userName = StringField("User Name")
    password = PasswordField("Password")
    submit = SubmitField('Submit User')

class NewJujiUser(FlaskForm):
    userName = StringField("User Name")
    password = PasswordField("Password")
    check_password = PasswordField("Retype Password")
    submit = SubmitField('Submit Account Information')

# login page - use microservice
@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', template_form=LogInForm())

# if there is no user in DB - use microservice
@app.route('/newUser', methods=["GET","POST"])
def createJuji():
    return render_template('newUser.html', template_form = NewJujiUser())

# this will be first page a user goes to after logging in
@app.route('/technique/<int:user_id>', methods=["GET", "POST"])
def technique(user_id):
    return f'User {user_id} techniques'