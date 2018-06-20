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


# @app.route("/category/edit/<category_id>/", methods=["POST", "GET"])
# @login_required
# def cetegory_edit(category_id):
#     c = Message.query.get(category_id)
#     f = MessageForm()
#
#     if request.method=="GET":
#         f.subject.data=c.subject
#         f.body.data=c.body
#         f.categories.data=[c.category_id for c in c.categories]
#
#     if f.validate_on_submit():
#         if f.subject.data is None:
#             message=MessageForm()
#             message.subject.data=f.subject.data; message.body.data=f.body.data
#             message.categories.data=f.categories.data
#             db.session.add(message)
#             db.session.commit()
#             return url_for("categories/edit.html")
#
#     return render_template("categories/edit.html", form=f)


@app.route("/category/delete/<category_id>/", methods=["POST", "GET"])
@login_required
def category_delete(category_id):
    c=Category.query.get(category_id)
    db.session.delete(c)
    db.session.commit()

    return redirect(url_for("categories_index"))