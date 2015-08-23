from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from model import connect_to_db, db, User, Flight, SavedSearch
# import api_seed as api_seed



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
    traveler1_origin = request.form["traveler1_origin"]
    traveler2_origin = request.form["traveler2_origin"]
    traveler1_max_price = int(request.form["traveler1_max_price"])
    traveler2_max_price = int(request.form["traveler2_max_price"])
    departure_date = request.form["departure_date"]
    return_date = request.form["return_date"]
    destination = request.form["destination"]
    print name
    print email
    print password
    print traveler1_name
    print traveler2_name
    print traveler1_origin
    print traveler2_origin
    print traveler1_max_price
    print traveler2_max_price
    print departure_date
    print return_date
    print destination

    search_results = User(name=name, email=email, password=password, traveler1_name=traveler1_name, traveler2_name=traveler2_name, traveler1_origin=traveler1_origin, traveler2_origin=traveler2_origin, traveler1_max_price=traveler1_max_price, traveler2_max_price=traveler2_max_price, departure_date=departure_date, return_date=return_date, destination=destination)
    print search_results


    db.session.add(search_results)
    db.session.commit()


    # print traveler1_origin
    # print destination



    t1_flight_info = Flight.query.filter_by(outbound_city_origin=traveler1_origin, inbound_city_origin=destination).first()
    
    t2_flight_info = Flight.query.filter_by(outbound_city_origin=traveler2_origin, inbound_city_origin=destination).first()
    # print t2_flight_info.inbound_datetime_departure

    print t1_flight_info.base_fare, t1_flight_info.outbound_city_origin, t1_flight_info.outbound_city_final_destination, t1_flight_info.outbound_airline, t1_flight_info.outbound_datetime_departure,  "this is t1" 

    print  t2_flight_info.base_fare, t2_flight_info.outbound_city_origin, t2_flight_info.outbound_city_final_destination, t2_flight_info.outbound_airline, t2_flight_info.outbound_datetime_departure, "this is t2" 

    return render_template("search_results.html", search_results=search_results, t1_flight_info=t1_flight_info, t2_flight_info=t2_flight_info) 





if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run()

