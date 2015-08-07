""" Model and database functions for Wanderlust project. """

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


#################################################################

# Defining all Models in this database


class User(db.Model):
    #User is a sublclass of db.Model

    """ User of Wanderlust Application """

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(150), nullable=True)
    email = db.Column(db.String(150), nullable=False)
    login = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)


class Flight(db.Model):

    """ Flight database info for travelers"""

    __tablename__ = "flights"

    flight_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    
    origin_city_name = db.Column(db.String(75), nullable=False)
    origin_airport_name = db.Column(db.String(200), nullable=False)
    origin_airport_code = db.Column(db.String(3), nullable=False)
    origin_airline = db.Column(db.String(75), nullable=False)       
    origin_flight_number = db.Column(db.Integer, nullable=False)
    origin_datetime_departure = db.Column(db.DateTime, nullable=False)
    origin_datetime_arrival = db.Column(db.DateTime, nullable=False)
    origin_connection_city_name = db.Column(db.String(75), nullable=True)
    origin_connection_airport_name = db.Column(db.String(200), nullable=True)
    origin_connection_airport_code = db.Column(db.String(3), nullable=True)
    origin_connection_airline = db.Column(db.String(75), nullable=True)
    origin_connection_flight_number = db.Column(db.Integer, nullable=True)
    origin_connection_datetime_departure = db.Column(db.DateTime, nullable=True)
    origin_connection_datetime_arrival = db.Column(db.DateTime, nullable=True)
    return_city_name = db.Column(db.String(75), nullable=False)
    return_airport_name = db.Column(db.String(200), nullable=False)
    return_airport_code = db.Column(db.String(3), nullable=False)
    return_airline = db.Column(db.String(75), nullable=False)
    return_flight_number = db.Column(db.Integer, nullable=False)  
    return_datetime_departure = db.Column(db.DateTime, nullable=False)
    return_datetime_arrival =  db.Column(db.DateTime, nullable=False)
    return_connection_city_name = db.Column(db.String(75), nullable=True)
    return_connection_airport_name = db.Column(db.String(200), nullable=True)
    return_connection_airport_code = db.Column(db.String(3), nullable=True)
    return_connection_airline = db.Column(db.String(75), nullable=True)
    return_connection_flight_number = db.Column(db.Integer, nullable=True)
    return_connection_datetime_departure = db.Column(db.DateTime, nullable=True)
    return_connection_datetime_arrival = db.Column(db.DateTime, nullable=True)  
    base_fare = db.Column(db.Integer, nullable=False)
    taxes = db.Column(db.Integer, nullable=False)
    total_fare = db.Column(db.Integer, nullable=False)
    destination_region = db.Column(db.String(30), nullable=True)
    next_connection = db.Column(db.Integer, db.ForeignKey="flights.flight_id", nullable=True)
    #STILL NOT CLEAR ON HOW TO USE THIS ATTRIBUTES INSTEAD OF HAVING CONNECTION ATTRIBUTES


class SavedSearch(db.Model):
#Save is a subclass of db.Model

    """Database of saved user searches in Wanderlust Application"""

    __tablename__ = "saved_searches"

    search_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    search_info = db.Column(db.String(1000), nullable=True)
    user_id = db.Column(db.Integer, nullable=False)


class FlightUserMap(db.Model):

    """ The association table for the many-to-many associations between users and flight tables"""

    __tablename__ = "flight_user_maps"

    mapping_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey('flights.flight_id'), nullable=False)

    #Defines a relationship to a user
    user = db.relationship("User", backref=db.backref("flight_user_maps", order_by=mapping_id))

    flight = db.relationship("Flight", backref=db.backref("flight_user_maps", order_by=mapping_id))


##############################################################################
# Helper functions


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flights.db'
    db.app = app
    db.init_app(app)
    db.app.config["SQLALCHEMY_ECHO"] = True


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
