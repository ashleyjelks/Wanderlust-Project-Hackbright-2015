import urllib2
import json
import pprint
from model import FlightLeg, Flight
from model import db
# from time import sleep

#PrettyPrint takes a dictionary and turns it into human readable  organization
api_url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=AIzaSyCyyvZo3s217blnQ_fDVvnSKVILq98neFc"

USA_AIRPORT_CODES = ["SFO", "LAX", "PHX", "SEA", "DEN", "DFW", "IAH", "ORD",
                     "ATL", "MIA", "IAD", "PHL", "JFK", "BOS", "CLT", "LAS"]
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
CITY_COMBOS = [("SFO", "LAX"),("SFO", "PHX"),("SFO", "SEA"),("SFO", "DEN"),("SFO", "DFW"),("SFO", "IAH"),("SFO", "ORD"),("SFO", "ATL"),("SFO", "MIA")]
               # ("SFO", "IAD"),("SFO", "PHL"),("SFO", "JFK"),("SFO", "BOS"),("SFO", "CLT"),("SFO", "LAS"),("SFO", "YUL"),("SFO", "YYZ"),("SFO", "YVR")
               # ("SFO", "HNL"),("SFO", "NAS"),("SFO", "MBJ"),("SFO", "HAV"),("SFO", "BGI"),("SFO", "POS"),("SFO", "SJU"),("SFO", "GCM"),("SFO", "MEX")
               # ("SFO", "CUN"),("SFO", "SJO"),("SFO", "PTY"),("SFO", "CTG"),("SFO", "BOG"),("SFO", "UIO"),("SFO", "LIM"),("SFO", "EZE"),("SFO", "GIG")
               # ("SFO", "CCS"),("SFO", "GRU"),("SFO", "LIS"),("SFO", "MAD"),("SFO", "CDG"),("SFO", "LHR"),("SFO", "DUB"),("SFO", "FCO"),("SFO", "ZRH")
               # ("SFO", "GVA"),("SFO", "MXP"),("SFO", "AMS"),("SFO", "TXL"),("SFO", "BRU"),("SFO", "FRA"),("SFO", "ATH"),("SFO", "BUD"),("SFO", "WAW")
               # ("SFO", "DME"),("SFO", "ARN"),("SFO", "CPH"),("SFO", "CAI"),("SFO", "TUN"),("SFO", "RAK"),("SFO", "CMN"),("SFO", "DKR"),("SFO", "LOS")
               # ("SFO", "JNB"),("SFO", "CPT"),("SFO", "DAR"),("SFO", "NBO"),("SFO", "BOM"),("SFO", "DEL"),("SFO", "CGK"),("SFO", "SIN"),("SFO", "KUL")
               # ("SFO", "HKT"),("SFO", "BKK"),("SFO", "PEK"),("SFO", "HND"),("SFO", "HKG"),("SFO", "PVG"),("SFO", "ICN"),("SFO", "SGN"),("SFO", "MNL")
               # ("SFO", "RUH"),("SFO", "DXB"),("SFO", "IST"),("SFO", "TLV"),("SFO", "SYD"),("SFO", "MEL"),("SFO", "AKL"),("SFO", "PPT"),("SFO", "POM")]


def get_price(origin, destination, departure_date="2015-09-02", return_date="2015-09-16", max_price=2000):

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

    jsonreq = json.dumps(flight_request, encoding='utf-8', indent=1)
    req = urllib2.Request(api_url, jsonreq, {'Content-Type': 'application/json'})
    flight = urllib2.urlopen(req)
    response = flight.read()
    flight.close()
    parsed_json = json.loads(response)

    printer = pprint.PrettyPrinter()
    printer.pprint(parsed_json)
    return parsed_json


# def seed_response(response):

#     if len(response['trips']['data']['city']) == 2:
#         origin_city_name = response['trips']['data']['city'][1]['name']
#         origin_airport_name = response['trips']['data']['airport'][1]['name']
#         origin_airport_code = response['trips']['data']['city'][1]['code']
#         origin_airline = response['trips']['tripOption'][0]['slice'][0]['segment'][0]['flight']['carrier']
#         origin_flight_number = response['trips']['tripOption'][0]['slice'][0]['segment'][0]['flight']['number']
#         origin_datetime_departure = response['trips']['tripOption'][0]['slice'][0]['segment'][0]['leg'][0]['departureTime']
#         origin_datetime_arrival = response['trips']['tripOption'][0]['slice'][0]['segment'][0]['leg'][0]['arrivalTime']
#         return_city_name = response['trips']['data']['city'][0]['name']
#         return_airport_name = response['trips']['data']['airport'][0]['name']
#         return_airport_code = response['trips']['data']['city'][0]['code']
#         return_airline = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['flight']['carrier']
#         return_flight_number = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['flight']['number']
#         return_datetime_departure = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['leg'][0]['departureTime']
#         return_datetime_arrival = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['leg'][0]['arrivalTime']
#         base_fare = response['trips']['tripOption'][0]['pricing'][0]['saleFareTotal']
#         taxes = response['trips']['tripOption'][0]['pricing'][0]['saleTaxTotal']
#         total_fare = response['trips']['tripOption'][0]['pricing'][0]['saleTotal']

