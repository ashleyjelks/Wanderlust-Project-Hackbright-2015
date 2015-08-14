# app.py

"""Wanderlust App Server"""

from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
# from model import connect_to_db, db, User, FlightLeg, Flight, SavedSearch, FlightUserMap

# User, Flight, FlightUserMap, SavedSearch,


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined



@app.route('/')
def index():
    """Homepage."""

    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run()
