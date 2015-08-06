"""Wanderlust App Server"""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session

from flask_debugtoolbar import DebugToolbarExtension

from model import User, Flight, FlightUserMap, SavedSearch, connect_to_db, db


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

""" FIGURE OUT HOW TO HIDE THE APP secret_key ON GITHUB  """

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined



@app.route('/')
def index():
    """Homepage."""

    return render_template("index.html")


"""
YOU NEED TO CREATE AN INSTANCE OF THE FLIGHT CLASS TO INCLUDE FLIGHT DATA FOR THE 2ND TRAVELER,
USE THIS CODE SNIPPET FROM SEED.PY FROM RATINGS
new_user = User(user_id=new_user_id, age=user_age, zipcode=user_zipcode)
#new_user is the object. new_user is also an instance of the User class.
"""

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()
