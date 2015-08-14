""" Models and database functions for Wanderlust project. """

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


#################################################################

# Defining all Models in this database

# class CodeRegion(db.Model):

#     """ Aiport codes by region"""

#     __tablename__ = "code_regions"

#     region_id = db.Column(db.Integer, autoincrement=True, nullable=False)
#     code = db.Column(db.String(3), primary_key=True, nullable=False)
#     region = db.Column(db.String(35), nullable=False)


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
    outbound_city_origin = db.Column(db.String(75), nullable=False)
    outbound_city_final_destination = db.Column(db.String(75), nullable=False)
    outbound_airline = db.Column(db.String(75), nullable=False)
    outbound_flight_number = db.Column(db.Integer, nullable=False)
    outbound_datetime_departure = db.Column(db.DateTime, nullable=False)
    outbound_datetime_arrival = db.Column(db.DateTime, nullable=False)
    inbound_city_origin = db.Column(db.String(75), nullable=False)
    inbound_city_final_destination = db.Column(db.String(75), nullable=False)
    inbound_airline = db.Column(db.String(75), nullable=False)
    inbound_flight_number = db.Column(db.Integer, nullable=False)
    inbound_datetime_departure = db.Column(db.DateTime, nullable=False)
    inbound_datetime_arrival = db.Column(db.DateTime, nullable=False)
    base_fare = db.Column(db.Integer, nullable=False)
    taxes = db.Column(db.Integer, nullable=False)
    total_fare = db.Column(db.Integer, nullable=False)
    outbound_connecting_city = db.Column(db.String(75), nullable=True)
    inbound_connecting_city = db.Column(db.String(75), nullable=True)


class SavedSearch(db.Model):
#SavedSearch is a subclass of db.Model

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

#############################################################################
# Helper functions


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flights.db'
    db.app = app
    db.init_app(app)
    db.app.config["SQLALCHEMY_ECHO"] = True


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print "Connected to DB."














#     """ Model and database functions for Wanderlust project. """

# from flask_sqlalchemy import SQLAlchemy

# from config.sql import get_sql_config
# # get_sql_config knows if its testing, development, integration, production, so it nows which settings give you

# # example of sql config

# sql_config = {
#     'port': 8787,
#     'host': localhost,
#     'db': flights.db
# }

# sql_config = get_sql_config()
# db = SQLAlchemy(port=sql_config.get('port'), host=sql_config.get('host'), db=sql_config.get('db'))

# # RuntimeError: application not registered on db instance and no application bound to current context = ERROR THAT IS ONE THE PROBLEMS...WHY WON'T IT PASS THE 

# #################################################################

# # Defining all Models in this database

# class CodeRegion(db.Model):

#     """ Aiport codes by region"""

#     __tablename__ = "code_regions"

#     region_id = db.Column(db.Integer, autoincrement=True, nullable=False)
#     code = db.Column(db.String(3), primary_key=True, nullable=False)
#     region = db.Column(db.String(35), nullable=False)


# class User(db.Model):
#     #User is a sublclass of db.Model

#     """ User of Wanderlust Application """

#     __tablename__ = "users"

#     user_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
#     name = db.Column(db.String(150), nullable=False)
#     username = db.Column(db.String(150), nullable=True)
#     email = db.Column(db.String(150), nullable=False)
#     login = db.Column(db.String(100), nullable=False)
#     password = db.Column(db.String(100), nullable=False)


# class FlightLeg(db.Model):

#     """ Flight database info for travelers"""

#     __tablename__ = "flight_legs"

#     leg_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
#     city_origin = db.Column(db.String(75), nullable=False)
#     city_destination = db.Column(db.String(75), nullable=True)
#     airline = db.Column(db.String(75), nullable=False)
#     flight_number = db.Column(db.Integer, nullable=False)
#     datetime_departure = db.Column(db.DateTime, nullable=False)
#     datetime_arrival = db.Column(db.DateTime, nullable=False)


# class Flight(db.Model):

#     """ Flight database info for travelers"""

#     __tablename__ = "flights"

#     flight_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
#     outbound_flight_leg_id = db.Column(db.Integer, db.ForeignKey('flight_legs.leg_id'))
#     outbound_connecting_flight_leg_id = db.Column(db.Integer, db.ForeignKey('flight_legs.leg_id'), nullable=True)
#     inbound_flight_leg_id = db.Column(db.Integer, db.ForeignKey('flight_legs.leg_id'))
#     inbound_connecting_flight_leg_id = db.Column(db.Integer, db.ForeignKey('flight_legs.leg_id'), nullable=True)
#     base_fare = db.Column(db.Integer, nullable=False)
#     taxes = db.Column(db.Integer, nullable=False)
#     total_fare = db.Column(db.Integer, nullable=False)

#     outbound_leg = db.relationship('FlightLeg',
#                                    backref=('outbound_legs'),
#                                    foreign_keys=['Flight.outbound_flight_leg_id'])

#     outbound_connection_leg = db.relationship('FlightLeg',
#                                               backref=('outbound_connection_legs'),
#                                               foreign_keys=['Flight.outbound_connecting_flight_leg_id'])

#     inbound_leg = db.relationship('FlightLeg',
#                                   backref=('inbound_legs'),
#                                   foreign_keys=['Flight.inbound_flight_leg_id'])

#     inbound_connection_leg = db.relationship('FlightLeg',
#                                              backref=('inbound_connection_legs'),
#                                              foreign_keys=['Flight.inbound_connecting_flight_leg_id'])


# class SavedSearch(db.Model):
# #SavedSearch is a subclass of db.Model

#     """Database of saved user searches in Wanderlust Application"""

#     __tablename__ = "saved_searches"

#     search_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
#     search_info = db.Column(db.String(1000), nullable=True)
#     user_id = db.Column(db.Integer, nullable=False)


# class FlightUserMap(db.Model):

#     """ The association table for the many-to-many associations between users and flight tables"""

#     __tablename__ = "flight_user_maps"

#     mapping_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
#     flight_id = db.Column(db.Integer, db.ForeignKey('flights.flight_id'), nullable=False)

#     #Defines a relationship to a user
#     user = db.relationship("User", backref=db.backref("flight_user_maps", order_by=mapping_id))

#     flight = db.relationship("Flight", backref=db.backref("flight_user_maps", order_by=mapping_id))


# # #############################################################################
# Helper functions


# def connect_to_db(app):
#     """Connect the database to our Flask app."""

#     # Configure to use our SQLite database
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flights.db'
#     db.app = app
#     db.init_app(app)
#     db.app.config["SQLALCHEMY_ECHO"] = True


# if __name__ == "__main__":
#     # As a convenience, if we run this module interactively, it will leave
#     # you in a state of being able to work with the database directly.

#     from server import app
#     connect_to_db(app)
#     print "Connected to DB."

