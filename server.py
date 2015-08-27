from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from model import connect_to_db, db, User, Search, Flight, SavedSearch
from airline_airport_conversions import airlines, cities, airports


# import api_seed as api_seed



app = Flask(__name__)
app.secret_key = "ABC"
# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined



@app.route('/',)
def homepage():

    """Wanderlust Homepage. Users can register for an account, login, or simply search flights."""

    
    return render_template("homepage.html")



@app.route('/register', methods=['GET'])
def register_page():
    """Show form for users to register to use Wanderlust"""

    return render_template("register_page.html")


@app.route('/register', methods=['POST'])
def register_process():
    """Process registration form inputs."""

    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    email = request.form["email"]
    password = request.form["password"]

    new_user = User(firstname=firstname, lastname=lastname, email=email, password=password)

    db.session.add(new_user)
    db.session.commit()

    flash("%s %s is now registered with Wanderlust!. Thank you." % (firstname, lastname))

    return render_template("index.html")


# JSON OBJECT
# Key lat/long: value


@app.route('/login', methods=['GET'])
def login_page():
    """Show login page."""

    return render_template("login_page.html")


# @app.route('/map_cities.json')
# def map_cities():
#     # import latlongs
#     return jsonify(latlongs)


@app.route('/login', methods=['POST'])
def login_process():
    """Process login."""

    # Get form variables
    email = request.form["email"]
    password = request.form["password"]

    user = User.query.filter_by(email=email).first()

    if not user:
        flash("Sorry, you are not a registered Wanderlust user. Please create an account!")
        return redirect("/login")

    if user.password != password:
        flash("Incorrect password, please try again.")
        return redirect("/login")

    session["user_id"] = user.user_id
    print session

    flash("You are logged in to Wanderlust!")
    
    return render_template("index.html")   



@app.route('/search_results', methods=['GET'])
def index():

    """Route to gather a user's flight search parameters"""

    return render_template("search_results.html")


@app.route('/search_results',  methods=['POST'])
def get_search():
    """Process search request, renders user results of their request. """

    traveler1_name = request.form["traveler1_name"]
    traveler2_name = request.form["traveler2_name"]
    traveler1_origin = request.form["traveler1_origin"]
    traveler2_origin = request.form["traveler2_origin"]
    traveler1_max_price = int(request.form["traveler1_max_price"])
    traveler2_max_price = int(request.form["traveler2_max_price"])
    departure_date = request.form["departure_date"]
    return_date = request.form["return_date"]
    destination = request.form["destination"]

    print traveler1_name, traveler2_name, traveler1_origin, traveler2_origin, traveler1_max_price, traveler2_max_price, departure_date, return_date, destination

    search_request = Search(traveler1_name=traveler1_name, traveler2_name=traveler2_name, traveler1_origin=traveler1_origin, traveler2_origin=traveler2_origin, traveler1_max_price=traveler1_max_price, traveler2_max_price=traveler2_max_price, departure_date=departure_date, return_date=return_date, destination=destination)

    db.session.add(search_request)
    db.session.commit()

    print search_request
    print type(search_request)

    t1 = Flight.query.filter_by(outbound_city_origin=cities[traveler1_origin], inbound_city_origin=cities[destination]).filter(Flight.base_fare<=traveler1_max_price).first()
    alt1 = None

    if not t1:
        alt1 = Flight.query.filter_by(outbound_city_origin=cities[traveler1_origin], inbound_city_origin=cities[destination]).first()
        
    t2 = Flight.query.filter_by(outbound_city_origin=cities[traveler2_origin], inbound_city_origin=cities[destination]).filter(Flight.base_fare<=traveler2_max_price).first()
    alt2 = None

    if not t2:
        alt2 = Flight.query.filter_by(outbound_city_origin=cities[traveler2_origin], inbound_city_origin=cities[destination]).first()
       
    print "This is ", t1, t2




    return render_template("search_results.html", search_request=search_request, t1=t1, t2=t2, alt1=alt1, alt2=alt2) 




if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run()
    

