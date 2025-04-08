"""main app.py for flask"""

# import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    """renders index.html"""
    return render_template("index.html")


# TODO: handle submit review from frontend to send to DB/ML # pylint: disable=fixme

# wait (?) on ML to return reponse on submitted review and then: # pylint: disable=fixme
# TODO: write functions to get data from the DB
# and then parse data to send to frontend

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
