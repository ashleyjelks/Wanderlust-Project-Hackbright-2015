""" Models and database functions for Wanderlust project. """

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


#################################################################

# Defining all Models in this database

class User(db.Model):
    #User is a sublclass of db.Model

    """ User of Wanderlust Application and their search parameters."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name = db.Column(db.String(150), nullable=True)
    email = db.Column(db.String(150), nullable=True)
    password = db.Column(db.String(100), nullable=True)
    traveler1_name = db.Column(db.String(150), nullable=True)
    traveler2_name = db.Column(db.String(150), nullable=True)
    traveler1_origin = db.Column(db.String(75), nullable=True)
    traveler2_origin = db.Column(db.String(75), nullable=True)
    traveler1_max_price = db.Column(db.Integer, nullable=True)
    traveler2_max_price = db.Column(db.Integer, nullable=True)
    departure_date = db.Column(db.String(75), nullable=True)
    return_date = db.Column(db.String(75), nullable=True)
    destination = db.Column(db.String(75), nullable=True)



class Flight(db.Model):

    """ Flight database info for travelers."""

    __tablename__ = "flights"

    flight_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
    outbound_city_origin = db.Column(db.String(75), nullable=False)
    outbound_city_final_destination = db.Column(db.String(75), nullable=False)
    outbound_airline = db.Column(db.String(75), nullable=False)
    outbound_flight_number = db.Column(db.Integer, nullable=False)
    outbound_datetime_departure = db.Column(db.String(75), nullable=False)
    outbound_datetime_arrival = db.Column(db.String(75), nullable=False)
    inbound_city_origin = db.Column(db.String(75), nullable=False)
    inbound_city_final_destination = db.Column(db.String(75), nullable=False)
    inbound_airline = db.Column(db.String(75), nullable=False)
    inbound_flight_number = db.Column(db.Integer, nullable=False)
    inbound_datetime_departure = db.Column(db.String(75), nullable=False)
    inbound_datetime_arrival = db.Column(db.String(75), nullable=False)
    base_fare = db.Column(db.Integer, nullable=False)
    taxes = db.Column(db.Integer, nullable=False)
    total_fare = db.Column(db.Integer, nullable=False)
    outbound_connecting_city = db.Column(db.String(75), nullable=True)
    inbound_connecting_city = db.Column(db.String(75), nullable=True)
    user = db.relationship('User', backref=db.backref('flights', order_by=user_id))



class SavedSearch(db.Model):

    """ Flight database info for travelers."""

    __tablename__ = "saved_searches"

    search_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable =False)
    flight_id = db.Column(db.Integer, db.ForeignKey('flights.flight_id'), nullable =False)
     


    # outbound_city_origin, outbound_city_final_destination, outbound_airline, outbound_flight_number, outbound_datetime_departure, outbound_datetime_arrival, inbound_city_origin, inbound_city_final_destination, inbound_airline, inbound_flight_number, inbound_datetime_departure, inbound_datetime_arrival, base_fare, taxes, total_fare, outbound_connecting_city, inbound_connecting_city 



#############################################################################
# Helper functions


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flightapp.db'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."


