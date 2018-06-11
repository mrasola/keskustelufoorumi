from flask import render_template
from application import app
from application.auth.models import User

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/statistics")
def stats():
    return render_template("stats.html", ms=User.users_messages_number())