from app import app, db, login_manager
from app.models import Users
from flask import render_template, request, redirect, url_for
import bcrypt

@login_manager.user_loader
def user_loader(user_id):
    return Users.query.get(user_id)



@app.route('/')
@app.route('/index')
# @login_required
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    is_call = False
    is_sms = False
    is_email = False
    if "call" in request.form:
        is_call = True
    if "sms" in request.form:
        is_sms = True
    if "email" in request.form:
        is_email = True
    name = request.form["name"]
    reminder_text = request.form["reminder"]
    date = request.form["date"]
    time = request.form["time"]



@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        POST_EMAIL = request.form["email"]
        POST_PASSWORD = request.form["password"]


    return render_template('login.html')

@app.route('/signup', methods=["POST", "GET"])
def sign_up():
    errors = ""
    success = ""
    if request.method == "POST":
        POST_EMAIL = request.form["email"]
        POST_PASSWORD = request.form["password"]
        salt = bcrypt.gensalt()
        hashed_pwd = bcrypt.hashpw(POST_PASSWORD.encode(), salt)
        exists = db.session.query(Users.idusers).filter_by(email=POST_EMAIL).scalar() is not None
        if exists:
            errors = "That email is already taken. Please try again."
            return render_template('signup.html', errors=errors, success=success)
        else:
            success = "Congrats! You're all signed up. <a href='/login'>Log in here</a>'"
        return render_template('signup.html', errors=errors, success=success)
    else:
        return render_template('signup.html', errors=errors, success=success)

@app.route('/forgot', methods=["POST"])
def forgot():
    try:
        if request.method == "POST":
            email = request.form["email"]
    except Exception as e:
        pass