#     if len(response['trips']['data']['city']) == 3:

#         origin_city_name = response['trips']['data']['city'][2]['name']
#         origin_airport_name = response['trips']['data']['airport'][2]['name']
#         origin_airport_code = response['trips']['data']['city'][2]['code']
#         origin_airline = response['trips']['tripOption'][0]['slice'][0]['segment'][0]['flight']['carrier']
#         origin_flight_number = response['trips']['tripOption'][0]['slice'][0]['segment'][0]['flight']['number']
#         origin_datetime_departure = response['trips']['tripOption'][0]['slice'][0]['segment'][0]['leg'][0]['departureTime']
#         origin_datetime_arrival = response['trips']['tripOption'][0]['slice'][0]['segment'][0]['leg'][0]['arrivalTime']
#         origin_connection_city_name = response['trips']['data']['city'][0]['name']
#         origin_connection_airport_name = response['trips']['data']['airport'][0]['name']
#         origin_connection_airport_code = response['trips']['data']['city'][0]['code']
#         origin_connection_airline = response['trips']['tripOption'][0]['slice'][0]['segment'][1]['flight']['carrier']
#         origin_connection_flight_number = response['trips']['tripOption'][0]['slice'][0]['segment'][1]['flight']['number']
#         origin_connection_datetime_departure = response['trips']['tripOption'][0]['slice'][0]['segment'][1]['leg'][0]['departureTime']
#         origin_connection_datetime_arrival = response['trips']['tripOption'][0]['slice'][0]['segment'][1]['leg'][0]['arrivalTime'] 
#         return_city_name = response['trips']['data']['city'][0]['name']
#         return_airport_name = response['trips']['data']['airport'][0]['name']
#         return_airport_code = response['trips']['data']['city'][0]['code']
#         return_airline = response['trips']['tripOption'][0]['slice'][1]['segment'][1]['flight']['carrier']
#         return_flight_number = response['trips']['tripOption'][0]['slice'][1]['segment'][1]['flight']['number']
#         return_datetime_departure = response['trips']['tripOption'][0]['slice'][1]['segment'][1]['leg'][0]['departureTime']
#         return_datetime_arrival = response['trips']['tripOption'][0]['slice'][1]['segment'][1]['leg'][0]['arrivalTime']  
#         return_connection_city_name = response['trips']['data']['city'][1]['name']
#         return_connection_airport_name = response['trips']['data']['airport'][1]['name']
#         return_connection_airport_code = response['trips']['data']['city'][1]['code']
#         return_connection_airline = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['flight']['carrier']
#         return_connection_flight_number = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['flight']['number']
#         return_connection_datetime_departure = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['leg'][0]['departureTime']
#         return_connection_datetime_arrival = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['leg'][0]['arrivalTime']
#         base_fare = response['trips']['tripOption'][0]['pricing'][0]['saleFareTotal']
#         taxes = response['trips']['tripOption'][0]['pricing'][0]['saleTaxTotal']
#         total_fare = response['trips']['tripOption'][0]['pricing'][0]['saleTotal']


#     if len(response['trips']['data']['city']) == 4:


#     if code in EUROPEAN_AIRPORT_CODES:
#         destination_region = "EUROPE"

#     if code in AFRICAN_AIRPORT_CODES:
#         destination_region = "AFRICA"

#     if code in ASIAN_AIRPORT_CODES:
#         destination_region = "ASIA"

#     if code in MIDDLE_EASTERN_AIRPORT_CODES:
#         destination_region = "MIDDLE EAST"

#     if code in LATIN_AMERICAN_AIRPORT_CODES:
#         destination_region = "LATIN AMERICA"

#     if code in OCEANIAN_AIRPORT_CODES:
#         destination_region = "AUSTRALIA/PACIFIC"

#     if code in MEXICO_CARIBBEAN_AIRPORT_CODES:
#         destination_region = "MEXICO/CARIBBEAN"

