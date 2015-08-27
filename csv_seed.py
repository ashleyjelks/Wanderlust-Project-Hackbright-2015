from model import connect_to_db, db, Flight
from server import app
from dateutil import parser



def seed_flights():

    for line in open("newflightdata.csv"):

        print line[0:4]

        # 123,,JFK,SEA,B6,63,"2015-09-02 09:01","2015-09-02 12:11",SEA,JFK,B6,464,"2015-09-16 13:19","2015-09-16 21:43",346,54,401,,

        # old_id = 
        # blank_user =
        # outbound_city_origin=outbound_flight_origin,
        # outbound_city_final_destination=outbound_flight_destination, 
        # outbound_airline=outbound_airline,
        # outbound_flight_number=outbound_flight_number, 
        # outbound_datetime_departure=outbound_datetime_departure, 
        # outbound_datetime_arrival=outbound_datetime_arrival,
        # inbound_city_origin=inbound_flight_origin, 
        # inbound_city_final_destination=inbound_flight_destination, 
        # inbound_airline=inbound_airline,
        # inbound_flight_number=inbound_flight_number, 
        # inbound_datetime_departure=inbound_datetime_departure, 
        # inbound_datetime_arrival=inbound_datetime_arrival,
        # base_fare=base_fare, 
        # taxes=taxes, 
        # total_fare=total_fare


        null=None, null=None, outbound_city_origin, outbound_city_final_destination, outbound_airline, outbound_flight_number, outbound_datetime_departure, outbound_datetime_arrival, inbound_city_origin, inbound_city_final_destination, inbound_airline, inbound_flight_number, inbound_datetime_departure, inbound_datetime_arrival, base_fare, taxes, total_fare = line.split(",")

        
        # base_fare = base_fare[3:]
        # base_fare = int(float(base_fare))
        # taxes = taxes[3:]
        # taxes = int(float(taxes))
        # total_fare = total_fare[3:]
        # total_fare = int(float(total_fare))
        
        # outbound_datetime_departure = outbound_datetime_departure[1:17]
        # outbound_datetime_arrival = outbound_datetime_arrival[1:17]
        # inbound_datetime_departure = inbound_datetime_departure[1:17]        
        # inbound_datetime_arrival = inbound_datetime_arrival[1:17]
        
        add_flight = Flight(outbound_city_origin=outbound_city_origin, outbound_city_final_destination=outbound_city_final_destination, outbound_airline=outbound_airline, outbound_flight_number=outbound_flight_number, outbound_datetime_departure=outbound_datetime_departure, outbound_datetime_arrival=outbound_datetime_arrival, inbound_city_origin=inbound_city_origin, inbound_city_final_destination=inbound_city_final_destination, inbound_airline=inbound_airline, inbound_flight_number=inbound_flight_number, inbound_datetime_departure=inbound_datetime_departure, inbound_datetime_arrival=inbound_datetime_arrival, base_fare=base_fare, taxes=taxes, total_fare=total_fare)

        # print add_flight

        # db.session.add(add_flight)

        # db.session.commit()



if __name__ == "__main__":
    connect_to_db(app)
    seed_flights()

