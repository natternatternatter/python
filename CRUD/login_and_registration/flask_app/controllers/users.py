from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route("/")
def display_login_and_registration():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():

    if User.validate_registration(request.form) == False:
        return redirect("/")

    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    data = {
        'first_name': request.form["first_name"],
        'last_name': request.form["last_name"],
        'email': request.form["email"],
        'password': pw_hash
    }

    User.register(data)
    flash("User registered, log in now.")

    return redirect("/")


@app.route("/login", methods=["POST"])
def login():
    current_user = User.validate_email(request.form)
    if current_user == None:
        flash("This email address is not registered")
        return redirect("/")
    print(current_user.password)
    if not bcrypt.check_password_hash(current_user.password, request.form['password']):
        flash("Email and Password do not match")
        return redirect("/")

    session['first_name'] = current_user.first_name
    session['email'] = current_user.email
    session['user_id'] = current_user.id

    return redirect("/success")


@app.route("/success")
def display_home_page():
    return render_template("registration_success.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
