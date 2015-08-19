from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from model import connect_to_db, db, User, Flight
import api_seed as api_seed

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/', methods=['GET'])
def index():

    """Route to gather a user's search parameters"""

    return render_template("index.html")


@app.route('/search_results',  methods=['POST'])
def get_search():
    """Wanderlust Homepage. Here user inserts search parameters"""

    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    traveler1_name = request.form["traveler1_name"]
    traveler2_name = request.form["traveler2_name"]
    first_origin = request.form["first_origin"]
    second_origin = request.form["second_origin"]
    first_max_price = int(request.form["first_max_price"])
    second_max_price = int(request.form["second_max_price"])
    departure_date = request.form["departure_date"]
    return_date = request.form["return_date"]
    destination = request.form["destination"]
    print name
    print email
    print password
    print traveler1_name
    print traveler2_name
    print first_origin
    print second_origin
    print first_max_price
    print second_max_price
    print departure_date
    print return_date
    print destination

    search_request = User(name=name, email=email, password=password, traveler1_name=traveler1_name, traveler2_name=traveler2_name, first_origin=first_origin, second_origin=second_origin, first_max_price=first_max_price, second_max_price=second_max_price, departure_date=departure_date, return_date=return_date, destination=destination)
    print search_request

    db.session.add(search_request)
    db.session.commit()

    t1 = api_seed.get_price_traveler_one(first_origin, destination, departure_date, return_date, first_max_price)
    t2 = api_seed.get_price_traveler_two(second_origin, destination, departure_date, return_date, second_max_price)

    test = Flight.query.filter_by(flight_id=47).one()

    print "*"*20, test

    return render_template("search_results.html", t1=t1, t2=t2)


if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run()


