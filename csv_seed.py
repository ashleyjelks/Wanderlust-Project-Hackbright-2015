from model import connect_to_db, db, Flight
from server import app
from dateutil import parser



def seed_flights():

    for line in open("dropflightstable.csv"):
        line.strip("\n")
        print line.split('"')

        # 123,,JFK,SEA,B6,63,"2015-09-02 09:01","2015-09-02 12:11",SEA,JFK,B6,464,"2015-09-16 13:19","2015-09-16 21:43",346,54,401,,

        flight_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
        user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
        outbound_city_origin = db.Column(db.String(75), nullable=False)
        outbound_city_final_destination = db.Column(db.String(75), nullable=False)
        outbound_airline_code = db.Column(db.String(75), nullable=False)
        outbound_airline_name = db.Column(db.String(75), nullable=False)
        outbound_flight_number = db.Column(db.Integer, nullable=False)
        outbound_datetime_departure = db.Column(db.String(75), nullable=False)
        outbound_datetime_arrival = db.Column(db.String(75), nullable=False)
        inbound_city_origin = db.Column(db.String(75), nullable=False)
        inbound_city_final_destination = db.Column(db.String(75), nullable=False)
        inbound_airline_code = db.Column(db.String(75), nullable=False)
        inbound_airline_name = db.Column(db.String(75), nullable=False)
        inbound_flight_number = db.Column(db.Integer, nullable=False)
        inbound_datetime_departure = db.Column(db.String(75), nullable=False)
        inbound_datetime_arrival = db.Column(db.String(75), nullable=False)
        outbound_destination_city_airport = db.Column(db.String(75), nullable=True)
        inbound_destination_city_airport = db.Column(db.String(75), nullable=True)
        outbound_city_airport = db.Column(db.String(75), nullable=True)
        inbound_city_airport = db.Column(db.String(75), nullable=True)
        base_fare = db.Column(db.Integer, nullable=False)
        taxes = db.Column(db.Integer, nullable=False)
        total_fare = db.Column(db.Integer, nullable=False)
        user = db.relationship('User', backref=db.backref('flights', order_by=user_id))
        
        # add_flight = Flight(outbound_city_origin=outbound_city_origin, outbound_city_final_destination=outbound_city_final_destination, outbound_airline=outbound_airline, outbound_flight_number=outbound_flight_number, outbound_datetime_departure=outbound_datetime_departure, outbound_datetime_arrival=outbound_datetime_arrival, inbound_city_origin=inbound_city_origin, inbound_city_final_destination=inbound_city_final_destination, inbound_airline=inbound_airline, inbound_flight_number=inbound_flight_number, inbound_datetime_departure=inbound_datetime_departure, inbound_datetime_arrival=inbound_datetime_arrival, base_fare=base_fare, taxes=taxes, total_fare=total_fare)

        # print add_flight

        # db.session.add(add_flight)

        # db.session.commit()



if __name__ == "__main__":
    connect_to_db(app)
    seed_flights()

