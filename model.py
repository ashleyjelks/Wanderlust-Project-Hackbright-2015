""" Model and database functions for Wanderlust project. """

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


#################################################################

# Defining all Models in this database

class CodeRegion(db.Model):

    """ Aiport codes by region"""

    __tablename__ = "code_regions"

    code = db.Column(db.String(3), primary_key=True, nullable=False)
    region = db.Column(db.String(35), nullable=False)


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


class FlightLeg(db.Model):

    """ Flight database info for travelers"""

    __tablename__ = "flight_legs"

    leg_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    city_name = db.Column(db.String(75), nullable=False)
    airport_name = db.Column(db.String(200), nullable=False)
    airport_code = db.Column(db.String(3), nullable=False)
    airline = db.Column(db.String(75), nullable=False)
    flight_number = db.Column(db.Integer, nullable=False)
    datetime_departure = db.Column(db.DateTime, nullable=False)
    datetime_arrival = db.Column(db.DateTime, nullable=False)


class Flight(db.Model):

    """ Flight database info for travelers"""

    __tablename__ = "flights"

    flight_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)

    origin_leg_id = db.Column(db.Integer, db.ForeignKey('flight_legs.leg_id'))
    origin_connection_leg_id = db.Column(db.Integer, db.ForeignKey('flight_legs.leg_id'), nullable=True)
    return_leg_id = db.Column(db.Integer, db.ForeignKey('flight_legs.leg_id'))
    return_connection_leg_id = db.Column(db.Integer, db.ForeignKey('flight_legs.leg_id'), nullable=True)
    base_fare = db.Column(db.Integer, nullable=False)
    taxes = db.Column(db.Integer, nullable=False)
    total_fare = db.Column(db.Integer, nullable=False)
    destination_region = db.Column(db.String(30), nullable=False)

    # origin_leg = db.Relationship('FlightLeg',
    #                              backref=db.backref('origin_legs'),
    #                              db.foreign_keys='Flight.origin_leg_id')

    origin_leg = db.relationship('FlightLeg',
                                 backref=('origin_legs'),
                                 foreign_keys=['Flight.origin_leg_id'])

    # origin_connection_leg = db.Relationship('FlightLeg',
    #                                         backref=db.backref('origin_connection_legs'),
    #                                         db.foreign_keys='Flight.origin_connection_leg_id')

    origin_connection_leg = db.relationship('FlightLeg',
                                            backref=('origin_connection_legs'),
                                            foreign_keys=['Flight.origin_connection_leg_id'])

    # return_leg = db.Relationship('FlightLeg',
    #                              backref=db.backref('return_legs'),
    #                              db.foreign_keys='Flight.return_leg_id')

    return_leg = db.relationship('FlightLeg',
                                 backref=('return_legs'),
                                 foreign_keys=['Flight.return_leg_id'])

    # reutun_connection_leg = db.Relationship('FlightLeg',
    #                                         backref=db.backref('return_connection_legs'),
    #                                         db.foreign_keys='Flight.return_connection_leg_id')

    return_connection_leg = db.relationship('FlightLeg',
                                            backref=('return_connection_legs'),
                                            foreign_keys=['Flight.return_connection_leg_id'])


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
