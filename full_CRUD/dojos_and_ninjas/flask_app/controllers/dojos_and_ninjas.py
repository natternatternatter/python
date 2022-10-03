from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route("/dojos")
def show_all_dojos():

    dojos = Dojo.get_all_dojos()
    print(dojos)
    return render_template("dojos.html", dojos=dojos)


@app.route("/new_dojo", methods=["POST"])
def new_dojo():

    data = {"name": request.form["name"]}

    Dojo.add_a_dojo(data)
    return redirect("/dojos")


@app.route("/dojos/<int:dojo_id>")
def show_ninjas(dojo_id):

    data = {
        'id': dojo_id
    }

    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template("dojo_show.html", dojo=dojo)


@app.route("/ninjas")
def ninja_form():
    dojos = Dojo.get_all_dojos()
    return render_template("ninjas.html", dojos=dojos)


@app.route("/new_ninja", methods=["POST"])
def new_ninja():

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    print(data)
    Ninja.add_a_ninja(Ninja, data)
    return redirect(f"/dojos/{request.form['dojo_id']}")
