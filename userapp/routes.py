from flask import request, render_template, redirect, jsonify

from userapp import app, db
from userapp.models import User


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        user = User(
            request.form["username"],
            request.form["name"],
            request.form["password"],
        )

        db.session.add(user)
        db.session.commit()

        return redirect("/")

    return render_template("index.html", users=User.query.all())


@app.route("/edit/<int:user_id>", methods=["GET", "POST"])
def edit_user_id(user_id):
    user = User.query.get(user_id)

    if request.method == "POST":
        user.username = request.form["username"]
        user.name = request.form["name"]
        user.password = request.form["password"]

        db.session.commit()

        return redirect("/")

    return jsonify(
        type=1,
        id=user.id,
        name=user.name,
        username=user.username,
        password=user.password,
    )


@app.route("/delete/<int:user_id>", methods=["GET", "POST"])
def delete_user_id(user_id):
    user = User.query.get(user_id)

    if request.method == "POST":
        db.session.delete(user)
        db.session.commit()

        return redirect("/")

    return jsonify(
        type=2,
        id=user.id,
        name=user.name,
        username=user.username,
        password=user.password,
    )
