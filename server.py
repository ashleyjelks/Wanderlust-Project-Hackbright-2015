from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from model import connect_to_db, db, User, Search, Flight, SavedSearch
from airline_airport_conversions import airlines, cities, airports
from latlong import latlongs


app = Flask(__name__)
app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined


@app.route('/', methods=['GET'])
def homepage():

    """Wanderlust Homepage. Users can register for an account, login, or simply search flights."""

    return render_template("index.html")


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


@app.route('/login', methods=['GET'])
def login_page():
    """Show login page."""

    return render_template("login_page.html")


@app.route('/map_cities.json')
def map_cities():

    return jsonify(latlongs)


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

    flash("You are logged in to Wanderlust!")

    return render_template("index.html")


@app.route('/logout')
def logout():
    """Log out."""

    del session["user_id"]
    flash("You have successfully logged out of your Wanderlust account!")
    return redirect("/")


@app.route('/saved_searches', methods=['GET'])
def view_saved_searches():
    """View saved flight searches."""

    user_id = session['user_id']

    saved_searches = SavedSearch.query.filter_by(user_id=user_id).all()
    # print saved_searches, "= saved", "$"*100

    for flight in saved_searches:
        print flight
        flight_list = []
        t1_flights = Flight.query.filter_by(flight_id=flight.t1_flight_id).all()
        t2_flights = Flight.query.filter_by(flight_id=flight.t2_flight_id).all()
        flight_list.append((t1_flights, t2_flights))

    for travelers in saved_searches:
        traveler_info = []
        traveler = Search.query.filter_by(search_id=travelers.search_id).all()
        traveler_info.append(traveler)

    return render_template("saved_searches.html", saved_searches=saved_searches, flight_list=flight_list, traveler_info=traveler_info)


@app.route('/saved_searches', methods=['POST'])
def make_saved_searches():
    """View saved flight searches."""

    t1 = request.form.get('t1_flight_id')
    alt1 = request.form.get('alt1_flight_id')
    t2 = request.form.get('t2_flight_id')
    alt2 = request.form.get('alt2_flight_id')
    user_id = session['user_id']

    if t1:
        search_t1=t1
    else:
        search_t1=alt1

    if t2:
        search_t2=t2
    else:
        search_t2=alt2

    search_id = request.form.get('search_id')
    print search_id, "1"
    print user_id, "2"
    print search_t1, "3"
    print search_t2, "4"

    save_search = SavedSearch(user_id=user_id, search_id=search_id, t1_flight_id=search_t1, t2_flight_id=search_t2)

    db.session.add(save_search)
    db.session.commit()

    flash("Your query has been saved to your user account.")

    return redirect("/saved_searches")


@app.route('/search_results', methods=['GET'])
def index():

    """Route to gather a user's flight search parameters"""

    return render_template("search_results.html")


@app.route('/search_results',  methods=['POST'])
def get_search():
    """Process search request, renders user results of their request. """

    user_id = session.get("user_id")
    traveler1_name = request.form["traveler1_name"]
    traveler2_name = request.form["traveler2_name"]
    traveler1_origin = request.form["traveler1_origin"]
    traveler2_origin = request.form["traveler2_origin"]
    traveler1_max_price = int(request.form["traveler1_max_price"])
    traveler2_max_price = int(request.form["traveler2_max_price"])
    departure_date = request.form["departure_date"]
    return_date = request.form["return_date"]
    destination = request.form["destination"]

    t1 = Flight.query.filter_by(outbound_city_origin=cities[traveler1_origin], inbound_city_origin=cities[destination]).filter(Flight.total_fare<=traveler1_max_price).first()
    alt1 = None

    if not t1:
        alt1 = Flight.query.filter_by(outbound_city_origin=cities[traveler1_origin], inbound_city_origin=cities[destination]).first()

    t2 = Flight.query.filter_by(outbound_city_origin=cities[traveler2_origin], inbound_city_origin=cities[destination]).filter(Flight.total_fare<=traveler2_max_price).first()
    alt2 = None

    if not t2:
        alt2 = Flight.query.filter_by(outbound_city_origin=cities[traveler2_origin], inbound_city_origin=cities[destination]).first()


    if user_id:
        search_request = Search(user_id=user_id, traveler1_name=traveler1_name, traveler2_name=traveler2_name, traveler1_origin=traveler1_origin, traveler2_origin=traveler2_origin, traveler1_max_price=traveler1_max_price, traveler2_max_price=traveler2_max_price, departure_date=departure_date, return_date=return_date, destination=destination)

        db.session.add(search_request)
        db.session.commit()

        search_request_id = Search.query.filter_by(user_id=user_id, traveler1_name=traveler1_name, traveler2_name=traveler2_name, traveler1_origin=traveler1_origin, traveler2_origin=traveler2_origin, traveler1_max_price=traveler1_max_price, traveler2_max_price=traveler2_max_price, departure_date=departure_date, return_date=return_date, destination=destination).first()
        print "&"*100
        print search_request_id
        print search_request_id.user_id
        print "&"*100

        return render_template("search_results.html", search_request=search_request, search_request_id=search_request_id, t1=t1, t2=t2, alt1=alt1, alt2=alt2, destination=destination, traveler1_name=traveler1_name, traveler2_name=traveler2_name)


    return render_template("search_results.html", t1=t1, t2=t2, alt1=alt1, alt2=alt2, destination=destination, traveler1_name=traveler1_name, traveler2_name=traveler2_name)


if __name__ == "__main__":
    app.debug = False
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run()
