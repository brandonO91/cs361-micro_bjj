from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

class LogInForm(FlaskForm):
    userName = StringField("User Name")
    password = PasswordField("Password")
    submit = SubmitField('Submit User')

# login page - use microservice
@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', template_form=LogInForm())

# if there is no user in DB
@app.route('/newUser', methods=["GET","POST"])
def createJuji():
    return 'Creating new jiujitiero'

# this will be first page a user goes to after logging in
@app.route('/technique/<int:user_id>', methods=["GET", "POST"])
def technique(user_id):
    return f'User {user_id} techniques'