from flask_socketio import SocketIO
from flask_socketio import send
from os import *
from time import localtime, strftime
from datetime import datetime
from flask import render_template, jsonify, request, Flask, redirect, url_for
from flask_socketio import send, emit, join_room, leave_room
from flask_wtf import FlaskForm
from pylint_flask import *
from pylint import *
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from flask_sqlalchemy import *
from pymysql import *
from flask_login import LoginManager, UserMixin, login_user, current_user, login_required, logout_user
app = Flask(__name__)
socketio = SocketIO(app)



db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:bikaloic@localhost/talky'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False



class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(256), unique = True, nullable = False)
    password = db.Column(db.String(256), nullable = False)
     

def invalid_credentials(form, field):
    username_entered = form.username.data
    password_entered = field.data

    user_object = User.query.filter_by(username = username_entered).first()
    if user_object is None :
         raise ValidationError("Username or password is wrong")
    elif password_entered != user_object.password :
        raise ValidationError("Username or password is wrong")


class RegistrationForm(FlaskForm):
    username = StringField('username_label', validators = [InputRequired(message="Username required"), Length(min = 4, max = 25, message = "Username must be between 4 and 25 characters")])
    password = PasswordField('password_label', validators = [InputRequired(message="Password required"), Length(min = 4, max = 25, message = "Password must be between 4 and 25 characters")])
    confirm_pswd = PasswordField('confirm_pswd_label', validators = [InputRequired(message="Password required"), EqualTo('password', message = "Password must match")])
    submit_button = SubmitField('Create')


class Login_form(FlaskForm):
    username = StringField('username_label', validators = [InputRequired(message = "Username required")])
    password = PasswordField('password_label', validators = [InputRequired(message = "Password is needed"), invalid_credentials])
    submit = SubmitField('Login')




app.secret_key = 'minilolo'

db = SQLAlchemy(app)


ROOMS = ["Room1", "Room2", "Room3", "Room4"]

login = LoginManager(app)
login.init_app(app)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
@app.route('/home')

def home():
    """Renders the home page."""
    return render_template(
        'Page.html',
        title='Home Page',
        year=datetime.now().year,
    )


@socketio.on('message')
def messenger(mess):
    print(f"\n\n{mess}\n\n")
    send({'msg' : mess['msg'], 'username' : mess['username'], 'time_stamp' : strftime('%I:%M%p', localtime())}, room = mess['room'])
    


@socketio.on('join')
def join(mess):
    join_room(mess['room'])
    send({'msg' : mess['username'] + " has joined the " + mess['room'] + " ."}, room = mess['room'])



@socketio.on('leave')
def leave(pipi):
    leave_room(pipi['room'])
    send({'msg' : pipi['username'] + " has left the " + pipi['room'] + " ."}, room=pipi['room'])

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route( '/sign_in' ,methods =['GET', 'POST'])
def sign_in():
    """ty le resaka database : elle passe sur le database selectionner"""
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
       username = reg_form.username.data
       password = reg_form.password.data

       user_object = User.query.filter_by(username = username).first()
       if user_object : 
           return "Aready taken"

       user = User(username = username, password = password)
       db.session.add(user)
       db.session.commit()
       return redirect(url_for('log_in'))
        
    return render_template(
        'login.html', form = reg_form
        )


@app.route('/log_in', methods = ['GET', 'POST'])
def log_in():
    Loginform = Login_form()
    if Loginform.validate_on_submit():
        user_object = User.query.filter_by(username = Loginform.username.data).first()
        login_user(user_object)
        if current_user.is_authenticated:
            return redirect(url_for('chatbox'))
            
        return "Not logged in"

    return render_template('log_in.html', form = Loginform)



@app.route('/chatbox', methods = ['GET','¨POST'])
def chatbox():
    """main page of minilolo"""

    if not current_user.is_authenticated:
        return "Log in please before anything"
    return render_template(
        'chat.html', title = "koko", message = "taybe", username = current_user.username, rooms = ROOMS
        )


@app.route('/log_out', methods = ['GET'])
def logout():
    logout_user()
    return 'koko'


@app.route('/test')
def test():
    return "bite de merde"

if __name__ == '__main__':
    socketio.run(app, host = '127.0.0.1', port = 5000, debug = True)
