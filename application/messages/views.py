from flask_login import login_required, current_user
from application import app, db
from flask import render_template, request, url_for, redirect, flash
from application.messages.models import Message, Category
from application.messages.forms import MessageForm


@app.route("/messages", methods=["GET"])
def messages_index():
    return render_template("messages/list.html", ms=Message.query.all())


@app.route("/messages/new/")
@login_required
def messages_form():
    return render_template("messages/new.html", form=MessageForm())


@app.route("/messages/", methods=["POST"])
@login_required
def messages_create():
    f=MessageForm(request.form)

    if not f.validate():
        return render_template("messages/new.html", form=f)

    m=Message(f.subject.data, f.body.data)
    m.account_id=current_user.id

    for c in f.categories.data:
        cat=Category.query.filter_by(category=c[1]).first()
        m.categories.append(cat)

    db.session().add(m)
    db.session().commit()

    return redirect(url_for("messages_index"))


@app.route("/messages/<message_id>/", methods=["POST"])
@login_required
def message_set_read(message_id):
    m = Message.query.get(message_id)
    m.read = True

    db.session().commit()

    return redirect(url_for("messages_index"))


@app.route("/messages/<message_id>/", methods=["GET"])
def message_look(message_id):
    m=Message.query.get(message_id)

    return render_template("messages/lookMessage.html", m=m)


@app.route("/messages/<message_id>/edit/", methods=["POST", "GET"])
@login_required
def message_edit(message_id):
    m = Message.query.get(message_id)
    f = MessageForm(request.form, obj=m)

    if request.method=="POST" and f.validate_on_submit():
        f.populate_obj(m); m.read=False
        db.session.commit()

        return redirect(url_for("message_look", message_id=m.id))

    return render_template("messages/edit.html", form=f)


@app.route("/messages/delete/<message_id>/", methods=["POST", "GET"])
@login_required
def message_delete(message_id):
    m=Message.query.get(message_id)
    db.session.delete(m)
    db.session.commit()

    return redirect(url_for("messages_index"))

