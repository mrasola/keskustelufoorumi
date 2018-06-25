from flask_login import current_user
from flask import render_template, request, url_for, redirect, flash
from application import app, db, login_required
from application.categories.models import Category
from application.categories.forms import CategoryForm


@app.route("/categories", methods=["GET"])
def categories_index():
    return render_template("categories/list.html", cs=Category.query.all())


@app.route("/categories/new/")
@login_required(role="USER")
def categories_form():
    return render_template("categories/new.html", form=CategoryForm())


@app.route("/categories/new", methods=["POST", "GET"])
@login_required(role="USER")
def categories_create():
    f=CategoryForm(request.form)

    if not f.validate():
        return render_template("categories/new.html", form=f)

    c=Category(f.name.data, f.description.data)

    db.session().add(c)
    db.session().commit()
    flash("Category added successfully!", category="success")

    return redirect(url_for("categories_index"))


@app.route("/categories/<category_id>/", methods=["GET"])
def category_look(category_id):
    c=Category.query.get(category_id)

    return render_template("categories/look.html", c=c)


@app.route("/categories/<category_id>/edit/")
@login_required(role="USER")
def category_edit_form(category_id):
    f=CategoryForm(); c=Category.query.get(category_id);
    f.name.default=c.name; f.description.default=c.description; f.process()
    return render_template("categories/edit.html", form=f, c=c)


@app.route("/category/<category_id>/edit", methods=["POST", "GET"])
@login_required(role="USER")
def category_edit(category_id):
    f=CategoryForm(request.form)

    if not f.validate():
        return render_template("categories/edit.html", form=f)

    c=Category.query.get(category_id)
    c.description=f.description.data; c.name=f.name.data

    db.session().commit()

    return redirect(url_for("categories_index"))


@app.route("/category/delete/<category_id>/", methods=["POST", "GET"])
@login_required(role="USER")
def category_delete(category_id):
    c=Category.query.get(category_id)
    db.session.delete(c)
    db.session.commit()

    return redirect(url_for("categories_index"))