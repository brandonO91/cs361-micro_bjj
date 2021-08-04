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

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', template_form=LogInForm())

@app.route('/<int:user_id/technique', methods=["GET", "POST"])
def technique():
    return f'User {user_id} techniques'