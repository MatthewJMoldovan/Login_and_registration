from flask import render_template,redirect,request,session, flash
from flask_app import app
from flask_app.models.user import User


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/create_user', methods = ['POST'])
def create_user():

    if not User.validate(request.form):
        return redirect('/')

    User.create_user(request.form)
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    if not 'uid' in session:
        flash("Access Denied! Login First!")
        return redirect('/')

    return render_template("dashboard.html")

@app.route('/secure_login', methods = ['POST'])
def secure_login():
    logged_in_user = User.validate_login(request.form)
    if not logged_in_user:
        return redirect('/')
        
    session['uid'] = logged_in_user.id
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')