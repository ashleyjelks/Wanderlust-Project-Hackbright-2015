import urllib2
import json
import pprint
import dateutil.parser
from model import connect_to_db, db, Flight
from server import app

api_url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=AIzaSyCyyvZo3s217blnQ_fDVvnSKVILq98neFc"

USA_AIRPORT_CODES = ['SFO', 'LAX', 'PHX', 'SEA', 'DEN', 'DFW', 'IAH', 'ORD',
                     'ATL', 'MIA', 'IAD', 'PHL', 'JFK', 'BOS', 'CLT', 'LAS']
CANADIAN_AIRPORT_CODES = ["YUL", "YYZ", "YVR", "HNL"]
MEXICO_CARIBBEAN_AIRPORT_CODES = ["NAS", "MBJ", "HAV", "BGI", "POS", "SJU", "GCM", "MEX", "CUN"]
LATIN_AMERICAN_AIRPORT_CODES = ["SJO", "PTY", "CTG", "BOG", "UIO", "LIM", "EZE", "GIG", "CCS", "GRU"]
EUROPEAN_AIRPORT_CODES = ["LIS", "MAD", "CDG", "LHR", "DUB", "FCO", "ZRH", "GVA", "MXP",
                          "AMS", "TXL", "BRU", "FRA", "ATH", "BUD", "WAW", "DME", "ARN", "CPH"]
AFRICAN_AIRPORT_CODES = ["CAI", "TUN", "RAK", "CMN", "DKR", "LOS", "JNB", "CPT", "DAR", "NBO"]
ASIAN_AIRPORT_CODES = ["BOM", "DEL", "CGK", "SIN", "KUL", "HKT", "BKK", "PEK", "HND", "HKG",
                       "PVG", "ICN", "SGN", "MNL"]
MIDDLE_EASTERN_AIRPORT_CODES = ["RUH", "DXB", "IST", "TLV"]
OCEANIAN_AIRPORT_CODES = ["SYD", "MEL", "AKL", "PPT", "POM"]
CITY_COMBOS = [("SFO", "LAX"), ("SFO", "PHX"), ("SFO", "SEA"), ("SFO", "DEN"), ("SFO", "DFW"), ("SFO", "IAH"), ("SFO", "ORD"), ("SFO", "ATL"), ("SFO", "MIA")]
               # ("SFO", "IAD"),("SFO", "PHL"),("SFO", "JFK"),("SFO", "BOS"),("SFO", "CLT"),("SFO", "LAS"),("SFO", "YUL"),("SFO", "YYZ"),("SFO", "YVR")
               # ("SFO", "HNL"),("SFO", "NAS"),("SFO", "MBJ"),("SFO", "HAV"),("SFO", "BGI"),("SFO", "POS"),("SFO", "SJU"),("SFO", "GCM"),("SFO", "MEX")
               # ("SFO", "CUN"),("SFO", "SJO"),("SFO", "PTY"),("SFO", "CTG"),("SFO", "BOG"),("SFO", "UIO"),("SFO", "LIM"),("SFO", "EZE"),("SFO", "GIG")
               # ("SFO", "CCS"),("SFO", "GRU"),("SFO", "LIS"),("SFO", "MAD"),("SFO", "CDG"),("SFO", "LHR"),("SFO", "DUB"),("SFO", "FCO"),("SFO", "ZRH")
               # ("SFO", "GVA"),("SFO", "MXP"),("SFO", "AMS"),("SFO", "TXL"),("SFO", "BRU"),("SFO", "FRA"),("SFO", "ATH"),("SFO", "BUD"),("SFO", "WAW")
               # ("SFO", "DME"),("SFO", "ARN"),("SFO", "CPH"),("SFO", "CAI"),("SFO", "TUN"),("SFO", "RAK"),("SFO", "CMN"),("SFO", "DKR"),("SFO", "LOS")
               # ("SFO", "JNB"),("SFO", "CPT"),("SFO", "DAR"),("SFO", "NBO"),("SFO", "BOM"),("SFO", "DEL"),("SFO", "CGK"),("SFO", "SIN"),("SFO", "KUL")
               # ("SFO", "HKT"),("SFO", "BKK"),("SFO", "PEK"),("SFO", "HND"),("SFO", "HKG"),("SFO", "PVG"),("SFO", "ICN"),("SFO", "SGN"),("SFO", "MNL")
               # ("SFO", "RUH"),("SFO", "DXB"),("SFO", "IST"),("SFO", "TLV"),("SFO", "SYD"),("SFO", "MEL"),("SFO", "AKL"),("SFO", "PPT"),("SFO", "POM")]


