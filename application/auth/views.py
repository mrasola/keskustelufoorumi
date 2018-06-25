from flask import render_template, request, redirect, url_for, flash
from application import app, db, login_required
from application.auth.models import User
from application.auth.forms import *
from flask_login import login_user, logout_user


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/login.html", form=LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/login.html", form=form,
                               error="No such username or password. Try again:")

    login_user(user)
    return redirect(url_for("index"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/register/")
def auth_form():
    return render_template("auth/registration.html", form=RegistrationForm())


@app.route("/auth/register", methods=["POST", "GET"])
def auth_register():
    f=RegistrationForm(request.form)

    if not f.validate(): return render_template("auth/registration.html", form=f)

    u = User(name=f.name.data, username=f.username.data, password=f.password.data)

    db.session().add(u)
    db.session().commit()

    return redirect(url_for("auth_login"))


@app.route("/auth/<account_id>/delete", methods=["POST", "GET"])
@login_required(role="ADMIN")
def user_delete(account_id):
    u=User.query.get(account_id)
    db.session.delete(u)
    db.session.commit()
    flash("User deleted!", category="success")

    return redirect(url_for("categories_index"))
