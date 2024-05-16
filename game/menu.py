from flask import (
    Flask, redirect, render_template, url_for, request
)

from markupsafe import escape


app = Flask(__name__)


@app.route("/home")
def menu():
    return render_template("home.html")