def get_price(origin="SFO", destination="JFK", departure_date="2015-09-02", return_date="2015-09-16", max_price=2000):

    flight_request = {
        "request": {
            "passengers": {
                "kind": "qpxexpress#passengerCounts",
                "adultCount": 1,
            },
            "slice": [
                {
                    "kind": "qpxexpress#sliceInput",
                    "origin": origin,
                    "destination":  destination,
                    "date": departure_date,
                    "maxStops": 1,
                    "maxPrice": max_price
                },
                {
                    "kind": "qpxexpress#sliceInput",
                    "origin": destination,
                    "destination": origin,
                    "date": return_date,
                    "maxStops": 1,
                    "maxPrice": max_price
                }
            ],
            "refundable": "false",
            "solutions": 1

        }
    }
    print "1"
    jsonreq = json.dumps(flight_request, encoding='utf-8', indent=1)
    print "2"
    req = urllib2.Request(api_url, jsonreq, {'Content-Type': 'application/json'})
    print "3"
    flight = urllib2.urlopen(req)
    print "4"
    response = flight.read()
    print "5"
    flight.close()
    print "6"
    parsed_json = json.loads(response)
    print "7"
    printer = pprint.PrettyPrinter()
    print "8"
    printer.pprint(parsed_json)
    print "9"
    response = parsed_json
    print "10"
    outbound_flight_origin = response['trips']['tripOption'][0]['slice'][0]['segment'][0]['leg'][0]['origin']
    print "11"
    outbound_flight_destination = response['trips']['tripOption'][0]['slice'][0]['segment'][0]['leg'][0]['destination']
    print "12"
    outbound_airline = response['trips']['tripOption'][0]['slice'][0]['segment'][0]['flight']['carrier']
    print "13"
    outbound_flight_number = response['trips']['tripOption'][0]['slice'][0]['segment'][0]['flight']['number']
    print "14"

    outbound_datetime_departure = dateutil.parser.parse(response['trips']['tripOption'][0]['slice'][0]['segment'][0]['leg'][0]['departureTime'])
    print "15"
    print outbound_datetime_departure

    outbound_datetime_arrival = dateutil.parser.parse(response['trips']['tripOption'][0]['slice'][0]['segment'][0]['leg'][0]['arrivalTime'])
    print "16"
    inbound_flight_origin = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['leg'][0]['origin']
    print "17"
    inbound_flight_destination = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['leg'][0]['destination']
    print "18"
    inbound_airline = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['flight']['carrier']
    print "19"
    inbound_flight_number = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['flight']['number']
    print "20"
    inbound_datetime_departure = dateutil.parser.parse(response['trips']['tripOption'][0]['slice'][1]['segment'][0]['leg'][0]['departureTime'])
    print "21"
    inbound_datetime_arrival = dateutil.parser.parse(response['trips']['tripOption'][0]['slice'][1]['segment'][0]['leg'][0]['arrivalTime'])
    print "22"
    base_fare = response['trips']['tripOption'][0]['pricing'][0]['saleFareTotal']
    print "23"
    taxes = response['trips']['tripOption'][0]['pricing'][0]['saleTaxTotal']
    print "24"
    total_fare = response['trips']['tripOption'][0]['pricing'][0]['saleTotal']
    print "25"
    flight = Flight(outbound_city_origin=outbound_flight_origin, outbound_city_final_destination=outbound_flight_destination, outbound_airline=outbound_airline,
                    outbound_flight_number=outbound_flight_number, outbound_datetime_departure=outbound_datetime_departure, outbound_datetime_arrival=outbound_datetime_arrival,
                    inbound_city_origin=inbound_flight_origin, inbound_city_final_destination=inbound_flight_destination, inbound_airline=inbound_airline,
                    inbound_flight_number=inbound_flight_number, inbound_datetime_departure=inbound_datetime_departure, inbound_datetime_arrival=inbound_datetime_arrival,
                    base_fare=base_fare, taxes=taxes, total_fare=total_fare)
    print "26"
    db.session.add(flight)
    print "27"
    db.session.commit()
    print "28"

    return
    print "29"

if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()
    get_price()


# """
# YOU NEED TO CREATE AN INSTANCE OF THE FLIGHT CLASS TO INCLUDE FLIGHT DATA FOR THE 2ND TRAVELER,
# USE THIS CODE SNIPPET FROM SEED.PY FROM RATINGS
# new_user = User(user_id=new_user_id, age=user_age, zipcode=user_zipcode)
# #new_user is the object. new_user is also an instance of the User class.
# """


