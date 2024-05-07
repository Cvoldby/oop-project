from flask import (
    Flask, redirect, render_template, url_for, request
)

from markupsafe import escape


app = Flask(__name__)


@app.route("/")
def hell_world():
    return "<p>This is a welcome page!</p>"


