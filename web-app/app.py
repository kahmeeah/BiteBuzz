"""main app.py for flask"""

# import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    """renders index.html"""
    return render_template("index.html")


# TODO: handle submit review from frontend to send to DB # pylint: disable=fixme

# wait (?) on ML to return reponse on submitted review and then: # pylint: disable=fixme
# TODO: write functions to get data from the DB
# and then parse data to send to frontend