#     import urllib2
# import json
# import pprint
# from model import connect_to_db, db, CodeRegion
# # FlightLeg, 
#  # Flight
# from app import app
# from flight_codes import USA_AIRPORT_CODES, CANADIAN_AIRPORT_CODES, LATIN_AMERICAN_AIRPORT_CODES, 
#                          EUROPEAN_AIRPORT_CODES, AFRICAN_AIRPORT_CODES, ASIAN_AIRPORT_CODES, 
#                          MIDDLE_EASTERN_AIRPORT_CODES, OCEANIAN_AIRPORT_CODES
# # from time import sleep

# #PrettyPrint takes a dictionary and turns it into human readable  organization
# api_url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=AIzaSyCyyvZo3s217blnQ_fDVvnSKVILq98neFc"


# def populate_code_region_table():

#     for code in USA_AIRPORT_CODES:
#         usa = "USA"
#         new_code_region = CodeRegion(code=code, region=usa)
#         db.session.add(new_code_region)
#     db.session.commit()

#     # for code in CANADIAN_AIRPORT_CODES:
#     #     new_code_region = CodeRegion(code="CANADA")
#     #     db.session.add(new_code_region)

#     # for code in LATIN_AMERICAN_AIRPORT_CODES:
#     #     new_code_region = CodeRegion(code="LATIN AMERICA")
#     #     db.session.add(new_code_region)

#     # for code in EUROPEAN_AIRPORT_CODES:
#     #     new_code_region = CodeRegion(code="EUROPE")
#     #     db.session.add(new_code_region)

#     # for code in AFRICAN_AIRPORT_CODES:
#     #     new_code_region = CodeRegion(code="AFRICA")
#     #     db.session.add(new_code_region)

#     # for code in USA_AIRPORT_CODES:
#     #     new_code_region = CodeRegion(code="USA")
#     #     db.session.add(new_code_region)

#     # for code in ASIAN_AIRPORT_CODES:
#     #     new_code_region = CodeRegion(code="ASIA")
#     #     db.session.add(new_code_region)

#     # for code in MIDDLE_EASTERN_AIRPORT_CODES:
#     #     new_code_region = CodeRegion(code="MID-EAST")
#     #     db.session.add(new_code_region)

#     # for code in OCEANIAN_AIRPORT_CODES:
#     #     new_code_region = CodeRegion(code="AUSTRALIA/SOUTH PACIFIC")
#     #     db.session.add(new_code_region)

#     db.session.commit()


# # def get_price(origin="SFO", destination="LHR", departure_date="2015-09-02", return_date="2015-09-16", max_price=2000):

# #     flight_request = {
# #         "request": {
# #             "passengers": {
# #                 "kind": "qpxexpress#passengerCounts",
# #                 "adultCount": 1,
# #             },
# #             "slice": [
# #                 {
# #                     "kind": "qpxexpress#sliceInput",
# #                     "origin": origin,
# #                     "destination":  destination,
# #                     "date": departure_date,
# #                     "maxStops": 1,
# #                     "maxPrice": max_price
# #                 },
# #                 {
# #                     "kind": "qpxexpress#sliceInput",
# #                     "origin": destination,
# #                     "destination": origin,
# #                     "date": return_date,
# #                     "maxStops": 1,
# #                     "maxPrice": max_price
# #                 }
# #             ],
# #             "refundable": "false",
# #             "solutions": 1

# #         }
# #     }

# #     jsonreq = json.dumps(flight_request, encoding='utf-8', indent=1)
# #     req = urllib2.Request(api_url, jsonreq, {'Content-Type': 'application/json'})
# #     flight = urllib2.urlopen(req)
# #     response = flight.read()
# #     flight.close()
# #     parsed_json = json.loads(response)

# #     printer = pprint.PrettyPrinter()
# #     printer.pprint(parsed_json)
# #     return parsed_json


# # def seed_response(response):

# #     outbound_flight_origin = response['trips']['tripOption'][0]['slice'][0]['segment'][0]['leg'][0]['origin']
# #     outbound_flight_destination = response['trips']['tripOption'][0]['slice'][0]['segment'][0]['leg'][0]['destination']
# #     outbound_airline = response['trips']['tripOption'][0]['slice'][0]['segment'][0]['flight']['carrier']
# #     outbound_flight_number = response['trips']['tripOption'][0]['slice'][0]['segment'][0]['flight']['number']
# #     outbound_datetime_departure = response['trips']['tripOption'][0]['slice'][0]['segment'][0]['leg'][0]['departureTime']
# #     outbound_datetime_arrival = response['trips']['tripOption'][0]['slice'][0]['segment'][0]['leg'][0]['arrivalTime']
# #     new_outbound_leg = FlightLeg(outbound_flight_origin, outbound_flight_destination, outbound_airline,
# #                                  outbound_flight_number, outbound_datetime_departure, outbound_datetime_arrival)
# #     db.session.add(new_outbound_leg)
# #     db.session.commit()

