"""main app.py for flask"""

# import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    """renders index.html"""
    return render_template("index.html")
