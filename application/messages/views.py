from flask_login import current_user
from application import app, db, login_required, login_manager
from flask import render_template, request, url_for, redirect, flash
from application.messages.models import Message
from application.categories.models import Category
from application.messages.forms import MessageForm


@app.route("/messages", methods=["GET"])
def messages_index():
    return render_template("messages/list.html", ms=Message.query.all())


@app.route("/messages/new/")
@login_required(role="USER")
def messages_form():
    return render_template("messages/new.html", form=MessageForm())


@app.route("/messages/new", methods=["POST"])
@login_required(role="USER")
def messages_create():
    f=MessageForm()

    if not f.validate():
        return render_template("messages/new.html", form=f)

    m=Message(f.subject.data, f.body.data)
    m.account_id=current_user.id

    for c in f.categories.data:
        cat=Category.query.get(c)
        m.categories.append(cat)

    db.session.add(m)
    db.session.commit()

    return redirect(url_for("messages_index"))


@app.route("/messages/<message_id>/", methods=["POST"])
@login_required(role="USER")
def message_set_read(message_id):
    m = Message.query.get(message_id)
    m.read = True

    db.session().commit()

    return redirect(url_for("messages_index"))


@app.route("/messages/<message_id>/", methods=["GET"])
def message_look(message_id):
    m=Message.query.get(message_id)

    return render_template("messages/look.html", m=m)


@app.route("/messagess/<message_id>/edit/")
@login_required(role="USER")
def message_edit_form(message_id):
    f=MessageForm(); m=Message.query.get(message_id)

    if current_user.id!=m.account_id and not current_user.roles().__contains__("ADMIN"):
        return login_manager.unauthorized()

    f.subject.default=m.subject; f.body.default=m.body; f.process()

    return render_template("messages/edit.html", form=f, m=m)


@app.route("/message/<message_id>/edit", methods=["POST", "GET"])
@login_required(role="USER")
def message_edit(message_id):
    f=MessageForm()

    if not f.validate():
        return render_template("messages/edit.html", form=f)

    m=Message.query.get(message_id)
    m.body=f.body.data; m.subject=f.subject.data; m.read=False

    for c in m.categories:
        if not f.categories.data.__contains__(c.id):
            m.categories.remove(c)

    for c in f.categories.data:
        cat=Category.query.get(c)
        m.categories.append(cat)

    db.session.commit()

    return redirect(url_for("messages_index"))


@app.route("/messages/delete/<message_id>/", methods=["POST", "GET"])
@login_required(role="USER")
def message_delete(message_id):
    m=Message.query.get(message_id)
    db.session.delete(m)
    db.session.commit()

    return redirect(url_for("messages_index"))