# #     inbound_flight_origin = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['leg'][0]['origin']
# #     inbound_flight_destination = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['leg'][0]['destination']
# #     inbound_airline = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['flight']['carrier']
# #     inbound_flight_number = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['flight']['number']
# #     inbound_datetime_departure = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['leg'][0]['departureTime']
# #     inbound_datetime_arrival = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['leg'][0]['arrivalTime']
# #     new_inbound_leg = FlightLeg(inbound_flight_origin, inbound_flight_destination, inbound_airline,
# #                                 inbound_flight_number, inbound_datetime_departure, inbound_datetime_arrival)
# #     db.session.add(new_inbound_leg)
# #     db.session.commit()

# #     base_fare = response['trips']['tripOption'][0]['pricing'][0]['saleFareTotal']
# #     taxes = response['trips']['tripOption'][0]['pricing'][0]['saleTaxTotal']
# #     total_fare = response['trips']['tripOption'][0]['pricing'][0]['saleTotal']

# #     if len(response['trips']['tripOption'][0]['slice'][0]['segment']) > 1:

# #         outbound_connecting_flight_origin = response['trips']['tripOption'][0]['slice'][0]['segment'][1]['leg'][0]['origin']
# #         outbound_connecting_flight_destination = response['trips']['tripOption'][0]['slice'][0]['segment'][1]['leg'][0]['destination']
# #         outbound_connecting_airline = response['trips']['tripOption'][0]['slice'][0]['segment'][1]['flight']['carrier']
# #         outbound_connecting_flight_number = response['trips']['tripOption'][0]['slice'][0]['segment'][1]['flight']['number']
# #         outbound_connecting_datetime_departure = response['trips']['tripOption'][0]['slice'][0]['segment'][1]['leg'][0]['departureTime']
# #         outbound_connecting_datetime_arrival = response['trips']['tripOption'][0]['slice'][0]['segment'][1]['leg'][0]['arrivalTime']
# #         new_outbound_connecting_leg = FlightLeg(outbound_connecting_flight_origin, outbound_connecting_flight_destination,
# #                                                 outbound_connecting_airline, outbound_connecting_flight_number,
# #                                                 outbound_connecting_datetime_departure, outbound_connecting_datetime_arrival)
# #         db.session.add(new_outbound_connecting_leg)
# #         db.session.commit()

# #     else:
# #         new_outbound_connecting_leg = None

# #     if len(response['trips']['tripOption'][0]['slice'][1]['segment']) > 1:

# #         inbound_connecting_flight_origin = response['trips']['tripOption'][0]['slice'][1]['segment'][1]['leg'][0]['origin']
# #         inbound_connecting_flight_destination = response['trips']['tripOption'][0]['slice'][1]['segment'][1]['leg'][0]['destination']
# #         inbound_connecting_airline = response['trips']['tripOption'][0]['slice'][1]['segment'][1]['flight']['carrier']
# #         inbound_connecting_flight_number = response['trips']['tripOption'][0]['slice'][1]['segment'][1]['flight']['number']
# #         inbound_connecting_datetime_departure = response['trips']['tripOption'][0]['slice'][1]['segment'][1]['leg'][0]['departureTime']
# #         inbound_connecting_datetime_arrival = response['trips']['tripOption'][0]['slice'][1]['segment'][1]['leg'][0]['arrivalTime']
# #         new_inbound_connecting_leg = FlightLeg(inbound_connecting_flight_origin, inbound_connecting_flight_destination, inbound_connecting_airline,
# #                                                inbound_connecting_flight_number, inbound_connecting_datetime_departure, inbound_connecting_datetime_arrival)
# #         db.session.add(new_inbound_connecting_leg)
# #         db.session.commit()

# #     else:
# #         new_inbound_connecting_leg = None

# #     code_region = CodeRegion.get(outbound_flight_origin).one()

# #     region = code_region.region
# #     #from the code region object....it is attaching the code_region field to region?????? Get clarification on objects again!!!! In order to pass the airport codes to the model.py file and DB
# #     #they first had to be objects, not just strings....so abstract. Must understand this! Unclear on lines 182-184


# #     flight = Flight(new_outbound_leg, new_outbound_connecting_leg, new_inbound_leg, new_inbound_connecting_leg,
# #                     base_fare, taxes, total_fare)


# if __name__ == "__main__":
#     populate_code_region_table()
#     # get_price()
#     # seed_response()