#     if code in USA_AIRPORT_CODES:
#         destination_region = "USA"

#     if code in CANADIAN_AIRPORT_CODES:
#         destination_region = "CANADA"

#     new_origin_leg = FlightLeg(origin_city_name, origin_airport_name, origin_airport_code, origin_airline,
#                                origin_flight_number, origin_datetime_arrival, origin_datetime_departure)
#     db.session.add(new_origin_leg)
#     db.session.commit()

#     new_return_leg = FlightLeg(return_city_name, return_airport_name, return_airport_code, return_airline,
#                                return_flight_number, return_datetime_arrival, return_datetime_departure)
#     db.session.add(new_return_leg)
#     db.session.commit()

#     if origin_connection_city_name:
#         new_origin_connection_leg = FlightLeg(origin_connection_city_name, origin_connection_airport_name,
#                                               origin_connection_airport_code, origin_connection_airline,
#                                               origin_connection_flight_number, origin_connection_datetime_departure,
#                                               origin_connection_datetime_arrival)
#         db.session.add(new_origin_connection_leg)
#         db.session.commit()
#     else:
#         new_origin_connection_leg = None

#     if return_connection_city_name:
#         new_return_connection_leg = FlightLeg(return_connection_city_name, return_connection_airport_name,
#                                               return_connection_airport_code, return_connection_airline,
#                                               return_connection_flight_number, return_connection_datetime_departure,
#                                               return_connection_datetime_arrival)
#         db.session.add(new_return_connection_leg)
#         db.session.commit()
#     else:
#         new_return_connection_leg = None

#     new_flight = Flight(new_origin_leg, new_origin_connection_leg, new_return_leg,
#                         new_return_connection_leg, base_fare, taxes, total_fare, destination_region)
#     db.session.add(new_flight)
#     db.session.commit()


# if __name__ == "__main__":
#     # As a convenience, if we run this module interactively, it will leave
#     # you in a state of being able to work with the database directly.
#     for city in CITY_COMBOS:
#         data = get_price(city[0], city[1])
#         seed_response(data)




response['trips']['data']['city'][2]['name']
response['trips']['data']['airport'][2]['name']
response['trips']['data']['city'][2]['code']
response['trips']['tripOption'][0]['slice'][0]['segment'][0]['flight']['carrier']
response['trips']['tripOption'][0]['slice'][0]['segment'][0]['flight']['number']
response['trips']['tripOption'][0]['slice'][0]['segment'][0]['leg'][0]['departureTime']
response['trips']['tripOption'][0]['slice'][0]['segment'][0]['leg'][0]['arrivalTime']
      

response['trips']['data']['city'][0]['name']
response['trips']['data']['airport'][0]['name']
response['trips']['data']['city'][0]['code']
response['trips']['tripOption'][0]['slice'][0]['segment'][1]['flight']['carrier']
response['trips']['tripOption'][0]['slice'][0]['segment'][1]['flight']['number']
response['trips']['tripOption'][0]['slice'][0]['segment'][1]['leg'][0]['departureTime']
response['trips']['tripOption'][0]['slice'][0]['segment'][1]['leg'][0]['arrivalTime'] 



response['trips']['data']['city'][0]['name']
response['trips']['data']['airport'][0]['name']
response['trips']['data']['city'][0]['code']
response['trips']['tripOption'][0]['slice'][1]['segment'][1]['flight']['carrier']
response['trips']['tripOption'][0]['slice'][1]['segment'][1]['flight']['number']
response['trips']['tripOption'][0]['slice'][1]['segment'][1]['leg'][0]['departureTime']
response['trips']['tripOption'][0]['slice'][1]['segment'][1]['leg'][0]['arrivalTime']  
#         return_connection_city_name = response['trips']['data']['city'][1]['name']
#         return_connection_airport_name = response['trips']['data']['airport'][1]['name']
#         return_connection_airport_code = response['trips']['data']['city'][1]['code']
#         return_connection_airline = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['flight']['carrier']
#         return_connection_flight_number = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['flight']['number']
#         return_connection_datetime_departure = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['leg'][0]['departureTime']
#         return_connection_datetime_arrival = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['leg'][0]['arrivalTime']
#         base_fare = response['trips']['tripOption'][0]['pricing'][0]['saleFareTotal']
#         taxes = response['trips']['tripOption'][0]['pricing'][0]['saleTaxTotal']
#         total_fare = response['trips']['tripOption'][0]['pricing'][0]['saleTotal']
