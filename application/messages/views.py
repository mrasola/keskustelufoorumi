from application import app, db
from flask import render_template, request, url_for, redirect
from application.messages.models import Message

@app.route("/messages", methods=["GET"])
def messages_index():
    return render_template("messages/list.html", ms = Message.query.all())

@app.route("/messages/new/")
def messages_form():
    return render_template("messages/new.html")

@app.route("/messages/", methods=["POST"])
def messages_create():
    m = Message(request.form.get("subject"), request.form.get("body"))

    db.session().add(m)
    db.session().commit()

    return redirect(url_for("messages_index"))

@app.route("/messages/<message_id>/", methods=["POST"])
def message_set_read(message_id):
    m = Message.query.get(message_id)
    m.read= True
    db.session().commit()

    return redirect(url_for("messages_index"))

@app.route("/messages/<message_id>/", methods=["GET"])
def message_look(message_id):
    m = Message.query.get(message_id)

    return render_template("messages/lookMessage.html", m=m)