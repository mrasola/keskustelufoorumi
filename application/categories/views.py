from flask_login import login_required, current_user
from application import app, db
from flask import render_template, request, url_for, redirect, flash
from application.categories.models import Category
from application.categories.forms import CategoryForm


@app.route("/categories", methods=["GET"])
def categories_index():
    return render_template("categories/list.html", cs=Category.query.all())


@app.route("/categories/new/")
@login_required
def categories_form():
    return render_template("categories/new.html", form=CategoryForm())


@app.route("/categories/new", methods=["POST", "GET"])
@login_required
def categories_create():
    f=CategoryForm(request.form)

    if not f.validate():
        return render_template("categories/new.html", form=f)

    c=Category(f.name.data, f.description.data)

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("categories_index"))


@app.route("/categories/<category_id>/", methods=["GET"])
def category_look(category_id):
    c=Category.query.get(category_id)

    return render_template("categories/look.html", c=c)


@app.route("/category/edit/<category_id>/", methods=["POST", "GET"])
@login_required
def category_edit(category_id):
    c=Category.query.get(category_id)

    if c:
        form=CategoryForm(formdata=request.form, obj=c);

        if request.method=='POST' and form.validate():
            c.name=form.name.data; c.description=form.description.data
            db.session.commit()

            flash('Album updated successfully!')
            return redirect("categories_index")

        return render_template("categories/new.html", form=form)
    else:
        return 'Error loading #{id}'.format(id=id)


@app.route("/category/delete/<category_id>/", methods=["POST", "GET"])
@login_required
def category_delete(category_id):
    c=Category.query.get(category_id)
    db.session.delete(c)
    db.session.commit()

    return redirect(url_for("categories_index"))