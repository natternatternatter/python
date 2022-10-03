from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User


# routes will go here

@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("read_all.html", users=users)


@app.route("/new_user_form")
def new_user_form():
    return render_template("create.html")


@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    # We pass the data dictionary into the new_user method from the User class.
    User.new_user(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')
