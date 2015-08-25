from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from model import connect_to_db, db, User, Flight, SavedSearch
from airline_airport_conversions import airlines, cities
# import api_seed as api_seed



app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/',)
def homepage():

    """Wanderlust Homepage. Users can register for an account, login, or simply search flights."""

    return render_template("homepage.html")


@app.route('/index', methods=['GET'])
def index():

    """Route to gather a user's flight search parameters"""

    return render_template("index.html")


@app.route('/register', methods=['GET'])
def register_page():
    """Show form for users to register to use Wanderlust"""

    return render_template("register_page.html")


@app.route('/register', methods=['POST'])
def register_process():
    """Process registration form inputs."""

    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]

    new_user = User(name=name, email=email, password=password)

    db.session.add(new_user)
    db.session.commit()

    flash("%s is now registered with Wanderlust!. Thank you." % name)

    return render_template("index.html")



@app.route('/search_results',  methods=['POST'])
def get_search():
    """Process search request, renders user results of their request. """

    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    traveler1_name = request.form["traveler1_name"]
    traveler2_name = request.form["traveler2_name"]
    traveler1_origin = request.form["traveler1_origin"]
    traveler2_origin = request.form["traveler2_origin"]
    traveler1_max_price = int(request.form["traveler1_max_price"])
    traveler2_max_price = int(request.form["traveler2_max_price"])
    departure_date = request.form["departure_date"]
    return_date = request.form["return_date"]
    destination = request.form["destination"]

    search_results = Search(traveler1_name=traveler1_name, traveler2_name=traveler2_name, traveler1_origin=traveler1_origin, traveler2_origin=traveler2_origin, traveler1_max_price=traveler1_max_price, traveler2_max_price=traveler2_max_price, departure_date=departure_date, return_date=return_date, destination=destination)

    db.session.add(search_results)
    db.session.commit()

    t1_flight_info = Flight.query.filter_by(outbound_city_origin=traveler1_origin, inbound_city_origin=destination).first()
    
    t2_flight_info = Flight.query.filter_by(outbound_city_origin=traveler2_origin, inbound_city_origin=destination).first()

    return render_template("search_results.html", search_results=search_results, t1_flight_info=t1_flight_info, t2_flight_info=t2_flight_info) 




if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run()

